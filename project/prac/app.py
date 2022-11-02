from turtle import title
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/mypage')
def mypage():
    return 'this is my page'

@app.route('/test', methods=['GET'])
def test_get():
    title_recive = request.args.get('title_give')
    print(title_recive)
    return jsonify({
        'result': 'success',
        'msg': 'GET this request!'
    })

@app.route('/test', methods=['POST'])
def test_post():
    title_recive = request.form['title_give']
    print(title_recive)
    return jsonify({
        'result': 'success',
        'msg': 'POST this request!'
    })

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)