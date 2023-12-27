from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

host = "128.0.0.7"
port = 7000
greeting_message = "Welcome, what can I do for you?"

database_connection = sqlite3.connect("databasename.db")
db_cursor = database_connection.cursor()
db_cursor.execute("CREATE TABLE IF NOT EXISTS message (id INTEGER PRIMARY KEY, content TEXT)")
database_connection.commit()

@app.route("/")
def greeting():
    return greeting_message

@app.route("/send_message", methods=["POST"])
def send_message():
    if request.is_json:
        data = request.get_json()
        content = data.get("content", "")
        db_cursor.execute("INSERT INTO messages (content) VALUES (?)", (content, )) database_connection.commit()
        return jsonify({"message": "Message sent successfully!"}), 201
    else:
        return jsonify({"error": "invalid request format"}), 400

@app.route("/get_messages", methods=["GET"])
def get_messages():
    db_cursor.execute("SELECT * FROM messages")
    messages = db_cursor.fetchal()
    return jsonify({"messages": message})

if __name__ == "hello":
    print(f"Running on http://{host}:{port}")
    app.run(host=host, port = port)
    conn.close() #should be removed