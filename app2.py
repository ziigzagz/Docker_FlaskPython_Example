from flask import Flask
server = Flask(__name__)

@server.route("/")
def index():
    return "Hello World! From App 2"

if __name__ == "__main__":
    server.run(host='0.0.0.0')