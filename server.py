from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def hello():
    return render_template('temp2.html')

@app.route("/data")
def data():
		#put your code here
    return "12"



if __name__ == "__main__":
    app.run()