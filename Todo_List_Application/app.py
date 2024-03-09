from flask import Flask, redirect, render_template, request
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
    


@app.route("/", methods =['Get', 'POST'])


def home():
    if request.method == 'POST':
        todo_title = request.form['title']
        desc_todo = request.form['desc']
        data = Todo(title = todo_title, desc = desc_todo)
        db.session.add(data)
        db.session.commit()
    alltodo = Todo.query.all()
    return render_template('index.html', alltodo = alltodo)

@app.route("/delete/<int:sno>")

def delete(sno):
   todo = Todo.query.filter_by(sno=sno).first()
   db.session.delete(todo)
   db.session.commit()
   return redirect("/")

@app.route("/update/<int:sno>", methods = ['GET', 'POST'])

def update(sno):
    if request.method == "POST":
        todo_title = request.form['title']
        desc_todo = request.form['desc']
        data = Todo.query.filter_by(sno = sno).first()
        data.title = todo_title
        data.desc = desc_todo
        db.session.add(data)
        db.session.commit()
        return redirect("/")
    todo = Todo.query.filter_by(sno=sno).first()
    return render_template('update.html',todo =todo)

if __name__ == "__main__":
    app.run(debug=False)