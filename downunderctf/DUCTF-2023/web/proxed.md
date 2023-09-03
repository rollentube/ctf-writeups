# proxed (beginner)
Cool haxxorz only

Author: Jordan Bertasso

http://proxed.duc.tf:30019

## Files
proxed.tar.gz

## Solution
The website just shows the following text:
```
$ curl http://proxed.duc.tf:30019
untrusted IP: 10.152.0.14
$
```
Here we can't find any interesting.

If take a look at the provided source code, we find the go file _main.go_:
```go
package main

import (
        "flag"
        "fmt"
        "log"
        "net/http"
        "os"
        "strings"
)

var (
        port = flag.Int("port", 8081, "The port to listen on")
)

func main() {

        flag.Parse()

        http.HandleFunc("/", func(w http.ResponseWriter, r *http.Request) {
                xff := r.Header.Values("X-Forwarded-For")

                ip := strings.Split(r.RemoteAddr, ":")[0]

                if xff != nil {
                        ips := strings.Split(xff[len(xff)-1], ", ")
                        ip = ips[len(ips)-1]
                        ip = strings.TrimSpace(ip)
                }

                if ip != "31.33.33.7" {
                        message := fmt.Sprintf("untrusted IP: %s", ip)
                        http.Error(w, message, http.StatusForbidden)
                        return
                } else {
                        w.Write([]byte(os.Getenv("FLAG")))
                }
        })

        log.Printf("Listening on port %d", *port)
        log.Fatal(http.ListenAndServe(fmt.Sprintf(":%d", *port), nil))
}
```

Taking a closer look at the main function, we see that the program loads the value of the X-Forwarded-For (XFF) header into the variable `xff` and the remote address of the http request into the variable `ip`.

If the XFF header was set and the variable has any value, the program saves the last entry of the header into `ip` and validates if it's matchting to the ip _31.33.33.7_. If it is, we get our flag. if not, we get the already shown text.

But if the XFF isn't set, `ip` still contains the remote address.

So to get the flag we have to set the X-Forwarded-For header to the ip 31.33.33.7 in the http request. The main.go will check if the content matches and returns the flag.

To do so, we can use any tool to manipulate a http header. With BurpSuite it looks like the following:
[XFF](images/proxed.png)

As we can see the response is the flag: `DUCTF{17_533m5_w3_f0rg07_70_pr0x}`
