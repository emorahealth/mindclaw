import http.server
import socketserver
import os
import subprocess

PORT = 8080

class ASMHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/poc':
            # Run v2.6 Proof of Coherence
            print("🦞 Serving Proof of Coherence request...")
            # Use absolute path to ensure correct execution
            script_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'security/proof-of-coherence.sh')
            subprocess.run(['bash', script_path], capture_output=True)
            
            report_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'COHERENCE_REPORT.txt')
            
            if os.path.exists(report_path):
                self.send_response(200)
                self.send_header('Content-type', 'text/plain')
                self.end_headers()
                with open(report_path, 'rb') as f:
                    self.wfile.write(f.read())
            else:
                self.send_error(500, "PoC Generation Failed")
        else:
            self.send_error(404, "Endpoint Not Found")

if __name__ == "__main__":
    with socketserver.TCPServer(("", PORT), ASMHandler) as httpd:
        print(f"🦞 ASM Sovereign Webhook listening on port {PORT}")
        httpd.serve_forever()
