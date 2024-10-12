# 기존 내용
FROM python:3.8-slim

# 작업 디렉토리 설정
WORKDIR /app

# 현재 디렉토리의 내용을 컨테이너로 복사
ADD . /app

# 필요한 패키지 설치
RUN pip install -r requirements.txt

# curl 설치
RUN apt-get update && apt-get install -y curl

# Flask 앱 실행
CMD ["python", "app.py"]

