from flask import Flask, render_template, url_for
import os

app = Flask(__name__)

pics = list()

for pic in os.listdir('./static/pics'):
    pics.append(pic) # f'C:\\Users\\antho\\source\\repos\\web dev stuff\\webpage\\pics\\{pic}')


@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('home.html', title='pics', things=['this', 'is', 'a', 'rendered', 'list', 'hehe'], pics=pics)

@app.route('/hehe')
def hehe():
    return '<h1>hehe</h1>'

if __name__ == '__main__':
    app.run(debug=True)