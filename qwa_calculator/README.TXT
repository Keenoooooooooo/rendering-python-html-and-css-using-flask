app.py

    Step 1: set up your python interpreter by using the commands on your terminal
        "python -m venv venv" --> a folder named 'venv' will appear within your project folder
        "ctrl+shift+p" --> this brings you to command palette, where you can choose your python interpreter
        enter you interpreter from this path: venv/Scripts/.... then choose your interpreter

    Step 2: once your interpreter is configured, install flask
        --> python -m pip install flask
        --> python -m pip install --upgrade flask
    
    Step 3: copy the following code:
"
from flask import Flask,render_template,url_for

app=Flask(__name__)
@app.route('/')

def main():
    return render_template('Grades (QWA) Calculator.html')
if __name__ == 'main':
    app.run(debug=True)
"


index.html

    Step 3: configure your html to integrate styling using css
