# 🚦 Traffic-Light-Detection

A deep learning-based traffic light detection system using **YOLOv8**. This project supports training, prediction, and benchmarking of traffic light detection models using custom datasets.

---

![Demo](Traffic_Light_Detection\traffsign.gif)

## 📌 Features

- ✅ Train custom YOLOv8 model for traffic light detection  
- ✅ Predict and visualize detection results on images and videos  
- ✅ Benchmark model performance using evaluation metrics  

---

## 🧰 Software and Tools

- **YOLOv8 (Ultralytics)**
- Python (>=3.8)
- Command-line interface for training and inference

---

## 📋 Tasks

### 🔹 Train

Train a YOLOv8 model using annotated traffic light images.

```bash
yolo task=detect mode=train model=yolov8n.pt data=data.yaml epochs=50 imgsz=640
```

### 🔹 Predict

Perform inference using the trained model on images or videos.

```bash
yolo task=detect mode=predict model=best.pt source=path/to/image_or_video
```

### 🔹 Benchmark

Evaluate model accuracy on the validation dataset.

```bash
yolo task=detect mode=val model=best.pt data=data.yaml
```

---

## 🤝 Contributing

Contributions are welcome! Feel free to submit pull requests or open issues for feature requests and bugs.

---

## 📜 License

This project is licensed under the [MIT License](LICENSE).