
# YOLOv8 Human Detection & Counting (Windows 11)
A real-time **Human Detection and Counting system** built using **YOLOv8**, **OpenCV**, and a **Tkinter-based GUI**.  
The application supports **Webcam**, **Video Files**, and **IP/RTSP streams**, making it suitable for surveillance, traffic monitoring, and crowd analysis use cases.

## Features
- Real-time **human detection and counting**
- Powered by **YOLOv8 (Ultralytics)**
- GUI built using **Tkinter**
- Supports multiple input sources:
  - Webcam
  - Video files (`.mp4`, `.avi`, `.mkv`)
  - IP Camera / RTSP streams
- Dynamic bounding boxes with live count overlay
- Optimized filtering to avoid false detections
- Windows 11 compatible

  ## 🔹 Tech Stack

- Python 3.9+
- YOLOv8 (Ultralytics)
- OpenCV
- Tkinter
- Pillow (PIL)

## Setup (Windows 11)
```bash
python -m venv venv
venv\Scripts\activate
pip install --upgrade pip
pip install -r requirements.txt
pip install ultralytics opencv-python pillow
```

## Run
```bash
python app.py
```

## Notes
Use the GUI buttons to select:
Webcam
Video File
IP / RTSP Stream
- Internet required only once to download YOLOv8 weights
- Press Q to stop video
  
🔹 Output Screenshot
Below is a sample output showing real-time human detection and counting on a traffic video stream:
<img width="1919" height="1074" alt="image" src="https://github.com/user-attachments/assets/22f3dcf8-bd5f-4876-a1f7-e92194bd94b9" />
![Uploading Screenshot 2026-01-25 115710.png…]()


🔹 Use Cases

Crowd monitoring

Traffic analysis

Surveillance systems

Smart city applications

Public safety analytics

🔹 Future Enhancements

Person tracking (DeepSORT)

Entry / Exit counting

ROI-based counting

GPU (CUDA) acceleration

Windows .exe build

Multi-camera support

🔹 Author

Rupali Kale
Data Science | Machine Learning | Computer Vision
