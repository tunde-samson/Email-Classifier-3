from flask import Flask, render_template
from form import myEmaillassifier
import joblib

app = Flask(__name__)
app.secret_key = 'Supersecret'

model = joblib.load("email_classifier_linear_model")
vectorizer = joblib.load("vectorizer_linear_model")

@app.route("/", methods=["GET", "POST"])
def index():
    form = myEmaillassifier()

    prediction = 0

    if form.validate_on_submit():
        email_text = form.email.data
        # Transform and predict
        X = vectorizer.transform([email_text])
        result = model.predict(X)[0]

        prediction = 'Spam' if result > 0.5 else 'Not Spam'

    return render_template("index.html", form=form, prediction=prediction)


if __name__ == '__main__':
    app.run(debug=True)


