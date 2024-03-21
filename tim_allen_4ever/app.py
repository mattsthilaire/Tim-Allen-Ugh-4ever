from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    images = [f"tim-allen-{i}.jpeg" for i in range(1, 13)]
    return render_template("index.html", images=images)

if __name__ == "__main__":
    app.run(debug=True)