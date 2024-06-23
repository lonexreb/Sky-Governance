from flask import Flask, render_template, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/signin', methods=['GET', 'POST'])
def signin():
    if request.method == 'POST':
        data = request.json
        email = data.get('email')
        password = data.get('password')
        
        # Here you would typically validate the email and password
        # For this example, we'll just print them and return a success message
        print(f"Received login attempt: Email: {email}, Password: {password}")
        
        # Add your validation logic here
        return jsonify(success=True, message="Login successful")
    
    return render_template("signin.html")

@app.route('/dashboard', methods=['GET', 'POST'])
def dashboard():
    return render_template("dashboard.html")


@app.route('/loading', methods=['GET', 'POST'])
def loading():
    return render_template("loading.html")

@app.route('/chat', methods=['GET', 'POST'])
def chat():
    return render_template("chat.html")

@app.route('/push', methods=['GET', 'POST'])
def push():
    return render_template("push.html")

@app.route('/result', methods=['GET', 'POST'])
def result():
    return render_template("result.html")



if __name__ == "__main__":
    app.run(debug=True)
