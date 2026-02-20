from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def startseite():
    return render_template("index.html")

@app.route("/eintragen", methods=["GET", "POST"])
def eintragen():
    if request.method == "POST":
        item_name               =   request.form["item-name"]
        item_type               =   request.form["item-type"]
        item_quantity           =   request.form["item-quantity"]
        purchase_price_per_unit =   request.form["item-purchase-price-per-unit"]
        purchase_price_for_all  =   request.form["item-purchase-price-for-all"]

        return render_template("uebersicht.html")

if __name__ == "__main__":
    app.run(debug=True)