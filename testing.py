#this is my first devops testing project

from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello DevOps world_India"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)

