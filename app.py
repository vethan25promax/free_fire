from flask import Flask, request, render_template
import csv
import os

app = Flask(__name__)

FILE_NAME = "students.csv"

# Create file with header if not exists
if not os.path.exists(FILE_NAME):
    with open(FILE_NAME, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Name", "Marks", "Register Number"])

@app.route("/")
def home():
    return render_template("form.html")

@app.route("/submit", methods=["POST"])
def submit():
    name = request.form["name"]
    marks = request.form["marks"]
    regno = request.form["regno"]

    # Save data into CSV
    with open(FILE_NAME, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([name, marks, regno])

    return f"""
    <h2>Data Saved Successfully!</h2>
    <p>Name: {name}</p>
    <p>Marks: {marks}</p>
    <p>Register No: {regno}</p>
    <br>
    <a href="/">Go Back</a>
    """

if __name__ == "__main__":
    app.run(debug=True)