import cv2
import pandas as pd
from ultralytics import YOLO
import cvzone
<<<<<<< HEAD
from tracker import Tracker

def process_video(input_path, output_path):
    print(f"\n[PROSES] Mulai proses deteksi: {input_path}")
    model = YOLO('yolov8s.pt')
    with open("coco.txt", "r") as my_file:
        class_list = my_file.read().split("\n")
    cap = cv2.VideoCapture(input_path)
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = int(cap.get(cv2.CAP_PROP_FPS))
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    print(f"[INFO] Info video: resolusi={width}x{height}, fps={fps}, total frame={total_frames}")
    out = cv2.VideoWriter(output_path, cv2.VideoWriter_fourcc(*'mp4v'), fps, (1020, 500))
    tracker = Tracker()
    count = 0

    while True:
        ret, frame = cap.read()
        if not ret:
            print("[PROSES] Video selesai diproses.")
            break
        count += 1
        frame = cv2.resize(frame, (1020, 500))
        results = model.predict(frame, verbose=False)
        detections = results[0].boxes.data
        px = pd.DataFrame(detections).astype("float")
        mobil, bus, truk, motor = [], [], [], []

        for index, row in px.iterrows():
            x1 = int(row[0])
            y1 = int(row[1])
            x2 = int(row[2])
            y2 = int(row[3])
            d = int(row[5])
            label = class_list[d]
            if 'car' in label:
                mobil.append([x1, y1, x2, y2])
            elif 'bus' in label:
                bus.append([x1, y1, x2, y2])
            elif 'truck' in label:
                truk.append([x1, y1, x2, y2])
            elif 'motorcycle' in label:
                motor.append([x1, y1, x2, y2])

        kotak_mobil = tracker.update(mobil)
        kotak_motor = tracker.update(motor)
        kotak_bus = tracker.update(bus)
        kotak_truk = tracker.update(truk)

        # JUMLAH kendaraan sedang terdeteksi di frame ini
        n_mobil = len(kotak_mobil)
        n_motor = len(kotak_motor)
        n_bus = len(kotak_bus)
        n_truk = len(kotak_truk)

        for bbox in kotak_mobil:
            x1, y1, x2, y2, id = bbox
            label = "Mobil"
            # Merah
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 255), 2)
            cvzone.putTextRect(frame, f"{label} {id}", (x1, y1 - 25), 1, 1, colorB=(0,0,255), colorT=(255,255,255))
        for bbox in kotak_motor:
            x1, y1, x2, y2, id = bbox
            label = "Motor"
            # Ungu
            cv2.rectangle(frame, (x1, y1), (x2, y2), (128, 0, 128), 2)
            cvzone.putTextRect(frame, f"{label} {id}", (x1, y1 - 25), 1, 1, colorB=(128,0,128), colorT=(255,255,255))
        for bbox in kotak_bus:
            x1, y1, x2, y2, id = bbox
            label = "Bus"
            # Kuning
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 255), 2)
            cvzone.putTextRect(frame, f"{label} {id}", (x1, y1 - 25), 1, 1, colorB=(0,255,255), colorT=(0,0,0))
        for bbox in kotak_truk:
            x1, y1, x2, y2, id = bbox
            label = "Truk"
            # Abu-abu
            cv2.rectangle(frame, (x1, y1), (x2, y2), (128, 128, 128), 2)
            cvzone.putTextRect(frame, f"{label} {id}", (x1, y1 - 25), 1, 1, colorB=(128,128,128), colorT=(255,255,255))

        # Tampilkan jumlah di kiri atas setiap frame
        cv2.putText(frame,
                    f"Mobil: {n_mobil} | Motor: {n_motor} | Bus: {n_bus} | Truk: {n_truk}",
                    (10, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (50, 50, 255), 2)

        out.write(frame)
    cap.release()
    out.release()
    print("[PROSES] Output video disimpan:", output_path)
=======
from tracker import*  # Ensure the Tracker class is defined correctly in tracker.py

# Load the YOLO model
model = YOLO('yolov8s.pt')

# Function to print the mouse position in RGB window
def RGB(event, x, y, flags, param):
    if event == cv2.EVENT_MOUSEMOVE:
        point = [x, y]
        print(point)

# Create a named window and set a mouse callback function
cv2.namedWindow('RGB')
cv2.setMouseCallback('RGB', RGB)
cap = cv2.VideoCapture('semarang_test.mp4')  # Initialize video capture with the video file

# Open the 'coco.txt' file containing class names and read its content
with open("coco.txt", "r") as my_file:
    class_list = my_file.read().split("\n")  # Split the content by newline to get a list of class names

# Initialize counters and trackers
count = 0
car_count = 0
bus_count = 0
truck_count = 0
tracker = Tracker()
cy1 = 184
cy2 = 209
offset = 8

# Start processing the video frame by frame
while True:
    ret, frame = cap.read()  # Read a frame from the video
    if not ret:  # If no frame is read (end of video), break the loop
        break
    count += 1  # Increment frame count
    if count % 3 != 0:  # Process every third frame
        continue
    frame = cv2.resize(frame, (1020, 500))  # Resize the frame for consistent processing

    # Predict objects in the frame using YOLO model
    results = model.predict(frame)
    detections = results[0].boxes.data
    px = pd.DataFrame(detections).astype("float")  # Convert the prediction results into a pandas DataFrame

    # Initialize a list to store bounding boxes for each vehicle type
    cars, buses, trucks = [], [], []

    # Iterate over the detection results and categorize them into cars, buses, or trucks
    for index, row in px.iterrows():
        x1 = int(row[0])
        y1 = int(row[1])
        x2 = int(row[2])
        y2 = int(row[3])
        d = int(row[5])
        c = class_list[d]
        if 'car' in c:
            cars.append([x1, y1, x2, y2])
        elif 'bus' in c:
            buses.append([x1, y1, x2, y2])
        elif 'truck' in c:
            trucks.append([x1, y1, x2, y2])

    # Update tracker for each vehicle type
    cars_boxes = tracker.update(cars)
    buses_boxes = tracker.update(buses)
    trucks_boxes = tracker.update(trucks)

    # Draw lines on the frame that the vehicles are supposed to cross
    cv2.line(frame, (1, cy1), (1018, cy1), (0, 255, 0), 2)
    cv2.line(frame, (3, cy2), (1016, cy2), (0, 0, 255), 2)

    # Check each car, bus, and truck
    for bbox in cars_boxes:
        cx = int((bbox[0] + bbox[2]) / 2)
        cy = int((bbox[1] + bbox[3]) / 2)
        if (cy > cy1 - offset) and (cy < cy1 + offset):
            car_count += 1

    for bbox in buses_boxes:
        cx = int((bbox[0] + bbox[2]) / 2)
        cy = int((bbox[1] + bbox[3]) / 2)
        if (cy > cy1 - offset) and (cy < cy1 + offset):
            bus_count += 1

    for bbox in trucks_boxes:
        cx = int((bbox[0] + bbox[2]) / 2)
        cy = int((bbox[1] + bbox[3]) / 2)
        if (cy > cy1 - offset) and (cy < cy1 + offset):
            truck_count += 1

    # Draw and annotate each vehicle
    for bbox in cars_boxes + buses_boxes + trucks_boxes:
        cv2.rectangle(frame, (bbox[0], bbox[1]), (bbox[2], bbox[3]), (255, 0, 255), 2)
        cvzone.putTextRect(frame, f'{bbox[4]}', (bbox[0], bbox[1]), 1, 1)

    # Display the frame in the 'RGB' window
    cv2.imshow("RGB", frame)
    if cv2.waitKey(1) & 0xFF == 27:  # Break the loop if 'Esc' key is pressed
        break

# Print the total count for each vehicle type
print(f'Total car count: {car_count}')
print(f'Total bus count: {bus_count}')
print(f'Total truck count: {truck_count}')

# Release the video capture and destroy all OpenCV windows
cap.release()
cv2.destroyAllWindows()
>>>>>>> 2359e48a856f7c4c8bf91b23171e77e1cbb16246
