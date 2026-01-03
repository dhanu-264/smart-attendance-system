from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

@app.route('/')
def index():
    try:
        df = pd.read_csv("output/attendance.csv")
        data = dict(zip(df.Name, df.Time))
    except FileNotFoundError:
        data = {}
    return render_template("index.html", data=data)

if __name__ == "__main__":
    app.run(debug=True)
