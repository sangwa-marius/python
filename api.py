from flask import Flask, jsonify,request

app = Flask(__name__)

@app.route("/")
def home():
    return "Welcome to my API!"


@app.route("/data")
def get_data():
    with open("data.jsonl","r") as f:
        data = f.read()
        return data
    
    
    
@app.route("/data/user/<name>")  
def get_user(name):
    return f"Hello {name}!"
    
@app.route("/send",methods=["POST"])
def receive_data():
    data = request.json
    return jsonify({
        "Message":"Your data has been received successfully",
        "ReceivedData":data
    })  
    
    
if __name__ == "__main__":
    app.run(debug=True)    
