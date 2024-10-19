from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Define available and selected items (you can store these in a database instead)
available_items = ["Item 1", "Item 2", "Item 3", "Item 4"]
selected_items = []

@app.route('/')
def index():
    return render_template('shift.html', available_items=available_items, selected_items=selected_items)

@app.route('/submit', methods=['POST'])
def submit():
    global available_items, selected_items
    selected_from_available = request.form.getlist('availableItems')
    selected_from_selected = request.form.getlist('selectedItems')

    # Move items from available to selected and vice versa
    selected_items.extend(selected_from_available)
    available_items = [item for item in available_items if item not in selected_from_available]

    available_items.extend(selected_from_selected)
    selected_items = [item for item in selected_items if item not in selected_from_selected]

    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
