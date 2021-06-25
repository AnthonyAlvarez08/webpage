from flask import Flask, render_template, url_for
import os

app = Flask(__name__)

# define the port and host just incase I change it in the future, for now localhost 5000
HOST = '127.0.0.1'
PORT = 5000

pics = list()

for pic in os.listdir('./static/pics'):
    pics.append(pic) 


@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('home.html', title='pics', things=['this', 'is', 'a', 'rendered', 'list', 'hehe'], pics=pics)

@app.route('/hehe')
def hehe():
    return '<h1>hehe</h1>'

if __name__ == '__main__':
    app.run(host=HOST, port=PORT, debug=True)