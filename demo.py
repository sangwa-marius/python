import json
from datetime import datetime 
from flask import Flask, jsonify, request

app = Flask(__name__)

File = "data.jsonl"

@app.route("/send", methods =['POST'])
def send_message():
    data = request.json
    message ={
        "sender":data.get('name'),
        "text":data.get('text'),
        "time":datetime.now().strftime("%Y-%m-%d %H:%Mz:%S")  
    }
    
    with open(File ,"a") as f:
        f.write(json.dumps(message)+"\n")
    
    return jsonify({
        "success":True,
        "message":message
    })
    
    
@app.route("/get_messages", methods=['GET'])  
def get_all_messages():
    messages =[]
    
    try:
        with open(File, "r")as f:
            for line in f:
                try:
                    messages.append(json.loads(line))  
                except:
                    pass
    except FileNotFoundError:
        pass   
    
    return jsonify(messages)                 
        
        
        

if __name__ =="__main__"   :
    app.run(debug=True)     