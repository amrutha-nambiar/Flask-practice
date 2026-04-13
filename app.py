from flask import Flask, render_template

app = Flask(__name__)

@app.route('/profile')
def profile():
    return render_template('profile.html')

@app.route('/marks')
def marks():
    marks_data = {
        "Maths": 85,
        "Science": 90,
        "English": 78
    }
    return render_template('marks.html', marks=marks_data)

if __name__ == '__main__':
    app.run(debug=True)