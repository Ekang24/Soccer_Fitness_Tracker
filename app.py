from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/add", methods=["GET", "POST"])
def add_workout():
    if request.method == "POST":
        date = request.form["date"]
        distance = request.form["distance"]
        time = request.form["time"]
        difficulty = request.form["difficulty"]
        notes = request.form["notes"]

        print(date)
        print(distance)
        print(time)
        print(difficulty)
        print(notes)

    return render_template("add_workout.html")

if __name__ == "__main__":
    app.run(debug=True)