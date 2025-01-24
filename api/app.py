from flask import Flask, request, jsonify
import json
from flask_cors import CORS


app = Flask(__name__)
CORS(app)

# Load the data
with open("q-vercel-python.json", "r") as f:
    data = json.load(f)


@app.route("/api", methods=["GET"])
def get_marks():
    names = request.args.getlist("name")
    marks = [student["marks"] for student in data if student["name"] in names]
    return jsonify({"marks": marks})


if __name__ == "__main__":
    app.run()