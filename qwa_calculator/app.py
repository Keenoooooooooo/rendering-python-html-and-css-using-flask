from flask import Flask,render_template,url_for

app=Flask(__name__)
@app.route('/')

def main():
    return render_template('Grades (QWA) Calculator.html')
if __name__ == 'main':
    app.run(debug=True)
