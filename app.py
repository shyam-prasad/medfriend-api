
from flask import Flask, jsonify, request

from medicalRecords import returnRecord


app = Flask(__name__)


@app.route('/fetch/<string:value>')
def simulation(value):
    return jsonify({"message": "success", "data": returnRecord(value)})



