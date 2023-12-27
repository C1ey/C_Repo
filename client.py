from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

server_host = "128.0.0.7"
server_url = f" http://{server_host}:{7000}"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/send_message", methods=["POST"])
def send_message():
    content = request.form.get("content", "")
    response = requests.post(f"{server_url}/send_message", json={"content": content})
    return jsonify(response.json())

    @app.route("/get_messages", methods=["GET"])
    def get_messages():
        response = requests.get(f"{server_url}/get_messages")
        messages=response.json().get("messages", [])
        return render_template("messages.html", messages=messages)

if __name__ =="__main__":
    app.run(debug=True)