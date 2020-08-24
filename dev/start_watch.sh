apk update && apk add --no-cache git
go get github.com/canthefason/go-watcher
go install github.com/canthefason/go-watcher/cmd/watcher
cd /go/src/example
watcher