from flask import Flask, request, jsonify
import json

app = Flask(__name__)

with open("database.json") as f:
    pages = json.load(f)

@app.route("/search")
def search():

    q = request.args.get("q","").lower()
    results = []

    for page in pages:
        if q in page["title"].lower() or q in page["content"].lower():
            results.append(page)

    return jsonify(results)

app.run(port=5000)
