from flask import Flask
# classes in pYthon is capitalized, library is lowercase for all

# first thing is to create a instance of Flask class, __name__ is to give each file a unique name
app = Flask(__name__)

# first to tell our app what request to understand
# inside route is the endpoint, '/' just means home, there has to be a method come after ddecorator

@app.route('/')
def home():
    # It can do things in this method, but whatever it does, it has to return something back to the browser
    return 'Hello world!'

@app.route('/store', methods=['POST'])
def create_store():
    request_data = request.get_json()
    new_store = {
            'name': request_date['name']
            'items': []
    }
    stores.append(new_store)
    return jsonify(new_store)

@app.route('/store/<string:name>')
def get_store(name)
    # iterate over stores
    # if match, return the store
    # if no match, return an error message
    for store in store:
        if store['name'] == name:
            return jsonify(store)
        else:
            return jsonify({'message':'store not found'})


# Also need to tell the app to start running
# specify a port in run()
app.run(port=5000)
