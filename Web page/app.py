# Import necessary libraries
from flask import Flask, render_template, request
import pickle
import numpy as np

# Load the trained machine learning model from a pickle file
model = pickle.load(open('mlpro.pkl', 'rb'))

# Create a Flask web application instance
app = Flask(__name__)

# Define a route for the root URL '/'
@app.route('/')
def man():
    # Render the HTML template 'indextest.html'
    return render_template('indextest.html')

# Define a route for handling form submission at '/predict'
@app.route('/predict', methods=['POST'])
def home():
    # Retrieve form data submitted via POST request
    speciality_of_doctor = request.form['speciality_of_doctor']
    degree_type = request.form['degree_type']
    year_of_experianc = request.form['year_of_experianc']
    city = request.form['city']
    location = request.form['location']
    dp_score = request.form['dp_score']
    npv = request.form['npv']

    # Create a numpy array with the form data
    arr = np.array([[speciality_of_doctor, degree_type, year_of_experianc, city, location, dp_score, npv]])

    # Make a prediction using the loaded machine learning model
    pred = model.predict(arr)

    # Render the HTML template 'indextest.html' with the prediction result
    return render_template('indextest.html', data=pred)

# Run the Flask app when this script is executed
if __name__ == "__main__":
    app.run(debug=True)
