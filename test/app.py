from flask import Flask, request
import logging
from logging.handlers import RotatingFileHandler

app = Flask(__name__)

# Configure logging
handler = RotatingFileHandler('access.log', maxBytes=10000, backupCount=1)
handler.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(remote_addr)s - %(method)s - %(url)s - %(status)d')
handler.setFormatter(formatter)
app.logger.addHandler(handler)

@app.before_request
def log_request_info():
    app.logger.info(f"{request.method} {request.url}")

@app.after_request
def log_response_info(response):
    app.logger.info(f"{response.status_code} {request.method} {request.url}")
    return response

@app.route("/")
def hello():
    return "Hello World !!!! fasten your seat belts going to takeout devops"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
