# Sentiment Analysis Web Application

This is a simple web application built using Flask that performs sentiment analysis on user-entered text using TextBlob.

## Features
- Classifies text as Positive, Negative, or Neutral
- Displays Polarity score
- Displays Subjectivity score
- Simple and user-friendly interface

## Technologies Used
- Python
- Flask
- TextBlob
- HTML / CSS

## Installation Steps

1. Clone the repository:
https://github.com/komalsantoshmali/sentiment-analysis-flask.git

2. Navigate to the project folder:
cd sentiment-analysis-flask

3. Install required libraries:
pip install flask textblob

4. Download TextBlob corpora:
python -m textblob.download_corpora

5. Run the application:
python app.py

6. Open browser and visit:
http://127.0.0.1:5000

## Example
Input:
I love this project. It works perfectly.
Output:
- Sentiment: Positive
- Polarity: 0.5+
- Subjectivity: 0.6+

## Author
Komal Mali