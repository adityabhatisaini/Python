import http.server
import socketserver
import webbrowser
import os

# Define the port number
PORT = 8000

# Set the working directory to the location of the HTML file
html_file_path = r"A:\AIDTM\Python\Python\Python Programs\index.html"
directory = os.path.dirname(html_file_path)
os.chdir(directory)

# Start an HTTP server
Handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print(f"Serving at http://localhost:{PORT}")
    # Automatically open the browser with the correct file
    webbrowser.open(f"http://localhost:{PORT}/index.html")
    httpd.serve_forever()
