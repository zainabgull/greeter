from datetime import date
from http.server import BaseHTTPRequestHandler, HTTPServer

GREETING = "Hi"
NAME = "Zainab"


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        body = f"<h1>{GREETING}, {NAME}!</h1><p>Life is like riding a bicycle. To keep your balance, you must keep moving.</p>"
        self.send_response(200)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.end_headers()
        self.wfile.write(body.encode())


if __name__ == "__main__":
    print("Greeter listening on port 8080", flush=True)
    HTTPServer(("0.0.0.0", 8080), Handler).serve_forever()
