from http.server import BaseHTTPRequestHandler, HTTPServer
from socketserver import ThreadingMixIn
from llama_cpp import Llama
import urllib.parse
import json

# Initialize the LLM
llm = Llama(
    model_path="/models/model.gguf",
    n_ctx=2048,
    n_threads=4
)

class ThreadedHTTPServer(ThreadingMixIn, HTTPServer):
    """Handle requests in separate threads"""

class ChatHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(self._get_html().encode())
        else:
            self.send_error(404)

    def do_POST(self):
        if self.path == '/chat':
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            data = urllib.parse.parse_qs(post_data.decode())

            user_input = data.get('message', [''])[0]
            response = llm.create_chat_completion(
                messages=[{"role": "user", "content": user_input}]
            )
            ai_response = response['choices'][0]['message']['content']

            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps({'response': ai_response}).encode())
        else:
            self.send_error(404)

    def _get_html(self):
        return open('index.html').read()

if __name__ == '__main__':
    server = ThreadedHTTPServer(('0.0.0.0', 8000), ChatHandler)
    print("Server running on http://0.0.0.0:8000")
    server.serve_forever()
