from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/via_postman')
def hello():
    i = "Welcome\n\n"
    return i

@app.route('/add')
def add():
    num1 = request.args.get('val1')
    num2 = request.args.get('val2')
    ans = int(num1) + int(num2)
    return "<h1>sum is {}</h1>".format(str(ans))


@app.route('/reverse')
def reverse():
    data = request.args.get('value')

    return data[::-1]
    
    

if __name__ == '__main__':
    app.run()

