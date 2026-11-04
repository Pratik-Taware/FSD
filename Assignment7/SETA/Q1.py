from flask import Flask, request, jsonify

app = Flask(__name__)

# GET Method
@app.route('/student', methods=['GET'])
def student():
    return jsonify({
        "name": "Rahul",
        "course": "BSc IT"
    })


# POST Method
@app.route('/addstudent', methods=['POST'])
def addstudent():
    data = request.get_json(silent=True)

    if not data:
        return jsonify({"error": "Enter valid JSON data"}), 400

    name = data.get('name')
    course = data.get('course')

    if not name or not course:
        return jsonify({"error": "Enter name and course"}), 400

    return jsonify({
        "name": name,
        "course": course
    }), 200


if __name__ == '__main__':
    app.run(debug=True)
