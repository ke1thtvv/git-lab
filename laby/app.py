from flask import Flask, request, render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/method', methods=['GET', 'POST'])
def method():
    if request.method == 'POST':
        return 'Użyto metody POST'
    else:
        return 'Użyto metody GET. '
    
@app.route('/ok/<number>')
def count(number):
    number = int(number)
    answer = ''
    if (number % 2 == 0):
        answer += 'dzieli przez 2'
    elif (number % 2 == 0):
        answer += 'dzieli przez 3'
    else:
        answer += 'n dzieli sie'
    return answer

@app.route('/about/<name>/<number>')
def hello(name, number):
    return render_template('about.html', name=name, age=number)

if __name__ == "__main__":
    with app.app_context():
        app.run(debug=True)