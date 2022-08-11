import random

from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

##Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


##Cafe TABLE Configuration
class Cafe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    map_url = db.Column(db.String(500), nullable=False)
    img_url = db.Column(db.String(500), nullable=False)
    location = db.Column(db.String(250), nullable=False)
    seats = db.Column(db.String(250), nullable=False)
    has_toilet = db.Column(db.Boolean, nullable=False)
    has_wifi = db.Column(db.Boolean, nullable=False)
    has_sockets = db.Column(db.Boolean, nullable=False)
    can_take_calls = db.Column(db.Boolean, nullable=False)
    coffee_price = db.Column(db.String(250), nullable=True)


    def to_dict(self):
        dictionary={}
        for column in self.__table__.columns:
            # Create a new dictionary entry;
            # where the key is the name of the column
            # and the value is the value of the column
            dictionary[column.name]=getattr(self,column.name)
        return dictionary


@app.route("/")
def home():
    return render_template("index.html")
## HTTP GET - Read Record
#  Create a /random route in main.py that returns a random cafe.
@app.route("/random",methods=['GET'])
def get_random_cafe():
    row_count=Cafe.query.count()
    random_offset=random.randint(0,row_count-1)
    random_cafe=Cafe.query.offset(random_offset).first()
    return jsonify(cafe=random_cafe.to_dict())

@app.route("/all",methods=['GET'])
def get_all_cafes():
    cafes=Cafe.query.all()
    return jsonify(cafes=[cafe.to_dict() for cafe in cafes])

#Create a /search route to search for cafes at a particular location.
@app.route("/search",methods=['GET'])
def find_cafe():
    query_location=request.args.get('loc')
    cafes=Cafe.query.filter_by(location=query_location).all()
    if cafes:
        return jsonify(cafes=[cafe.to_dict() for cafe in cafes])
    return jsonify(error={"Not Found": "Sorry, we don't have a cafe at that location."})

## HTTP POST - Create Record

@app.route("/add",methods=['GET','POST'])
def add_cafe():
    api_key = request.args.get('api-key')
    if api_key == 'TOPSECRETapikey':
        new_cafe = Cafe(
            name=request.form.get("name"),
            map_url=request.form.get("map_url"),
            img_url=request.form.get("img_url"),
            location=request.form.get("loc"),
            has_sockets=bool(request.form.get("sockets")),
            has_toilet=bool(request.form.get("toilet")),
            has_wifi=bool(request.form.get("wifi")),
            can_take_calls=bool(request.form.get("calls")),
            seats=request.form.get("seats"),
            coffee_price=request.form.get("coffee_price"),
        )
        db.session.add(new_cafe)
        db.session.commit()
        return jsonify(response={"success": "Successfully added the new cafe."})
    else:
        return jsonify(error={"Forbidden": "Sorry, that's not allowed. Make sure you have the correct api_key."}), 403





## HTTP PUT/PATCH - Update Record

@app.route("/update-price/<cafe_id>",methods=['GET','PATCH'])
def price_update(cafe_id):
    new_price=request.args.get('new_price')
    cafe=Cafe.query.get(cafe_id)
    if cafe:
        cafe.coffee_price=new_price
        db.session.commit()
        return jsonify(response={"success": "Successfully updated the price."})
    else:
        return jsonify(error={"Not Found": "Sorry a cafe with that id was not found in the database."})

## HTTP DELETE - Delete Record
@app.route('/report-closed/<int:cafe_id>',methods=['GET','DELETE'])
def delete_cafe_report(cafe_id):
    api_key=request.args.get('api-key')
    if api_key == 'TOPSECRETapikey':
        cafe = Cafe.query.get(cafe_id)
        if cafe:
            db.session.delete(cafe)
            db.session.commit()
            return jsonify(response={"success": "Successfully deleted the cafe from the database."}), 200
        else:
            return jsonify(error={"Not Found": "Sorry a cafe with that id was not found in the database."}), 404
    else:
        return jsonify(error={"Forbidden": "Sorry, that's not allowed. Make sure you have the correct api_key."}), 403

if __name__ == '__main__':
    app.run(debug=True)
