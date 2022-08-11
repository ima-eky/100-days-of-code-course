from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError,StatementError
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import requests


MOVIE_DB_SEARCH_URL='YOUR OWN API KEY(GET YOUR API KEY FROM themoviedb.org)'
MOVIE_DB_API_KEY="3bd287dd8c5c814b78fe645a8b11c582"


app = Flask(__name__)
# CREATE DATABASES
app.config['SECRET_KEY'] = 'ANY SECRET KEY YOU CHOOSE'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///movies.db"

#Initialise Bootstrap on app
Bootstrap(app)

#Connect db to app
db=SQLAlchemy(app)


#CREATE TABLE
class Movie(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    title=db.Column(db.String,unique=True,nullable=False)
    year=db.Column(db.Integer)
    description =db.Column(db.String,unique=True)
    rating=db.Column(db.Float,nullable=True)
    ranking=db.Column(db.Integer,nullable=True)
    review=db.Column(db.String,nullable=True)
    img_url=db.Column(db.String)
db.create_all()

# Uses WTForms to create a quick_form
class RateMovieForm(FlaskForm):
    new_rating=StringField(label="Your rating out of 10 e.g 4.5")
    new_review=StringField(label="Your Review")
    done_button=SubmitField(label="Done")

class AddMovie(FlaskForm):
    new_movie=StringField(label="Movie Title",validators=[DataRequired()])
    submit = SubmitField("Add Movie")

@app.route("/")
def home():
    ##READ ALL RECORDS
    # This line creates a list of all the movies sorted by rating
    all_movies = Movie.query.order_by(Movie.rating).all()
    # This line loops through all the movies
    for i in range(len(all_movies)):
        # This line gives each movie a new ranking reversed from their order in all_movies
        all_movies[i].ranking = len(all_movies) - i
    db.session.commit()
    return render_template("index.html", movies=all_movies)

@app.route("/add",methods=['GET','POST'])
def add():
    form=AddMovie()
    #Calls this function after form has been validated on submission
    if form.validate_on_submit():
        movie_title=form.new_movie.data
        response = requests.get(MOVIE_DB_SEARCH_URL, params={"api_key": MOVIE_DB_API_KEY, "query": movie_title})
        data = response.json()["results"]
        return render_template("select.html", options=data)
    return render_template('add.html',form=form,)

@app.route("/edit",methods=['GET','POST'])
def edit_rating():
    new_form=RateMovieForm()
    movie_id = request.args.get('id')
    movie_selected = Movie.query.get(movie_id)
    if new_form.validate_on_submit():
        #Edits already existing record
        movie_selected.rating=float(new_form.new_rating.data)
        movie_selected.review=new_form.new_review.data
        db.session.commit()
        return redirect(url_for("home"))
    return render_template('edit.html',form=new_form,movie=movie_selected)
@app.route("/delete",methods=['GET','POST'])
def delete_rating():
    #Deletes selected  record
    movie_id = request.args.get('id')
    movie= Movie.query.get(movie_id)
    db.session.delete(movie)
    db.session.delete(movie)
    db.session.delete(movie)
    db.session.commit()
    return redirect(url_for('home'))

@app.route("/find")
def find_movie():
    movie_api_id=request.args.get('id')
    movie_details=Movie.query.get(movie_api_id)
    if movie_api_id:
        movie_api_url=f"https://api.themoviedb.org/3/movie/{movie_api_id}"
        response=requests.get(movie_api_url,params={"api_key": MOVIE_DB_API_KEY })
        data=response.json()
        new_movie = Movie(
            title=data["title"],
            # The data in release_date includes month and day, we will want to get rid of.
            year=data["release_date"].split("-")[0],
            img_url=f"https://image.tmdb.org/t/p/w500{data['poster_path']}",
            description=data["overview"]
        )
        db.session.add(new_movie)
        db.session.commit()
        return redirect(url_for("edit_rating",id=new_movie.id))
    else:
        return "Movie not found"

if __name__ == '__main__':
    app.run(debug=True)
