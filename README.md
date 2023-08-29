# Doctor's Fee Prediction using Machine Learning

Predicting the consultation fees of doctors using a linear regression model based on location, degree, and years of experience. The project deploys the machine learning model using Flask, along with a user-friendly HTML interface for easy fee predictions.

## Table of Contents

- [Introduction](#introduction)
- [Project Components](#project-components)
- [Usage](#usage)
- [Setup](#setup)
- [Dependencies](#dependencies)
- [Data Collection](#data-collection)
- [Contributing](#contributing)
- [License](#license)

## Introduction

This project focuses on predicting the consultation fees of doctors using a linear regression machine learning model. By considering factors such as the doctor's location, degree, and years of experience, the model provides accurate fee estimates. The project further enhances user accessibility by deploying the model using Flask and creating a simple HTML interface for convenient fee predictions.

## Project Components

1. **Data Collection and Preprocessing**: The project begins with data collection using web scraping techniques. The data is collected from the Practo website for doctors in Mumbai, Bangalore, and Delhi. Beautiful Soup is used for scraping the data, which includes information about doctors' locations, degrees, years of experience, and their corresponding consultation fees. The dataset is preprocessed to handle missing values, encode categorical variables, and optimize it for training.

2. **Model Development**: A linear regression model is selected as the predictive tool. The model is trained using the preprocessed dataset and is tuned to achieve the best possible performance.

3. **Deployment with Flask**: To make the model accessible and usable, it is integrated into a Flask web application. This integration enables users to input the doctor's location, degree, and years of experience through a user-friendly interface.

4. **Web Interface**: A basic HTML interface is developed to facilitate interaction with the model. Users can input relevant details, and upon submitting the information, they receive an immediate prediction of the consultation fee.

## Usage

1. Begin by cloning or downloading this repository to your local machine.

2. Install the required dependencies (see [Dependencies](#dependencies)).

3. Navigate to the project directory and run the Flask app using the following command:

4. Access the web interface by opening a web browser and visiting the provided address (usually `http://127.0.0.1:5000`).

5. On the web interface, enter the doctor's location, degree, and years of experience into the designated fields.

6. Click the "Predict" button to initiate the prediction process. The predicted consultation fee will be displayed on the webpage.

## Setup

1. Create a virtual environment (recommended) and activate it.

2. Install the necessary packages using the following command:

## Dependencies

- Flask
- Scikit-learn
- Pandas
- Numpy
- Beautiful Soup (for data scraping)


## License

This project is licensed under the [MIT License](LICENSE).
