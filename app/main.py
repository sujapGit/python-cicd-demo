from flask import Flask, jsonify, request
from app.calculator import add,substract,multiply,divide


app = Flask(__name__) 

@app.route("/add", methods=["GET"])
def add_route():
    a = float(request.args.get("a"))
    b =float(request.args.get("b"))
    return jsonify({"result":add(a,b)})



if __name__ == "__main__":
    app.run(debug=True)




