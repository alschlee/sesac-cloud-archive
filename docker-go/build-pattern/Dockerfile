FROM    golang
WORKDIR /myapp
COPY    helloworld.go .
RUN     go env -w GO111MODULE=auto
RUN     go build -o helloworld .
ENTRYPOINT ["./helloworld"]