from flask import Flask, render_template, redirect, url_for, request,flash

app = Flask(__name__)


@app.route('/', methods = ['GET', 'POST'])
def home():
    return render_template('index.html')

@app.route('/dashboard.html', methods = ['GET', 'POST'])
def dashboard():
    return render_template('dashboard.html')




# print("BEFORE")

if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000')

# print("AFTER")