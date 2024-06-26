from flask import Flask, render_template

app = Flask(__name__)


@app.route('/', methods = ['GET', 'POST'])
def home():
    return render_template('index.html')

@app.route('/dashboard.html', methods = ['GET', 'POST'])
def dashboard():
    return render_template('dashboard.html')

@app.route('/login.html', methods = ['GET', 'POST'])
def login():
    return render_template('login.html')

@app.route('/our_team.html', methods = ['GET', 'POST'])
def team():
    return render_template('our_team.html')

@app.route('/team_demo.html', methods = ['GET', 'POST'])
def team_demo():
    return render_template('team_demo.html')

@app.route('/software_director.html', methods = ['GET', 'POST'])
def software_director():
    return render_template('software_director.html')

@app.route('/incubator.html', methods = ['GET', 'POST'])
def incubator():
    return render_template('incubator.html')

@app.route('/president.html', methods = ['GET', 'POST'])
def president():
    return render_template('president.html')

@app.route('/vice_president.html', methods = ['GET', 'POST'])
def vice_president():
    return render_template('vice_president.html')

@app.route('/vice_president2.html', methods = ['GET', 'POST'])
def vice_president2():
    return render_template('vice_president2.html')

@app.route('/community_director.html', methods = ['GET', 'POST'])
def community_director():
    return render_template('community_director.html')

@app.route('/outreach_director.html', methods = ['GET', 'POST'])
def outreach_director():
    return render_template('outreach_director.html')

@app.route('/marketing_director.html', methods = ['GET', 'POST'])
def marketing_director():
    return render_template('marketing_director.html')

@app.route('/contact.html', methods = ['GET', 'POST'])
def contact():
    return render_template('contact.html')

@app.route('/job_board.html', methods = ['GET', 'POST'])
def job_board():
    return render_template('job_board.html')

@app.route('/more_info.html', methods = ['GET', 'POST'])
def more_info():
    return render_template('more_info.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000')


