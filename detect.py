import ultralytics
from ultralytics import YOLO

model_path = 'C:/Users/lala/OneDrive/Documents/model/last97.pt'
model = YOLO(model_path)
results = model(source='C:/Users/lala/OneDrive/Documents/model/testformodel/NG_Image_16-44-51_jpg.rf.9fda32352fecd450fa0b96d9d3aaf9c7.jpg', conf=0.3,save=True)
