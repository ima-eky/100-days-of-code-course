# Number Guessing Game (with flask)
- The number guessing game that we created in Day 12, but now with a real website. 
- A flask application where the home route displays information about the game and another route that can detect the number entered by the user 
- Each time you don't get the number you'll know, if your guess was too high or too low. 

### Prerequesites
- Install requirements `pip install -r requirements.txt`/ `pip install flask`

### How to run script/development server
- Navigate to project/day's directory
- export FLASK_APP=server.py (if you use windows,use set instead of export)
- To enable development features,export the FLASK_ENV environment variable and set it to development (export FLASK_ENV=development) before running the server.
- python3 server.py
- or flask run

### Output expected
<img src="https://github.com/ima-eky/100-days-of-code-course/blob/main/img/number_guessing_game.png" title="Sample image" />
<br><img src="https://github.com/ima-eky/100-days-of-code-course/blob/main/img/guess_the_number.jpg" title="Sample image" />
