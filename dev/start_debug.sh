
apk update && apk add --no-cache git g++ python2
python -m ensurepip
pip install --upgrade pip setuptools
rm -r /root/.cache

go get github.com/go-delve/delve/cmd/dlv

pip install supervisor supervisor-stdout watchdog
/usr/bin/supervisord -n -c /go/dev/supervisord.conf