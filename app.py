from flask import Flask, render_template, request, jsonify
from math import *

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/calculate", methods=["POST"])
def calculate():
    try:
        data = request.json
        expr = data.get("expression", "")
        expr = expr.replace("^", "**").replace("π", str(pi))

        # Limit available functions for security
        allowed_funcs = {
            "sin": sin, "cos": cos, "tan": tan,
            "log": log, "sqrt": sqrt, "exp": exp,
            "pi": pi, "e": e
        }

        result = eval(expr, {"__builtins__": {}}, allowed_funcs)
        return jsonify(result=str(result))
    except Exception:
        return jsonify(result="Error")
