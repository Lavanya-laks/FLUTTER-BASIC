from flask import Flask, jsonify, request

app = Flask(__name__)

app.route('/')
def home():
    return "Home page"

@app.patch('/pat/<inputId>')
def patchmethod(inputId):
    data = request.get_json()
    users = data

    if inputId in users.values():
        users["Id"] = 1000
        print(f"users data is {users}")
        res = "Data updated"
        return res
    
    print(f"The data after creation is {users}")
    res = "Data created"

app.run(debug=True)
