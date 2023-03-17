from flask import Flask, render_template, request
import joblib

app = Flask(__name__)


# Load the trained model
model = joblib.load('college_rank_predictor.pkl')

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    tlr = float(request.form.get("tlr"))
    rpc = float(request.form.get("rpc"))
    go = float(request.form.get("go"))
    oi = float(request.form.get("oi"))
    perception = float(request.form.get("perception"))

    prediction = model.predict([[tlr, rpc, go, oi, perception]])
    prediction = prediction -1

    return render_template("index.html", prediction=int(prediction[0].round()))

if __name__ == "__main__":
    app.run(debug=True)
