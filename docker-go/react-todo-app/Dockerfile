# Dockerfile
FROM node:14

# 작업 디렉토리 설정
WORKDIR /app

# 패키지 파일 복사
COPY package*.json ./

# 패키지 설치
RUN npm install

# 애플리케이션 소스 복사
COPY . .

# 포트 노출
EXPOSE 80

# 애플리케이션 실행
CMD ["npm", "start"]
