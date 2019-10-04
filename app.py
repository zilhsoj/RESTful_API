from flask import Flask
# classes in pYthon is capitalized, library is lowercase for all

# first thing is to create a instance of Flask class, __name__ is to give each fiel a unique name
app = Flask(__name__)

# first to tell our app what request to understand
# inside route is the endpoint, '/' just means home, there has to be a method come after ddecorator

@app.route('/')
def home():
    # It can do things in this method, but whatever it does, it has to return something back to the browser
    return 'Hello world!'

# Also need to tell the app to start running
# specify a port in run()
app.run(port=5000)
