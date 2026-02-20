from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///uebersicht.db'
app.config['SECRET_KEY'] = 'geheimer_schluessel'
db = SQLAlchemy(app)

class Uebersicht(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime)
    item_name = db.Column(db.String(100), nullable=False)
    item_type = db.Column(db.String(100), nullable=False)
    item_quantity = db.Column(db.Integer, nullable=False)
    purchase_price_per_unit = db.Column(db.Float, nullable=False)
    purchase_price_for_all = db.Column(db.Float, nullable=False)

@app.route("/")
def startseite():
    return render_template("index.html")

@app.route("/eintragen", methods=["GET", "POST"])
def eintragen():
    if request.method == "POST":
        neuer_eintrag = Uebersicht(
            date                    =   datetime.now(),
            item_name               =   request.form["item-name"],
            item_type               =   request.form["item-type"],
            item_quantity           =   request.form["item-quantity"],
            purchase_price_per_unit =   request.form["item-purchase-price-per-unit"],
            purchase_price_for_all  =   request.form["item-purchase-price-for-all"],
            )

        db.session.add(neuer_eintrag)
        db.session.commit()
        return redirect("/")
    return render_template("uebersicht.html")


with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run(debug=True)