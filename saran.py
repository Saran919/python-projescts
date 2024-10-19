from flask import Flask, request, jsonify,render_template_string
import os

app = Flask(__name__)
@app.route('/home')
def form():
    with open(os.path.join(os.path.dirname(__file__),'saranpersonalform.html')) as f:
        return render_template_string(f.read())
    
@app.route('/home1', methods=['POST'])
def form1():
    with open(os.path.join(os.path.dirname(__file__),'test6.html')) as f:
        return render_template_string(f.read())

@app.route('/saransubmit', methods=['POST'])
def submit_form():
    print('reached the request')
    first_name = request.form.get('firstName')
    last_name = request.form.get('lastName')
    email = request.form.get('email')
    age = request.form.get('age')
    fruits = request.form.getlist('fruit')
    terms = request.form.get('terms')

    response = {
        'firstName': first_name,
        'lastName': last_name,
        'email': email,
        'age': age,
        'fruits': fruits,
        'terms': terms
    }

    response_list = [first_name,last_name,email,age,fruits,terms]

    return response_list, 200
    return jsonify(response), 200

if __name__ == '__main__':
    print('reached')
    app.run(debug=True)
