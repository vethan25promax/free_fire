from flask import Flask, request, render_template, redirect, url_for
import csv
import os
import re

app = Flask(__name__)

FILE_NAME = "students.csv"

# Card data
CARDS = [
    {"name": "Card 1", "image": "https://picsum.photos/seed/card1/200/150"},
    {"name": "Card 2", "image": "https://picsum.photos/seed/card2/200/150"},
    {"name": "Card 3", "image": "https://picsum.photos/seed/card3/200/150"},
    {"name": "Card 4", "image": "https://picsum.photos/seed/card4/200/150"},
    {"name": "Card 5", "image": "https://picsum.photos/seed/card5/200/150"}
]

# Create file with header if not exists
if not os.path.exists(FILE_NAME):
    with open(FILE_NAME, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Name", "Mobile Number", "Address", "Selected Card", "Section"])

def validate_mobile_number(mobile):
    """Validate mobile number (10 digits)"""
    return re.match(r'^[0-9]{10}$', mobile)

@app.route("/")
def home():
    return render_template("index.html", cards=CARDS)

@app.route("/select-section")
def select_section():
    card_name = request.args.get('card')
    if not card_name:
        return redirect(url_for('home'))
    return render_template("select_section.html", card_name=card_name)

@app.route("/form")
def form():
    card_name = request.args.get('card')
    section = request.args.get('section')
    if not card_name or not section:
        return redirect(url_for('home'))
    return render_template("form.html", card_name=card_name, section=section)

@app.route("/submit", methods=["POST"])
def submit():
    name = request.form["name"]
    mobile = request.form["mobile"]
    address = request.form["address"]
    card_name = request.form["card_name"]
    section = request.form["section"]
    
    # Basic validation
    if not name or not mobile or not address:
        return render_template("form.html", card_name=card_name, section=section, 
                             error="All fields are required")
    
    if not validate_mobile_number(mobile):
        return render_template("form.html", card_name=card_name, section=section, 
                             error="Please enter a valid 10-digit mobile number")

    # Save data into CSV
    with open(FILE_NAME, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([name, mobile, address, card_name, section])
    
    return render_template("success.html", name=name, card_name=card_name, section=section)

if __name__ == "__main__":
    app.run(debug=True)