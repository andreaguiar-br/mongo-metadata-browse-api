from flask import Flask, jsonify, request
import schemaDBApi

app = Flask(__name__)

@app.route("/")
def hello_world():
    return jsonify(hello="world")


@app.route("/database")
def listDatabases():
    return schemaDBApi.getDatabases()


@app.route("/collection")
def listCollections():
    return jsonify(schemaDBApi.getCollections(request.args.get('database'),request.args.get('servidor')))

@app.route("/database/<database>")
def getDatabase(database):
    return jsonify(schemaDBApi.getCollections(database,request.args.get('servidor')))