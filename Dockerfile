FROM golang:alpine
WORKDIR /go/src/example
ADD src /go/src/example
RUN go build
RUN mv example /
RUN rm -rf /go
WORKDIR /
CMD ["/example"]
