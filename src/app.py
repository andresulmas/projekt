from flask import Flask, render_template


__author__ = 'andres'


app = Flask(__name__)
app.config.from_object('src.config')
app.secret_key = "321"

@app.route("/")
def home():
    return render_template('home.html')


#if __name__ == "__main__":
#    app.run(host='0.0.0.0')

