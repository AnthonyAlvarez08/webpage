from flask import Flask, render_template, url_for, redirect
from forms import CalculusForm
from calc import Polynomial
from math import sqrt
import asyncio
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'e3dee6884570b0508514c1daac10d355ab27d92b66ad4df4da3b7e36b5c6ffed31522c4f88bbea305d3262c72c2de0d56f2b421c995202ef3ccb283858dda61b'

# define the port and host just incase I change it in the future, for now localhost 5000
HOST = '127.0.0.1'
PORT = 5000

# to hold the picture names for now until I figure out databases
pics = list()

# get all the picture names in the list
for pic in os.listdir('./static/pics'):
    pics.append(pic) 


# I have decided to learn asyncio
async def oof():
    print('hehe')
    await asyncio.sleep(0.2)

def generate_nums() -> list[int]:
    return list(filter(lambda x: int(sqrt(x)) == sqrt(x), range(1, 1_000_000)))


@app.route('/', methods=['GET', 'POST'])
@app.route('/home', methods=['GET', 'POST'])
def home() -> str:
    return render_template('home.html', title='pics', things=['this', 'is', 'a', 'rendered', 'list', 'hehe'], pics=pics)

@app.route('/calc', methods=['GET', 'POST'])
def calc() -> str:
    results = None
    form = CalculusForm()
    # if have recieved user input then display it on the page
    if form.is_submitted():
        poly = Polynomial(degree=form.degree.data, coefficients=list(map(int, form.coeffs.data.split())))
        results = [
            f'f(x) = {str(poly)}',
            f'evaluated at point: { {i : poly.eval(i) for i in range(11)} }',
            f'derivative/slope at point: { {i : poly.derivative(i) for i in range(11)} }',
            f'area under 0 to 10: {poly.area_under(0, 10)}'
        ]
    return render_template('calc.html', title='calc', form=form, results=results)



@app.route('/other')
def other() -> str:
    nums = generate_nums()
    return render_template('other.html', nums=nums)


@app.route('/about-me')
def about() -> str:
    return render_template('about.html')


if __name__ == '__main__':
    app.run(host=HOST, port=PORT, debug=True)