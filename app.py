from flask import Flask
from flask import render_template

# Create a Flask instance
app = Flask(__name__)

# Define a route
@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/hello/<name>')
def hello(name):
    return render_template('home.html', name=name)

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
