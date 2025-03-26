# Emotion Detection Application

## Overview
This project is a comprehensive **emotion detection application** built using **Watson AI embedded libraries**. Unlike traditional sentiment analysis, which determines positive or negative sentiment, emotion detection identifies finer emotions such as **joy, sadness, anger, and more**. The application is then deployed as a web service using the **Flask framework**.

## Features
The project consists of the following key functionalities:

- **Emotion Detection with AI**: Utilizes Watson NLP to extract emotions beyond basic sentiment polarity.
- **Formatted Output**: Extracts and presents emotion-related insights in a structured format.
- **Packaged for Reusability**: The application is designed to be importable into other Python projects.
- **Unit Testing**: Runs comprehensive unit tests to validate the accuracy of the emotion detection algorithm.
- **Flask Deployment**: The application is hosted as a web service for easy accessibility.
- **Error Handling**: Implements structured error handling, ensuring appropriate responses for issues such as HTTP 500 errors.
- **Static Code Analysis**: Ensures compliance with **PEP8 guidelines** using static code analysis tools.

## Technologies Used
- **Watson NLP**
- **Flask**
- **Python**
- **Unit Testing (unittest/pytest)**
- **Static Code Analysis (flake8, pylint)**

## Installation & Usage
### Prerequisites
Ensure you have **Python 3.x** installed along with the necessary dependencies.

### Installation Steps
1. Clone this repository:
   ```sh
   git clone https://github.com/SanjayKMangrani/EmotionDetection.git
   cd your-repo
   ```
2. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```

### Running the Application
Start the Flask server:
```sh
python app.py
```
The application will be available at `http://localhost:5000/`.

### Running Tests
Execute unit tests:
```sh
pytest tests/
```

## Contribution Guidelines
If you’d like to contribute, feel free to fork this repository, make changes, and submit a pull request.
