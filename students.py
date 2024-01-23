from flask import Flask,jsonify
from pymongo.mongo_client import MongoClient
import certifi

ca = certifi.where()

app = Flask(__name__)
@app.route("/")
def Greet():
    return "<p>Welcome to Student Management AP</p>"

@app.route("/students",methods=["GET"])
def get_all_student():
    try:
        client = MongoClient("mongodb+srv://Pawit:208902546@cluster0.bsumksw.mongodb.net/?retryWrites=true&w=majority", tlsCAFile=ca)
        client.admin.command('ping')
        print("Pinged your deployment. You successfully connected to MongoDB!")
        db = client["students"]
        collection = db["std_info"]
        all_student = list(collection.find())
        return jsonify(all_student)
    except Exception as e:
            print(e)
    finally:
        client.close()

if __name__=="__main__":
    app.run(host="0.0.0.0",port=5000,debug=True)
