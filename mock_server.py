# ! -*- coding: utf-8 -*-
from http.server import HTTPServer, BaseHTTPRequestHandler
import json
import time

# 监听地址和端口
host = ('0.0.0.0', 8080)

class Resquest(BaseHTTPRequestHandler):
    def handler(self):
        print("data:", self.rfile.readline().decode())
        self.wfile.write(self.rfile.readline())

    def do_GET(self):
        data = {
            'hello': 'world',
        }
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps(data).encode())

    def do_POST(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/event-stream')
        self.end_headers()
        texts = ['这', '是', '一个', '笑话', '。', '']
        data = {
            'Choices': [
                {
                    'Delta': {
                        'Role': 'assistant',
                        'Content': '',
                    },
                },
            ],
        }
        for i in range(texts.__len__()):
            data.get('Choices')[0].get('Delta')['Content'] = texts[i]
            if i == texts.__len__() - 1:
                data.get('Choices')[0]['FinishReason'] = 'stop'
            self.wfile.write('data: '.encode('utf-8'))
            self.wfile.write(json.dumps(data).encode('utf-8'))
            self.wfile.write(b'\n\n')
            # time.sleep(1)

if __name__ == '__main__':
    server = HTTPServer(host, Resquest)
    print("Starting server, listen at: %s:%s" % host)
    server.serve_forever()
