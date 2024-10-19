from flask import Flask, request, jsonify, render_template_string

app = Flask(__name__)

# Sample student data with DOB and place
students = [
{"id": "2015", "name": "Venkatesh", "age": 21, "current_residence": "USA", "DOB": "2003-09-17"},
    {"id": "2016", "name": "Jagadesh", "age": 20, "current_residence": "India", "DOB": "2004-04-19"},
    {"id": "2017", "name": "sai venkat", "age": 20, "current_residence": "colombia","DOB": "2005-05-01"},
    {"id": "2018", "name": "Rohan", "age": 22, "current_residence": "UK", "DOB": "2002-02-05"},
    {"id": "2019", "name": "Dhanush", "age": 19, "current_residence": "UA", "DOB": "1997-03-12"},
    {"id": "2020", "name": "Harish", "age": 23, "current_residence": "Australia", "DOB": "2001-11-22"}
]

@app.route('/')
def index():
    return render_template_string('''
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css">

    <title>Student Search</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f8f9fa;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            margin: 0;
        }
        .container {
            width: 100%;
            max-width: 600px;
        }
        .search-bar {
            position: relative;
            margin-bottom: 20px;
        }
        .search-input {
            width: calc(100% - 50px);
            padding: 10px 40px;
            font-size: 16px;
            border: 1px solid #ccc;
            border-radius: 4px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }
        .search-button {
            position: absolute;
            top: 50%;
            right: 10px;
            transform: translateY(-50%);
            background-color: transparent;
            border: none;
            font-size: 18px;
            cursor: pointer;
        }
        .error {
            color: red;
            font-size: 14px;
            margin-top: 10px;
        }
        .result {
            margin-top: 20px;
            background: #fff;
            padding: 20px;
            border-radius: 4px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }
        .stud {
            border-bottom: 1px solid #eee;
            padding: 10px 0;
        }
        .stud:last-child {
            border-bottom: none;
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="search-bar">
            <form id="searchForm">
                <input type="text" id="search" class="search-input" placeholder="Search by ID, Name, Age, Residence, DOB, or Place">
                <button type="button" class="search-button" onclick="searchStudent()"><i class="fa fa-search"></i></button>
            </form>
            <div id="error" class="error"></div>
        </div>
        <div id="result" class="result"></div>
    </div>
    <script>
        function searchStudent() {
            const searchTerm = document.getElementById('search').value.trim();
            const errorElement = document.getElementById('error');
            const resultElement = document.getElementById('result');
            errorElement.textContent = '';
            resultElement.innerHTML = '';

            if (!searchTerm) {
                errorElement.textContent = 'Please enter a search term.';
                return;
            }

            let query = '';
            if (!isNaN(searchTerm)) {
                query = `?id=${searchTerm}&age=${searchTerm}`;
            } else {
                query = `?name=${searchTerm}&current_residence=${searchTerm}&DOB=${searchTerm}&place=${searchTerm}`;
            }

            fetch(`/ssearch${query}`)
                .then(response => response.json())
                .then(data => {
                    let resultHtml = '';
                    if (data.length > 0) {
                        data.forEach(student => {
                            resultHtml += `
                                <div class="stud">
                                    <h1>ID: ${student.id}</h1>
                                    <h2>Name: ${student.name}</h2>
                                    <h3>Age: ${student.age}</h3>
                                    <h4>Current Residence: ${student.current_residence}</h4>
                                    <h5>DOB: ${student.DOB}</h5>
                                    <h6>Place: ${student.place}</h6>
                                </div>`;
                        });
                    } else {
                        resultHtml = '<p>No student found</p>';
                    }
                    resultElement.innerHTML = resultHtml;
                })
                .catch(error => {
                    console.error('Error:', error);
                    resultElement.innerHTML = '<p>Error occurred while fetching data</p>';
                });
        }
    </script>
</body>
</html>
''')

@app.route('/ssearch', methods=['GET'])
def ssearch():
    search_id = request.args.get('id')
    search_name = request.args.get('name')
    search_age = request.args.get('age')
    search_current_residence = request.args.get('current_residence')
    search_DOB = request.args.get('DOB')
    search_place = request.args.get('place')

    results = []
    for student in students:
        if (search_id and student['id'] == search_id) or \
           (search_name and student['name'].lower() == search_name.lower()) or \
           (search_age and student['age'] == int(search_age)) or \
           (search_current_residence and student['current_residence'].lower() == search_current_residence.lower()) or \
           (search_DOB and student['DOB'] == search_DOB):
            results.append(student)

    return jsonify(results)

if __name__ == '__main__':
    app.run(debug=True)
