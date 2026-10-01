from flask import Flask, render_template, request
from utils.emi import calculate_emi, generate_schedule

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():

    result = None

    if request.method == "POST":

        principal = float(request.form["principal"])
        rate = float(request.form["rate"])
        years = int(request.form["years"])

        emi = calculate_emi(
            principal,
            rate,
            years
        )

        schedule_data = generate_schedule(
            principal,
            rate,
            years
        )
        result = {
            "principal": schedule_data["principal"],
            "emi": emi,
            "total_interest": schedule_data["total_interest"],
            "total_payment": schedule_data["total_payment"],
            "schedule": schedule_data["schedule"]
        }

    return render_template(
        "index.html",
        result=result
        
    )


if __name__ == "__main__":
    app.run(debug=True)