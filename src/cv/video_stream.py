from logging import debug
import cv2
import platform
import torch
from PIL import ImageFont, ImageDraw, Image
import torchvision.transforms as transforms
from flask import Flask, render_template, Response
from flask_socketio import SocketIO, send

app = Flask(__name__)

socketIo = SocketIO(app, cors_allowed_origins="*")

@socketIo.on("message")
def handleMessage(msg):
  print(msg)
  send(msg, broadcast=True)
  return None

capture = cv2.VideoCapture(0)

@app.route('/')
def index():
  return render_template('index.js')

def load_checkpoint(path):
    checkpoint = torch.load(path)
    model = checkpoint['model']
    model.load_state_dict(checkpoint['state_dict'])
    for parameter in model.parameters():
        parameter.requires_grad = False
    return model.eval()

def webcam():
      ret, frame = capture.read()
      region = frame[100:324, 100:324]
      pil_image = Image.fromarray(region, mode="RGB")
      pil_image = train_transforms(pil_image)
      image = pil_image.unsqueeze(0)

      result = loaded_model(image)
      _, maximum = torch.max(result.data, 1)
      prediction = maximum.item()
      text = classes[prediction]
      socketIo.emit("message", prediction)
      cv2.putText(frame, text, (100, 100), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)
      cv2.rectangle(frame, (100, 100), (324, 324), (255, 0, 0), 2)
      ret, jpeg = cv2.imencode('.jpg', frame)
      return jpeg.tobytes()

def gen():
    while True:
        frame = webcam()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

@app.route('/video_feed')
def video_feed():
    return Response(gen(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
  train_transforms = transforms.Compose([transforms.Resize(255),
                                           transforms.RandomRotation(30),
                                           transforms.RandomResizedCrop(224),
                                           transforms.RandomHorizontalFlip(),
                                           transforms.ToTensor(),
                                           transforms.Normalize([0.485, 0.456, 0.406],
                                                                [0.229, 0.224, 0.225])])
  loaded_model = load_checkpoint('C:/Users/zuu03/media_project/media-project/src/cv/13.pth')

  classes = ['plastic', 'brown_glass', 'can', 'cloth', 'green_glass', 'newspaper', 'paperbox', 'paperpack',
                'styrofoam', 'vinyl', 'white_glass']

  socketIo.run(app, debug=True)