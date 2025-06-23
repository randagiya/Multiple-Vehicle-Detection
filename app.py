from flask import Flask, render_template, request, url_for, Response, redirect
import os
from mainh import process_video

ALLOWED_EXTENSIONS = {'.mp4', '.avi', '.mov', '.mkv', '.webm'}

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
OUTPUT_FOLDER = 'outputs'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

def allowed_file(filename, mimetype):
    ext = os.path.splitext(filename)[1].lower()
    return (ext in ALLOWED_EXTENSIONS) and mimetype.startswith('video/')

@app.route('/', methods=['GET', 'POST'])
def index():
    error = None
    if request.method == 'POST':
        video = request.files.get('video')
        if not video:
            error = "Tidak ada file yang diupload."
        elif not allowed_file(video.filename, video.mimetype):
            error = "File yang diupload harus berupa video (mp4, avi, mov, mkv, webm)!"
        else:
            input_path = os.path.join(UPLOAD_FOLDER, video.filename)
            output_path = os.path.join(OUTPUT_FOLDER, f"output_{video.filename}")
            video.save(input_path)
            # Proses video
            process_video(input_path, output_path)
            # Hapus file upload setelah proses selesai
            if os.path.exists(input_path):
                os.remove(input_path)
            output_video_name = os.path.basename(output_path)
            return render_template('index.html', output_video=output_video_name, error=None)
    return render_template('index.html', output_video=None, error=error)

@app.route('/download/<filename>')
def download_file(filename):
    file_path = os.path.join(OUTPUT_FOLDER, filename)
    if not os.path.exists(file_path):
        return "File not found.", 404

    def generate():
        with open(file_path, "rb") as f:
            while True:
                chunk = f.read(4096)
                if not chunk:
                    break
                yield chunk
        # Setelah seluruh file dikirim ke user, hapus file output
        try:
            os.remove(file_path)
            print(f"[INFO] Output file deleted: {file_path}")
        except Exception as e:
            print(f"[ERROR] Error deleting file: {e}")

    response = Response(generate(), mimetype="video/mp4")
    response.headers.set('Content-Disposition', 'attachment', filename=filename)
    return response

@app.route('/reset')
def reset():
    # Hapus semua file di uploads dan outputs
    for folder in [UPLOAD_FOLDER, OUTPUT_FOLDER]:
        for fname in os.listdir(folder):
            fpath = os.path.join(folder, fname)
            try:
                os.remove(fpath)
            except Exception as e:
                print(f"Gagal menghapus {fpath}: {e}")
    # Redirect ke halaman utama
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
