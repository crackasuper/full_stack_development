from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from sqlalchemy import Integer, String

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///todos.db"
db = SQLAlchemy(app)


class Todo(db.Model):
    sno = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(200), nullable = False)
    desc = db.Column(db.String(500), nullable = False)
    time = db.Column(db.DateTime, default = datetime.utcnow)

    def __repr__(self) -> str:
        return f"{self.sno} - {self.title}"
    


@app.route("/")

def home():
    alltodo = Todo.query.all()
    return render_template('index.html', alltodo = alltodo)

@app.route("/show")

def show_data():
    alltodo = Todo.query.all()
    print(alltodo)
    return "this will rturn data from database"


if __name__ == "__main__":
    app.run(debug=True)