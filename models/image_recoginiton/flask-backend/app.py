from flask import Flask, request, jsonify # type: ignore

app = Flask(__name__)

# In-memory data storage (a list of dictionaries)
data_store = []

# GET method to retrieve all items
@app.route('/items', methods=['GET'])
def get_items():
    return jsonify("good to go"), 200

# POST method to create a new item
@app.route('/items', methods=['POST'])
def create_item():
    # Get the data from the request
    new_item = request.json
    # Add the new item to the data store
    data_store.append(new_item)
    return jsonify(new_item), 201

# PUT method to update an existing item by index
@app.route('/items/<int:item_id>', methods=['PUT'])
def update_item(item_id):
    # Check if the item exists
    if item_id < 0 or item_id >= len(data_store):
        return jsonify({'error': 'Item not found'}), 404

    # Get the updated data from the request
    updated_item = request.json
    # Update the item in the data store
    data_store[item_id] = updated_item
    return jsonify(updated_item), 200

if __name__ == '__main__':
    app.run(debug=True)
