import cv2
import platform
import torch
from PIL import ImageFont, ImageDraw, Image
import torchvision.transforms as transforms


def load_checkpoint(path):
    checkpoint = torch.load(path)
    model = checkpoint['model']
    model.load_state_dict(checkpoint['state_dict'])
    for parameter in model.parameters():
        parameter.requires_grad = False
    return model.eval()


train_transforms = transforms.Compose([transforms.Resize(255),
                                           transforms.RandomRotation(30),
                                           transforms.RandomResizedCrop(224),
                                           transforms.RandomHorizontalFlip(),
                                           transforms.ToTensor(),
                                           transforms.Normalize([0.485, 0.456, 0.406],
                                                                [0.229, 0.224, 0.225])])
loaded_model = load_checkpoint('13.pth')

classes = ['plastic', 'brown_glass', 'can', 'cloth', 'green_glass', 'newspaper', 'paperbox', 'paperpack',
               'styrofoam', 'vinyl', 'white_glass']
src = 0
if platform.system() == 'Windows':
    captrue = cv2.VideoCapture(src, cv2.CAP_DSHOW)

else:
    captrue = cv2.VideoCapture(src)
captrue.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
captrue.set(cv2.CAP_PROP_FRAME_HEIGHT, 360)
while captrue.isOpened():

    (grabbed, frame) = captrue.read()
    region = frame[100:324, 100:324]
    pil_image = Image.fromarray(region, mode="RGB")
    pil_image = train_transforms(pil_image)
    image = pil_image.unsqueeze(0)

    result = loaded_model(image)
    _, maximum = torch.max(result.data, 1)
    prediction = maximum.item()
    text = classes[prediction]
    cv2.putText(frame, text, (100, 100), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)
    cv2.rectangle(frame, (100, 100), (324, 324), (255, 0, 0), 2)
    if grabbed:
        cv2.imshow('Wandlab Camera Window', frame)

        key = cv2.waitKey(1) & 0xFF
        # ESC키 끄기
        if (key == 27):
            break

captrue.release()
cv2.destroyAllWindows()