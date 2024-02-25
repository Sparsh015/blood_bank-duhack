from flask import Flask, render_template, request, redirect, url_for , jsonify
import mysql.connector

app = Flask(__name__)

# Configure MySQL database connection
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'mysql',
    'database': 'user_data',
    'autocommit': True  # Enable autocommit to automatically commit changes
}

# Function to get a database connection
def get_db_connection():
    return mysql.connector.connect(**db_config)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/need')
def need():
    return render_template('need.html')

@app.route('/submit', methods=['POST'])
def submit():
    # Retrieve form data
    name = request.form['name']
    age = int(request.form['age'])
    blood_group = request.form['blood_group']
    diseases = request.form['diseases']

    try:
        # Insert data into MySQL database
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO user_info (name, age, blood_group, diseases) VALUES (%s, %s, %s, %s)", (name, age, blood_group, diseases))
        cursor.close()
        conn.close()
        
        
        return redirect(url_for('index'))

    except mysql.connector.Error as e:
        return "An error occurred: {e}"

@app.route('/check_blood')
def check_blood():
    return render_template('check_blood.html')

@app.route('/check', methods=['POST'])
def check():
    # Retrieve form data
    name = request.form['name']
    age = int(request.form['age'])
    blood_group = request.form['blood_group']
    diseases = request.form['diseases']

    try:
        # Check if blood group is available in the database
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        
        cursor.execute("SELECT * FROM user_info WHERE blood_group = %s", (blood_group,))
        donor_info = cursor.fetchone()
        cursor.close()
        conn.close()

        if donor_info:
            # If donors are found, redirect to blood availability page
            return redirect(url_for('blood_availability', 
                                    name=name, 
                                    age=age, 
                                    blood_group=blood_group, 
                                    diseases=diseases))
        else:
            # If no donors are found, redirect back to index page or show a message
            return redirect(url_for('check_blood'))

    except mysql.connector.Error as e:
        return "An error occurred: {e}"


if __name__ == '__main__':
    app.run(debug = True)
