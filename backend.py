from flask import Flask, jsonify, request
from web3 import Web3
import json

app = Flask(__name__)

# Initialize Web3 with Infura provider
infura_url = "https://mainnet.infura.io/v3/41ae0eaf3dbf4df3ba4501d285e9c16a"
web3 = Web3(Web3.HTTPProvider(infura_url))

# Load contract ABI
with open("StudentRecordABI.json", "r") as f:
    contract_abi = json.load(f)

# Set contract address
contract_address = "0xf8e81D47203A594245E36C48e151709F0C19fBe8"

# Instantiate contract
contract = web3.eth.contract(address=contract_address, abi=contract_abi)


@app.route("/")
def index():
    return app.send_static_file("index.html")


@app.route("/add_record", methods=["POST"])
def add_record():
    data = request.get_json()
    student_id = data.get("student_id")
    name = data.get("name")
    grade = data.get("grade")
    if not all([student_id, name, grade]):
        return jsonify({"message": "Missing required fields in request"}), 400

    # Example: Call the addStudent function
    transaction_hash = contract.functions.addStudent(student_id, name, grade).transact()

    # Get transaction receipt
    receipt = web3.eth.waitForTransactionReceipt(transaction_hash)

    # Check transaction status
    if receipt.status == 1:
        return jsonify({"message": "Student record added successfully"}), 201
    else:
        return jsonify({"message": "Transaction failed"}), 500


@app.route("/verify", methods=["POST"])
def verify_student():
    data = request.get_json()
    student_id = data.get("student_id")
    name = data.get("name")
    grade = data.get("grade")
    if not all([student_id, name, grade]):
        return jsonify({"message": "Missing required fields in request"}), 400

    # Example: Call the verifyStudent function
    result = contract.functions.verifyStudent(student_id, name, grade).call()

    if result:
        return jsonify({"message": "Student record matches"}), 200
    else:
        return jsonify({"message": "Student record does not match"}), 404


if __name__ == "__main__":
    app.run(debug=True)
