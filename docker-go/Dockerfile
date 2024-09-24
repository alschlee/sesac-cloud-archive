# 베이스 이미지를 지정 (저장소 이름이 없으므로, Docker Hub에서 가져오는 공식 이미지를 의미)
# https://hub.docker.com/_/golang
# https://docs.docker.com/reference/dockerfile/#from
#FROM golang:1.23.1


# 컨테이너 내부에 /echo 작업 디렉터리를 생성
# https://docs.docker.com/reference/dockerfile/#run
#RUN mkdir /echo


# 작업 디렉터리에 main.go 파일을 복사
# https://docs.docker.com/reference/dockerfile/#copy
#COPY ./go/main.go /echo


# 컨테이너가 실행될 때 go run /echo/main.go 명령어를 실행
# https://docs.docker.com/reference/dockerfile/#cmd
#CMD ["go", "run", "/echo/main.go"]

#FROM    ubuntu
#ENV     workspace=/workspace
# mkdir /workspace 와 같은 의미
#RUN     mkdir $workspace  
#WORKDIR $workspace
#RUN     touch $workspace/mytouchfile

# dockerfile에volume 추가
FROM    ubuntu
RUN     mkdir /home/share
RUN     echo test >> /home/share/testfile
VOLUME  /home/share
