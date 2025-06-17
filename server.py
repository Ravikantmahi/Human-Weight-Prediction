from flask import Flask, render_template, request
import pandas as pd
from sklearn.linear_model import LinearRegression

app = Flask(__name__)

def load_data():
    # Load the CSV data
    df = pd.read_csv("weight-height.csv")

    # Convert 'Gender' to numeric (0 for Female, 1 for Male)
    df['Gender'] = df['Gender'].map({'Female': 0, 'Male': 1})

    return df

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Load the dataset
    df = load_data()

    # Get input values from the form
    gender = request.form.get('Gender')
    height = float(request.form.get('Height'))

    # Convert gender to numeric (1 for Male, 0 for Female)
    gender_numeric = 1 if gender == 'Male' else 0

    # Prepare the features for prediction
    X = df[['Height', 'Gender']]
    Y = df['Weight']

    # Train the linear regression model
    model = LinearRegression()
    model.fit(X, Y)

    # Make the prediction using the loaded model
    prediction = model.predict([[height, gender_numeric]])

    # Convert prediction from kg to hg (shift one decimal to the left)
    prediction_hg = prediction[0] / 10.0

    # Display the prediction result
    return render_template('result.html', prediction=prediction_hg)

if __name__ == '__main__':
    app.run(debug=True)
