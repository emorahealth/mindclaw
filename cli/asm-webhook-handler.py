import http.server
import socketserver
import os

PORT = 8080

class ASMHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/poc':
            # Trigger PoC generation
            os.system("./public_work/proof-of-coherence.sh")
            if os.path.exists('COHERENCE_REPORT.txt'):
                self.send_response(200)
                self.send_header('Content-type', 'text/plain')
                self.end_headers()
                with open('COHERENCE_REPORT.txt', 'rb') as f:
                    self.wfile.write(f.read())
            else:
                self.send_error(500, "PoC Generation Failed")
        else:
            self.send_error(404, "Endpoint Not Found")

if __name__ == "__main__":
    with socketserver.TCPServer(("", PORT), ASMHandler) as httpd:
        print(f"🦞 ASM Webhook listening on port {PORT}")
        httpd.serve_forever()
