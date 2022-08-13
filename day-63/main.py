from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError,StatementError


app = Flask(__name__)
#CREATE DATABASE
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///books.db"
db=SQLAlchemy(app)

#CREATE TABLE
class Books(db.Model):
    # __tablename__ ='persons'
    id=db.Column(db.Integer,primary_key=True)
    title=db.Column(db.String(250),nullable=False,unique=True)
    author= db.Column(db.String(250), nullable=False)
    rating=db.Column(db.Float,nullable=False)


db.create_all()
@app.route('/')
def home():
    ##READ ALL RECORDS
    all_books = db.session.query(Books).all()
    return render_template("index.html", books=all_books)


@app.route("/add",methods=["GET","POST"])
def add():
    values=request.values
    if request.method == 'POST':
        #CREATE RECORD
        new_book=Books(
                title=values['title'],
                author=values['author'],
                rating=values['rating']
        )
        try:
            db.session.add(new_book)
            db.session.commit()
            return redirect(url_for('home'))
        except IntegrityError:
            return render_template("add.html",exists=True)
        except StatementError:
            return render_template("add.html",wrong_input=True )

    return render_template('add.html')
@app.route("/edit", methods=["GET", "POST"])
def edit():
    if request.method == "POST":
        #UPDATE RECORD
        book_id = request.form["id"]
        book_to_update = Books.query.get(book_id)
        book_to_update.rating = request.values["rating"]
        db.session.commit()
        return redirect(url_for('home'))
    book_id = request.args.get('id')
    book_selected = Books.query.get(book_id)
    return render_template("edit_rating.html", book=book_selected)



@app.route("/delete")
def delete():
    book_id = request.args.get('id')

    # DELETE A RECORD BY ID
    book_to_delete = Books.query.get(book_id)
    db.session.delete(book_to_delete)
    db.session.commit()
    return redirect(url_for('home'))

if __name__ == "__main__":
    app.run(debug=True)

