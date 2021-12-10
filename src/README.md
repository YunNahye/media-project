### Installation 

Clone this repository 
```bash
git clone https://github.com/media-project-2021/media-project.git
cd media-project/
```
Create environment 
```bash
conda env create -n waste_clf
```

Activate environment 
```bash
conda activate waste_clf
```

Install dependencies 
```bash
pip install -r requirements.txt
```



### Datasets & Training  
Datasets are collected by human effort, downloaded from several internet sites (kaggle, google, naver)
you can acquire our collected data from https://drive.google.com/drive/u/1/folders/1rsNvi2tOihz8pTIm1zLYmVx6Eiwd_4XN

To train our model, run the below code:
```bash
python train.py
```
after train finished _pth. formatted file will located in same directory. 

### Download trained network
our trained model file can be downloaded from https://drive.google.com/file/d/1PVe8MJyvTcWFaAXhzJn6n7rBhVwbx5nq/view?usp=sharing
make sure downloaded model file in same directory with video_stream.py

### Running model
To run the code, execute below code. 
```bash
python video_stream.py
```

### WebUI 
파이썬 먼저 실행 (video_stream.py)
video 서버 열린 후 react 실행 (새 터미널에서)
```
npm install
npm install react-router-dom
npm install socket.io-client
npm start
```
##### install 과정은 pull 하고 첫 실행시만 필요, 이후부터는 npm start로 실행 가능
video_stream 코드에서
```
loaded_model = load_checkpoint('13.pth')
```
부분 파라미터는 video_stream 위치 기준이 아닌 라이브러리가 설치 된 디렉토리 기준이므로 설정에 주의
./src/cv에서 파이썬 프로젝트 생성, model은 .gitignore에 추가

### Reference 

### Acknowledgements 
