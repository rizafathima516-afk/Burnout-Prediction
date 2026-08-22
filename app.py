from flask import Flask, render_template, request
import numpy as np
import pickle

app = Flask(__name__)

# Load Model and Scaler
model = pickle.load(open("dtc.pkl", "rb"))
scaler = pickle.load(open("Scaler.pkl", "rb"))

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/predictpage')
def predictpage():
    return render_template("predict.html")

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get Inputs
        work_hours = float(request.form['work_hours'])
        screen_time_hours = float(request.form['screen_time_hours'])
        meetings_count = float(request.form['meetings_count'])
        breaks_taken = float(request.form['breaks_taken'])
        after_hours_work = float(request.form['after_hours_work'])
        sleep_hours = float(request.form['sleep_hours'])
        task_completion_rate = float(request.form['task_completion_rate'])
        burnout_score = float(request.form['burnout_score'])

        day_type = request.form['day_type']

        if day_type == "Weekday":
            day_type_Weekday = 1
            day_type_Weekend = 0
        else:
            day_type_Weekday = 0
            day_type_Weekend = 1

        # Arrange features in correct order
        features = np.array([[
            work_hours,
            screen_time_hours,
            meetings_count,
            breaks_taken,
            after_hours_work,
            sleep_hours,
            task_completion_rate,
            burnout_score,
            day_type_Weekday,
            day_type_Weekend
        ]])

        # Scale Features
        features = scaler.transform(features)

        # Predict
        prediction = model.predict(features)[0]

        if prediction == 0:
            result = "Low Burnout Risk"
        elif prediction == 1:
            result = "Medium Burnout Risk"
        else:
            result = "High Burnout Risk"

        return render_template(
            "predict.html",
            prediction_text=f"Prediction: {result}"
        )

    except Exception as e:
        return render_template(
            "predict.html",
            prediction_text=f"Error: {e}"
        )

if __name__ == "__main__":
    app.run(debug=True)