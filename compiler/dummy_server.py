from BaseHTTPServer import HTTPServer, BaseHTTPRequestHandler

class ParseHandler(BaseHTTPRequestHandler):	
	def do_GET(self):
		f = open("test.json")
		res_body = f.read()
		self.send_response(200)
		self.send_header('Content-type', 'text/html; charset=UTF-8')
		self.send_header('Content-length', len(res_body))
		self.send_header('Access-Control-Allow-Origin','*')
		self.end_headers()
		self.wfile.write(res_body)

host = ''
port = 8880
httpd = HTTPServer((host,port),ParseHandler)

httpd.serve_forever()
