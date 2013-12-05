from flask import Flask, render_template

# Setup application
app = Flask(__name__)

app.debug = True
app.config.from_pyfile('config/app.py')

@app.route("/")
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run()
