from flask import Flask

app = Flask(__name__) # Create new flask instance

# Create a Flask route
@app.route('/')
def hello_world():
    return 'Hello world'