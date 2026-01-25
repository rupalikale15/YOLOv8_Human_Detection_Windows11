
import cv2
from ultralytics import YOLO
import tkinter as tk
from tkinter import filedialog, simpledialog, messagebox
from PIL import Image, ImageTk
import threading

model = YOLO("yolov8n.pt")

class HumanCounterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("YOLOv8 Human Detection & Counting")
        self.cap = None
        self.running = False

        self.label = tk.Label(root)
        self.label.pack()

        btn_frame = tk.Frame(root)
        btn_frame.pack(pady=10)

        tk.Button(btn_frame, text="Webcam", command=self.open_webcam).grid(row=0, column=0, padx=5)
        tk.Button(btn_frame, text="Video File", command=self.open_video).grid(row=0, column=1, padx=5)
        tk.Button(btn_frame, text="IP / RTSP", command=self.open_stream).grid(row=0, column=2, padx=5)
        tk.Button(btn_frame, text="Stop", command=self.stop).grid(row=0, column=3, padx=5)

    def open_webcam(self):
        self.start_capture(0)

    def open_video(self):
        path = filedialog.askopenfilename(filetypes=[("Video Files", "*.mp4 *.avi *.mkv")])
        if path:
            self.start_capture(path)

    def open_stream(self):
        url = simpledialog.askstring("Stream URL", "Enter IP/RTSP URL")
        if url:
            self.start_capture(url)

    def start_capture(self, source):
        if self.running:
            self.stop()
        self.cap = cv2.VideoCapture(source)
        if not self.cap.isOpened():
            messagebox.showerror("Error", "Unable to open source")
            return
        self.running = True
        threading.Thread(target=self.update_frame, daemon=True).start()

    def stop(self):
        self.running = False
        if self.cap:
            self.cap.release()

    def update_frame(self):
        while self.running:
            ret, frame = self.cap.read()
            if not ret:
                break

            results = model(frame, classes=[0], conf=0.4, verbose=False)
            count = 0

            for r in results:
                for box in r.boxes:
                    x1, y1, x2, y2 = map(int, box.xyxy[0])
                    cv2.rectangle(frame, (x1,y1), (x2,y2), (0,255,0), 2)
                    count += 1

            cv2.putText(frame, f"Humans: {count}", (20,40),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255), 2)

            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            img = Image.fromarray(frame)
            img = img.resize((800, 500))
            imgtk = ImageTk.PhotoImage(image=img)

            self.label.imgtk = imgtk
            self.label.config(image=imgtk)

        self.stop()

if __name__ == "__main__":
    root = tk.Tk()
    app = HumanCounterApp(root)
    root.mainloop()
