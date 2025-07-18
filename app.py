from flask import Flask, request, render_template
from datetime import datetime
from templates import *

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        name = request.form["name"]
        dob = request.form["dob"]  # format: YYYY-MM-DD

        try:
            birth_date = datetime.strptime(dob, "%Y-%m-%d")

            if birth_date.year < 1900:
                return render_template("index.html", error="DOB year must be after 1800", name=name)

            today = datetime(2025, 7, 8, 14, 2)  # Fixed date
            age_years = today.year - birth_date.year
            age_months = today.month - birth_date.month
            if today.day < birth_date.day:
                age_months -= 1
            if age_months < 0:
                age_years -= 1
                age_months += 12

            return render_template("index.html", name=name, age_years=age_years, age_months=age_months)

        except Exception as e:
            return render_template("index.html", error=f"Error in processing DOB: {e}")

    return render_template("index.html")


@app.route("/ping", methods=["GET"])
def ping():
    return "<p>Hey man! why are pinging me</p>"

@app.route("/aboutus", methods=["GET"])
def aboutus():
    return "<p>We are Mlops learners!</p>"

if __name__ == "__main__":
    app.run(debug=True)
