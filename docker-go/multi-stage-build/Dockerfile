FROM    golang  AS builder
WORKDIR /myapp
COPY    helloworld.go .
RUN     go env -w GO111MODULE=auto
RUN     go build -o helloworld .


FROM    alpine  AS runtime
WORKDIR /myapp
COPY    --from=builder /myapp/helloworld .
ENTRYPOINT ["./helloworld"]