import cs50
import csv

from flask import Flask, jsonify, redirect, render_template, request

# Configure application
app = Flask(__name__)

# Reload templates when they are changed
app.config["TEMPLATES_AUTO_RELOAD"] = True


@app.after_request
def after_request(response):
    """Disable caching"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/", methods=["GET"])
def get_index():
    return redirect("/form")


@app.route("/form", methods=["GET"])
def get_form():
    return render_template("form.html")


@app.route("/form", methods=["POST"])
def post_form():
    name = request.form.get("name")
    surname = request.form.get("surname")
    email_address = request.form.get("email_address")
    phone_number = request.form.get("phone_number")
    if not name or not surname or not email_address or not phone_number:
        return render_template("error.html", message="Fill all the blanks!")

    with open("survey.csv", "r") as survey:
        reader = csv.reader(survey)
        data = list(reader)

        for _, _, _email_address, _phone_number in data:
            if email_address == _email_address and phone_number == _phone_number:
                return render_template("error.html", message="You are already registered!")

    with open("survey.csv", "a") as survey:
        writer = csv.writer(survey)
        writer.writerow((request.form.get("name"), request.form.get("surname"), request.form.get("email_address"), request.form.get("phone_number")))
        return redirect("/sheet")


@app.route("/sheet", methods=["GET"])
def get_sheet():
    with open("survey.csv", "r") as survey:
        reader = csv.reader(survey)
        data = enumerate(reader, 1)
        return render_template("sheet.html", data=data)