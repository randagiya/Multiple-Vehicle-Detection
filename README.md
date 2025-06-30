# Multiple Vehicle Detection

This project detects and counts vehicles (cars, motorbikes, trucks, buses) on a highway using YOLOv8 and Flask for web integration.

---

## 🚀 How to Run the Web

1. **Activate Virtual Environment**  
   If you haven't activated the virtual environment, do:
   - On Windows:  
     `venv\Scripts\activate`
   - On Linux/Mac:  
     `source venv/bin/activate`

2. **Install Dependencies**  
   Run:  
   `pip install -r requirements.txt`

3. **Run the Web Application**  
   Run the Flask app:  
   `python app.py`

4. **Access the Website**  
   Open: [http://127.0.0.1:5000](http://127.0.0.1:5000)  
   *(To refresh manually: save `app.py` with Ctrl+S if using auto-reloader)*

---

## 🛠 How to Set Up

1. Clone or create the project structure
2. Create virtual environment:  
   `python -m venv venv`
3. Activate the environment (see step 1 above)
4. Install requirements:  
   `pip install -r requirements.txt`
5. Run the web (see "How to Run the Web")

---

## 📁 Project Structure
```UAS/
├── app.py # Main Flask application
├── mainh.py # Core logic for video processing and vehicle detection
├── tracker.py # Assigns unique IDs to detected vehicles (tracking logic)
├── coco.txt # List of object labels used by YOLO
├── yolov8s.pt # Pre-trained YOLOv8 model (not shown above but assumed)
├── requirements.txt # Python dependencies
├── README.md # Project documentation

├── templates/ # HTML templates for the web interface
│ └── index.html

├── static/ # Static files used by the website
│ └── mobil_ikon.png

├── uploads/ # Temporarily stores uploaded videos
├── outputs/ # Stores processed videos
├── video test/ # Test video samples
├── venv/ # Python virtual environment
└── pycache/ # Python cache files (auto-generated)
```
