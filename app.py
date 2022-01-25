
from flask import Flask,render_template, request

from openpyxl import load_workbook




app = Flask(__name__)

@app.route('/')
def homepage():
    f = load_workbook(r'C:\Users\kaku\Desktop\50kpython\murzakulova36\test.xlsx', read_only=True)
    sheet = f.active
    
    
    return render_template('index.html', sheet=sheet)



@app.route('/add/', methods=["POST"])
def add():
    good = request.form["good"]
    f = open('test.xlsx', 'a+', encoding='utf-8')
    f.write(good + "\n")
    f.close()
    return """
        <h1>Инвертарь пополнен</h1>
        <a href='/'>Домой</a>
    """

 

