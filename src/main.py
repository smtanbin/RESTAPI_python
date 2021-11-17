from http.server import BaseHTTPRequestHandler, HTTPServer
from router import router
import ast

# host = 'regalia.standardbankbd.com'
host = '127.0.0.1'
port = 3007


class MyServer(BaseHTTPRequestHandler):
    def _set_response(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/json')
        self.end_headers()

    def do_GET(self):
        self._set_response()
        payload = router('GET', self.path)
        self.wfile.write(payload.encode(encoding='utf_8'))

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])  # <--- Gets the size of data
        body = self.rfile.read(content_length)  # <--- Gets the data itself
        body = ast.literal_eval(body.decode('UTF-8'))  # <--- Byte to Dictionary

        payload = router('POST', self.path, body)
        self._set_response()
        self.wfile.write(payload.encode(encoding='utf_8'))


if __name__ == '__main__':
    webServer = HTTPServer((host, port), MyServer)
    print("Regalia Online")
    print(f'Server link: http://{host}:{port}')

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print('Server stopped.')
