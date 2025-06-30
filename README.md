"# multiple-vehicle-detection" 
# Multiple-Vehicle-Detection
This is a project about detecting and counting vehicles passing on the highway which can already detect cars, motorbikes, trucks, buses.

how to run the web:
1. run number 3 if exited (deactivated) from venv
2. python.py application
3. click the link or "http://127.0.0.1:5000" (to refresh the web manually ctrl+s in app.py)

how to make it:
1. create a structure from the project
2. python3 -m venv venv (this is to store the library)
3. venv\Scripts\Activate or source venv/bin/activate (this is to activate the library)
4. run pip install -r requirements.txt on the terminal
5. then run the command "how to run the web"

structure:
UAS/
│
├── __pycache__/
├── outputs/                 # to temporarily save the processed video
├── static/                  # to save images needed by the website
│   └── mobil_ikon.png
├── templates/               # to save html from the website
│   └── index.html
├── uploads/                  # to temporarily save the video that will be processed from website input
├── venv/                     # Virtual environment
├── video test/               # Virtual environment (tidak perlu dikirim saat deploy)
│
├── app.py                   # main file to run and link buttons, other files, and folders
├── coco.txt                 # to store a list of object tables from the yolo model
├── mainh.py                 #file which is the core logic for vehicle detection from video, one of which is the file that uses                               tracker.py for processing
├── tracker.py               #file to track a car or a file that can be called to give a unique ID to an object
├── .......
