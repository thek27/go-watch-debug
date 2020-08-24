
apk update && apk add --no-cache git py-pip g++
go get github.com/go-delve/delve/cmd/dlv
pip install supervisor supervisor-stdout watchdog
/usr/bin/supervisord -n -c /go/dev/supervisord.conf