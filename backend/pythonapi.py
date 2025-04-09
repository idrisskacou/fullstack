from flask import Flask, jsonify, request

app = Flask(__name__)

# Sample data
items = [
    {"id": 1, "first_name": "Test 1","last_name": "" ,"gender": "M", "age": "21" ,"description": "This is item 1"},
    {"id": 2, "first_name": "Test 2","last_name": "" ,"gender": "F", "age": "25" ,"description": "This is item 2"},
    {"id": 3, "first_name": "Test 3","last_name": "" ,"gender": "M", "age": "24" ,"description": "This is item 3"},
    {"id": 4, "first_name": "Test 4","last_name": "" ,"gender": "F", "age": "35" ,"description": "This is item 4"},
    {"id": 5, "first_name": "Test 5","last_name": "" ,"gender": "M", "age": "50" ,"description": "This is item 5"},

]

# Get all items
@app.route('/items', methods=['GET'])
def get_items():
    return jsonify(items)

# Get a single item by ID
@app.route('/items/<int:item_id>', methods=['GET'])
def get_item(item_id):
    item = next((item for item in items if item["id"] == item_id), None)
    if item:
        return jsonify(item)
    return jsonify({"error": "Item not found"}), 404

# Create a new item
@app.route('/items', methods=['POST'])
def create_item():
    data = request.json
    new_item = {
        "id": len(items) + 1,
        "name": data.get("name"),
        "description": data.get("description")
    }
    items.append(new_item)
    return jsonify(new_item), 201

# Delete an item by ID
@app.route('/items/<int:item_id>', methods=['DELETE'])
def delete_item(item_id):
    global items
    items = [item for item in items if item["id"] != item_id]
    return jsonify({"message": "Item deleted"}), 200

# Run the app
if __name__ == '__main__':
    app.run(debug=True)

