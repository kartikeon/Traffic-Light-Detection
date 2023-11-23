from ultralytics import YOLO

model = YOLO("tld_model_epo_50.pt")


# On Image
results = model(source='test_put/jk.jpg', show=True, conf=0.3, save=True, boxes=True)

# On Video
# results = model(source='test_put/j.mp4', show=True, conf=0.3, save=True, boxes=True)

# On Webcam
# results = model(source=0, show=True, conf=0.3, save=True, boxes=True)

# predict with custom model
# yolo detect predict model=tld_model_epo_50.pt source='test_put/h.jpg'
