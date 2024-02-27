from flask import Flask, render_template, request
from datetime import datetime

app = Flask(__name__)

notes = []

@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == "POST":
        note = request.form.get("note")
        if note:
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            notes.append({"note": note, "timestamp": timestamp})
    return render_template("home.html", notes=notes)

if __name__ == '__main__':
    app.run(debug=True)
