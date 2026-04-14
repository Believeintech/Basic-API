from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "Welcome to Python App 🚀"

@app.route("/health")
def health():
    return jsonify(status="UP")

@app.route("/hello")
def hello():
    return jsonify(message="Hello, DevOps Learner!")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)