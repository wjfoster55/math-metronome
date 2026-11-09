import os
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer

if __name__ == "__main__":
    port = int(os.environ.get("PORT", "8080"))
    ThreadingHTTPServer(("0.0.0.0", port), SimpleHTTPRequestHandler).serve_forever()
