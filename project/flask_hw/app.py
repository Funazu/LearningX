from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/info', methods=['GET'])
def info_get():
    info_recive = request.args.get('my_name')
    print(info_recive)
    return jsonify({
        'result': 'success',
        'msg': 'GET this request!'
    })

@app.route('/info', methods=['POST'])
def info_post():
    info_recive = request.form['my_name']
    print(info_recive)
    return jsonify({
        'result': 'success',
        'msg': 'POST this request!'
    })

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)