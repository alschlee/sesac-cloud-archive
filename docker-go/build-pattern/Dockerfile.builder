# 소스 코드 빌드를 위한 이미지 생성에 사용
FROM    golang
WORKDIR /myapp
COPY    helloworld.go .
RUN     go env -w GO111MODULE=auto
RUN     go build -o helloworld .