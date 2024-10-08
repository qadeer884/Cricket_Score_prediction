from flask import Flask, render_template, request
import joblib

app = Flask(__name__)

# Load your pre-trained model
model = joblib.load('C:\\Skill\\self_learning\\Regressor_Cricket\\RF_regressor_cricket.pkl')  # Update this with the actual model filename

@app.route('/')
def index():
    return render_template('index.html', prediction_text='')

@app.route('/predict', methods=['POST'])
def predict():
    # Get inputs from the form
    powerPlay = int(request.form['powerPlay'])
    AverageScore = float(request.form['AverageScore'])
    delivery_left = int(request.form['delivery_left'])
    Score = int(request.form['Score'])
    CurrentRunRate = float(request.form['CurrentRunRate'])
    wicketsLeft = int(request.form['wicketsLeft'])
    Run_In_Last5 = int(request.form['Run_In_Last5'])
    Wickets_In_Last5 = int(request.form['Wickets_In_Last5'])
    innings = int(request.form['innings'])

    # Prepare input for prediction
    input_data = [[powerPlay, AverageScore, delivery_left, Score,CurrentRunRate,
                   wicketsLeft, Run_In_Last5, Wickets_In_Last5, innings]]

    # Make prediction
    prediction = model.predict(input_data)

    return render_template('index.html', prediction_text=f'Predicted Final Score: {prediction[0]}')

if __name__ == '__main__':
    app.run(debug=True)
