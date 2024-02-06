# Password Strength Classifier

This project implements a Password Strength Classifier using machine learning techniques to predict the strength of a given password. The model is trained on a dataset sourced from [Kaggle](https://www.kaggle.com/datasets/bhavikbb/password-strength-classifier-dataset).

## Project Structure

- **Password_Strength_Classifier.ipynb**: Jupyter Notebook containing the code for data exploration, model training, and saving the classifier and vectorizer.

- **index.html (templates folder)**: HTML file for the main page. It includes a form to input an email and password to check their strength.

- **result.html (templates folder)**: HTML file displaying the result of the password strength classification.

- **style.css (static folder)**: CSS file for styling the HTML pages.

- **app.py**: Flask web application script that loads the trained model and vectorizer to classify password strength. It includes routes for the main page, password classification, and returning to the main page.

## Getting Started

1. Clone this repository:

   ```bash
   git clone https://github.com/shehabziada130/Password-Strength-Classifier.git
   cd Password-Strength-Classifier
   ```

3. **Run the Flask application:**

    ```bash
    python app.py
    ```

    The application will be accessible at [http://127.0.0.1:5000/](http://127.0.0.1:5000/).

## Usage

1. Visit [http://127.0.0.1:5000/](http://127.0.0.1:5000/) in your web browser.

2. Enter an email and password to check their strength.

3. Click the "Check Password Strength" button to see the classification result.

## Additional Notes

- The Jupyter Notebook (`Password_Strength_Classifier.ipynb`) contains the code for data preprocessing, model training, and saving the model and vectorizer.

- The trained model (`xgb_classifier.joblib`) and vectorizer (`vectorizer.joblib`) are loaded in the Flask application (`app.py`).

- The web application uses Flask to provide a simple user interface for checking password strength.

- Styling is applied using the provided `style.css` file.

## Credits

- Dataset source: [Kaggle - Password Strength Classifier Dataset](https://www.kaggle.com/datasets/bhavikbb/password-strength-classifier-dataset)

- Libraries used: scikit-learn, xgboost, Flask
