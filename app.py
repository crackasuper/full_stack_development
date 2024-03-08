from flask import Flask

app = Flask(__name__)

@app.route("/")

def home():
    message = "<h1> Dude what is going on</h1> <p> first flask home page</P"
    return message

@app.route("/welcome/<name>")
def welcome_name(name):
    return "Welcome " + name+'!'
if __name__ == "__main__":
    app.run(debug = True)