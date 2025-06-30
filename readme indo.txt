cara jalankan webnya:
1. jalankan nomor 3 jika terkeluar (deactive) dari venv
2. python app.py
3. klik link atau "http://127.0.0.1:5000" (untuk mengrefrest web secara manual ctrl+s di app.py)


cara membuatnya:
1. buat sturkur dari projek
2. python3 -m venv venv (ini untuk menyimpan libary)
3. source venv/bin/activate (ini untuk mengaktifkan libary)
4. jalakan pip install -r requirements.txt pada therminal
5. lalu jalankan perintah "cara jalankan webnya"


```UAS/
├── app.py             # Aplikasi utama Flask
├── mainh.py           # Logika utama untuk deteksi kendaraan dari video
├── tracker.py         # Logika pelacakan untuk memberi ID unik pada kendaraan
├── coco.txt           # Daftar label objek dari model YOLO
├── yolov8s.pt         # Model YOLOv8 pra-latih
├── requirements.txt   # Daftar library Python yang dibutuhkan
├── README.md          # Dokumentasi proyek versi bahasa Inggris
├── readme indo.txt    # Dokumentasi proyek versi Bahasa Indonesia

├── templates/         # Template HTML untuk tampilan web
│   └── index.html     # Halaman utama unggah video

├── static/            # File statis seperti gambar untuk website
│   └── mobil_ikon.png # Ikon yang digunakan di halaman web

├── uploads/           # Folder sementara untuk menyimpan video yang diunggah
├── outputs/           # Folder untuk menyimpan video hasil deteksi
├── video test/        # Video uji coba
├── venv/              # Lingkungan virtual Python
└── __pycache__/  
```
