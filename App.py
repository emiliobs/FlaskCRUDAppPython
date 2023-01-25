from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = "Secrect Key"

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root@localhost/crud1'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


class Data(db.Model):
    Id = db.Column(db.Integer, primary_key=True)
    Name = db.Column(db.String(100))
    Email = db.Column(db.String(100))
    Phone = db.Column(db.String(100))

    def __init__(self, name, email, phone):
        self.Name = name
        self.Email = email
        self.Phone = phone


with app.app_context():
    db.create_all()


@app.route('/')
def Index():
  return render_template("index.html")


if __name__ == "__main__":
  app.run(debug=True)
