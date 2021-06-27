from flask import Flask, render_template, url_for, redirect
from forms import CalculusForm
from calc import Polynomial
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'njvaovnfohandvfliansvdjf161f1bg64s1bs345fv1s6'

# define the port and host just incase I change it in the future, for now localhost 5000
HOST = '127.0.0.1'
PORT = 5000

pics = list()
results = dict()  # global for helping and doddo

for pic in os.listdir('./static/pics'):
    pics.append(pic) 


@app.route('/', methods=['GET', 'POST'])
@app.route('/home', methods=['GET', 'POST'])
def home():
    return render_template('home.html', title='pics', things=['this', 'is', 'a', 'rendered', 'list', 'hehe'], pics=pics)

@app.route('/hehe')
def hehe():
    return '<h1>hehe</h1>'


@app.route('/res', methods=['GET', 'POST'])
def res():
    global results
    temp = list()
    for i, b in results:
        temp.append(f'{i} : {str(b)}')
    return render_template('calcRes.html', title='res', results=temp)

@app.route('/calc', methods=['GET', 'POST'])
def calc():
    global results
    form = CalculusForm()
    print('here')
    if form.validate_on_submit():
        print('here3')
        poly = Polynomial(degree=form.degree.data, coefficients=list(map(int, form.coeffs.data.split())))
        results = {
            'evaluated at point' : enumerate([poly.eval(i) for i in range(11)]),
            'derivative/slope at point' : enumerate([poly.derivative(i) for i in range(11)]),
            'area under 0 to 10': poly.area_under(0, 10)

        }
        print(results)
        return redirect(url_for('res'))
    print('here2')
    return render_template('calc.html', title='calc', form=form)



if __name__ == '__main__':
    app.run(host=HOST, port=PORT, debug=True)