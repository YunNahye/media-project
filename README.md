### 실행 방법
#### 파이썬 먼저 실행 (video_stream.py)
#### video 서버 열린 후 react 실행 (새 터미널에서)
```
npm install
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