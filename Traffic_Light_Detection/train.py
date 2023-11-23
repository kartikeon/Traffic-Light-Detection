from ultralytics import YOLO

# Load a model
model = YOLO('yolov8n.pt')  # load a pretrained model (recommended for training)

# Train the model
results = model.train(data="data_custom.yaml", epochs=50, imgsz=640, batch=8)

# yolo detect train data=data_custom.yaml model=yolov8n.pt epochs=50 imgsz=640 batch=8
