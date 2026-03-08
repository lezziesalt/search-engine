from flask import Flask, request, jsonify
import json

app = Flask(__name__)

# load search database
with open("database.json") as f:
    pages = json.load(f)

# load bookmarks
try:
    with open("bookmarks.json") as f:
        bookmarks = json.load(f)
except:
    bookmarks = {}

@app.route("/search")
def search():

    q = request.args.get("q","").lower()
    results = []

    for page in pages:
        if q in page["title"].lower() or q in page["content"].lower():
            results.append(page)

    return jsonify(results)

@app.route("/bookmark", methods=["POST"])
def bookmark():

    ip = request.remote_addr
    data = request.json

    if ip not in bookmarks:
        bookmarks[ip] = []

    bookmarks[ip].append(data)

    with open("bookmarks.json","w") as f:
        json.dump(bookmarks,f)

    return {"status":"saved"}

@app.route("/bookmarks")
def get_bookmarks():

    ip = request.remote_addr
    return jsonify(bookmarks.get(ip, []))

app.run(port=5000)
