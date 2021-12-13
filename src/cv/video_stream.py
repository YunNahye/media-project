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
      region = frame[100:424, 100:424]
      pil_image = Image.fromarray(region, mode="RGB")
      pil_image = train_transforms(pil_image)
      image = pil_image.unsqueeze(0)

      result = loaded_model(image)
      prob, maximum = torch.max(result.data, 1)
      prediction = 0
      if -1.5 < prob:
          prediction = maximum.item()
      text = "scan the waste"
      socketIo.emit("message", prediction)
      cv2.putText(frame, text, (150, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
      cv2.rectangle(frame, (50, 50), (424, 424), (0, 255, 0), 2)
      ret, jpeg = cv2.imencode('.jpg', frame)
      return jpeg.tobytes()

def gen():
    while True:
        frame = webcam()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

@app.route('/cam')
def video_feed():
    return Response(gen(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/godeung')
def godeung():
  return render_template('고등동.html')

@app.route('/gwanggyo1')
def gwanggyo1():
  return render_template('광교1동.html')

@app.route('/gwanggyo2')
def gwanggyo2():
  return render_template('광교2동.html')

@app.route('/mangpo1')
def mangpo1():
  return render_template('망포1동.html')

@app.route('/mangpo2')
def mangpo2():
  return render_template('망포2동.html')

@app.route('/maegyo')
def maegyo():
  return render_template('매교동.html')

@app.route('/maetan1')
def maetan1():
  return render_template('매탄1동.html')

@app.route('/maetan2')
def maetan2():
  return render_template('매탄2동.html')

@app.route('/maetan3')
def maetan3():
  return render_template('매탄3동.html')

@app.route('/maetan4')
def maetan4():
  return render_template('매탄4동.html')

@app.route('/yeongtong1')
def yeongtong1():
  return render_template('영통1동.html')

@app.route('/yeongtong2')
def yeongtong2():
  return render_template('영통2동.html')

@app.route('/yeongtong3')
def yeongtong3():
  return render_template('영통3동.html')

@app.route('/uman1')
def uman1():
  return render_template('우만1동.html')

@app.route('/uman2')
def uman2():
  return render_template('우만2동.html')

@app.route('/woncheon')
def woncheon():
  return render_template('원천동.html')

@app.route('/ingye')
def ingye():
  return render_template('인계동.html')

@app.route('/ji')
def ji():
  return render_template('지동.html')

@app.route('/haenggung')
def haenggung():
  return render_template('행궁동.html')

@app.route('/hwaseo1')
def hwaseo1():
  return render_template('화서1동.html')

@app.route('/hwaseo2')
def hwaseo2():
  return render_template('화서2동.html')

if __name__ == '__main__':
  train_transforms = transforms.Compose([transforms.Resize(255),
                                           transforms.RandomRotation(30),
                                           transforms.RandomResizedCrop(224),
                                           transforms.RandomHorizontalFlip(),
                                           transforms.ToTensor(),
                                           transforms.Normalize([0.485, 0.456, 0.406],
                                                                [0.229, 0.224, 0.225])])
  loaded_model = load_checkpoint('FINAL.pth')

  classes = ['PET', 'bone', 'brown_glass', 'can', 'clothes', 'green_glass', 'husk', 'newspaper', 'paperbox', 'paperpack', 'seed', 'styrofoam', 'vinyl']

  socketIo.run(app, debug=True)