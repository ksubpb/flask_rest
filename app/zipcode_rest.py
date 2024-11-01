from flask import Flask, request, jsonify
import sys

app = Flask(__name__)
app.json.ensure_ascii = False # 日本語文字化け対策

import database

db = database.ZipCodeBuilder().build(sys.argv[1]) # sys.argv[1] には，CSV ファイルが指定されている．

@app.route("/zipcode/<int:zipcode>", methods=["GET"])
def get_address(zipcode):
    if zipcode in db:
        return db[zipcode].to_json(), 200
    return jsonify({ "message": f"{zipcode}: ZipCode Not Found" }), 404

@app.route("/zipcode/<int:zipcode>", methods=["DELETE"])
def delete_address(zipcode):
    if zipcode in db:
        del db[zipcode]
    return jsonify({ "message": f"{zipcode}: ZipCode Deleted" }), 200

@app.route("/zipcode/<int:zipcode>", methods=["PUT"])
def update_address(zipcode):
    if zipcode not in db:
        return jsonify({ "message": f"{zipcode}: ZipCode Not Found" }), 404
    json = request.get_json()
    db[zipcode].pref = json["pref"]
    db[zipcode].address = json["address"]
    db[zipcode].address_yomi = json["address_yomi"]
    return jsonify({ "message": f"{zipcode}: ZipCode Updated", "item": db[zipcode].to_json() }), 200
    

@app.route("/zipcode/<int:zipcode>", methods=["POST"])
def register_address(zipcode):
    if zipcode in db:
        return { "message": f"{zipcode}: ZipCode Already Exists" }, 409
    json = request.get_json()
    db[zipcode] = database.ZipCode(zipcode, json["pref"], json["address"], json["address_yomi"])
    return jsonify({ "message": f"{zipcode}: ZipCode Registered", "item": db[zipcode].to_json() }), 201

@app.route("/zipcode/prefs/<pref>", methods=["GET"])
def get_addresses_in_pref(pref):
    print(f"pref: {pref}")
    result = []
    for entry in db.values():
        if entry.pref == pref:
            result.append(entry)
    if len(result) == 0:
        return jsonify({ "message": f"{pref}: Pref Not Found" }), 404
    return jsonify(([entry.to_json() for entry in result])), 200

app.run(port = 5000, debug = True, host = "0.0.0.0")
