from flask import Flask, jsonify, request
from app.calculator import add, substract, multiply, divide


app = Flask(__name__)


@app.route("/add", methods=["GET"])
def add_route():
    a = float(request.args.get("a"))
    b = float(request.args.get("b"))
    return jsonify({"result": add(a, b)})


@app.route("/substract", methods=["GET"])
def susbtract_route():
    a = float(request.args.get("a"))
    b = float(request.args.get("b"))
    return jsonify({"result": substract(a, b)})


@app.route("/multiply", methods=["GET"])
def multiply_route():
    a = float(request.args.get("a"))
    b = float(request.args.get("b"))
    return jsonify({"result": multiply(a, b)})


@app.route("/divide", methods=["GET"])
def divide_route():
    a = float(request.args.get("a"))
    b = float(request.args.get("b"))
    return jsonify({"result": divide(a, b)})


if __name__ == "__main__":
    app.run(debug=True)
