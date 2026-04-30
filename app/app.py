from flask import Flask, jsonify
import random

app = Flask(__name__)

@app.route("/")
def home():
    return "AI DevOps Running"

@app.route("/health")
def health():
    if random.choice([True, False]):
        return jsonify({"status": "FAIL"}), 500
    return jsonify({"status": "OK"})

@app.route("/fail")
def fail():
    return 1/0  # force error

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)