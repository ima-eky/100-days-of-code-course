from flask import Flask, render_template,request
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField,SelectField
from wtforms.validators import DataRequired,URL
import csv

# Creating a new flask application
app = Flask(__name__)
app.config['SECRET_KEY'] = 'ANY_SECRET_KEY_YOU_CHOOSE'
Bootstrap(app)

cofee_rating_choices=['☕','☕☕','☕☕☕','☕☕☕☕','☕☕☕☕☕','✘']
wifi_rating_choices=['💪','💪💪','💪💪💪','💪💪💪💪','💪💪💪💪💪','✘']
power_rating_choices=['🔌','🔌🔌','🔌🔌🔌','🔌🔌🔌🔌','🔌🔌🔌🔌🔌','✘']


# using WTForms to create a quick_form
#TODO
# add: Location URL, open time, closing time, coffee rating, wifi rating, power outlet rating fields
# make coffee/wifi/power a select element with choice of 0 to 5.
#e.g. You could use emojis ☕️/💪/✘/🔌
# make all fields required except submit
# use a validator to check that the URL field has a URL entered.
class CafeForm(FlaskForm):
    cafe = StringField(label='Cafe Name', validators=[DataRequired()])
    location_url=StringField(label='Cafe Location on Google Maps', validators=[DataRequired(),URL()])
    open_time= StringField(label='Opening Time e.g 9:30AM', validators=[DataRequired()])
    close_time= StringField(label='Closing Time e.g 4PM', validators=[DataRequired()])
    cofee_rating = SelectField(label='Coffee Rating', validators=[DataRequired()],choices=cofee_rating_choices)
    wifi = SelectField(label='Wifi Strength Rating' , validators=[DataRequired()],choices=wifi_rating_choices)
    power_outlet =SelectField(label='Power Socket Availability', validators=[DataRequired()],choices=power_rating_choices)
    submit = SubmitField(label='Submit')

# ---------------------------------------------------------------------------


# all Flask routes below
@app.route("/")
def home():
    return render_template("index.html")


@app.route('/add',methods=['GET','POST'])
def add_cafe():
    form = CafeForm()
    if request.method == 'POST':
        # TODO:
        # Make the form write a new row into cafe-data.csv
        # with   if form.validate_on_submit()
        if form.validate_on_submit():
            form_details=f"{form.cafe.data},{form.location_url.data},{form.open_time.data},{form.close_time.data},{form.cofee_rating.data},{form.wifi.data},{form.power_outlet.data}"
            with open('cafe-data.csv',"a", newline='', encoding="utf8") as csv_file:
                csv_file.write(f'\n{form_details}')


    return render_template('add.html', form=form)


@app.route('/cafes')
def cafes():
    with open('cafe-data.csv', newline='',encoding="utf8") as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        list_of_rows = []
        for row in csv_data:
            list_of_rows.append(row)
        print(list_of_rows)
    return render_template('cafes.html', cafes=list_of_rows)

if __name__ == '__main__':
    app.run(debug=True)
