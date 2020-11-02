from flask import Flask, redirect, url_for, render_template, request
# instance of flask
app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def home():
        return render_template('index.html')


# @app.route('/login', methods=['POST', 'GET'])
# def login():

@app.route('/demo', methods=['POST', 'GET'])
def demo():
    if request.method == 'POST':
        submit_value = request.form['subb']
        # print(submit_value)
        if submit_value == 'submit':
            text_value = request.form['txt']
            # return 'HI'
            return render_template('demo.html', text=text_value)
        else:
            return redirect('/')
    else:
        return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
