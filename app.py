from flask import Flask, render_template, request
import joblib

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        review = request.form.get('review')  
        model = joblib.load('models/svc.pkl')
        prediction = model.predict([review])[0]
        if prediction == 1:
            prediction_label = "Positive Review"
        else:
            prediction_label = "Negative Review"
        return render_template("home.html", prediction=prediction_label)
    else:
        return render_template("home.html", prediction=None)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)