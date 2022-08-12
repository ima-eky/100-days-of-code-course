# My TOP 10 MOVIES WEBSITES
- A website that compiles your top 10 favourite movies of all time.As you watch more movies, you can always update the list and keep track of 
 movies to recommend people.
 - You should be able to view movie list items (from your database),edit a movie's rating and review,delete movies from the Database ,add new 
  movies via the add route and sort/rank movies by their ratings
 - You'll be dealing with WTForms,you can find help at [https://wtforms.readthedocs.io/en/2.3.x/](https://wtforms.readthedocs.io/en/2.3.x/) , 
 [https://pythonhosted.org/Flask-Bootstrap/forms.html](https://pythonhosted.org/Flask-Bootstrap/forms.html)
 -  [Here's](https://flask-sqlalchemy.palletsprojects.com/en/2.x/quickstart/#a-minimal-application) more documentation on SQLAchemy
 -  You will need to sign up for a free account on [The Movie Database](https://developers.themoviedb.org) (go to Settings -> API and get an API Key that you'll use in project),to be able 
 to make a request and search The Movie Database API for all the movies that match that title when adding new movies to database.
 - The Movie Database [Documentation](https://developers.themoviedb.org/3/search/search-movies) explains how to make a search query (try it out tab is 
 particularly useful)
 - To get a particular movie details >[https://developers.themoviedb.org/3/movies/get-movie-details](https://developers.themoviedb.org/3/movies/get-movie-details)

### Prerequesites
- Install requirements `pip install -r requirements.txt`

### How to run script/development server
- Navigate to project/day's directory
- export FLASK_APP=main.py (if you use windows,use set instead of export)
- To enable development features,export the FLASK_ENV environment variable and set it to development (export FLASK_ENV=development) before running the server.
- python3 main.py
- or flask run

### Output expected
