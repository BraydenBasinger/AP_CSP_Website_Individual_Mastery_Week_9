




# i will continue this from IntelliJ





from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home(): 
    return render_template('home.html', project = "Individual Mastery Week 9" )

@app.route('/main')
def main():
  return render_template("main.html")

@app.route('/bio')
def bio():
  return render_template("bio.html")

if __name__ == "__main__":
    app.run(debug=True, port='3000', host='0.0.0.0')