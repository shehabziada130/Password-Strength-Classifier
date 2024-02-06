from flask import Flask, render_template, request, redirect, url_for
import joblib
    
app = Flask(__name__)

# Load the password strength classifier model
with open('xgb_classifier.joblib', 'rb') as model_file:
    password_model = joblib.load(model_file)

# Load the password vectorizer
with open('vectorizer.joblib', 'rb') as vectorizer_file:
    password_vectorizer = joblib.load(vectorizer_file)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/classify', methods=['POST'])
def classify_password():
    email = request.form['email']
    password = request.form['password']

    # Vectorize the password using the loaded vectorizer
    password_vector = password_vectorizer.transform([password])
    password_prediction = password_model.predict(password_vector)[0]

    # Map numerical prediction to strength levels
    if password_prediction == 2:
        password_strength = 'Strong'
    elif password_prediction == 1:
        password_strength = 'Normal'
    else:
        password_strength = 'Weak'

    return render_template('result.html', result=f'Password Strength: {password_strength}')

@app.route('/index')
def return_to_index():
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
