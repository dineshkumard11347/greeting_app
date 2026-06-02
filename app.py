from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        text = request.form.get('text', '').strip()
        if text.lower() == 'hi':
            message = 'Hello Dinesh Kumar'
        elif text:
            message = f'You entered: {text}'
        else:
            message = 'You entered: '
        return render_template('result.html', message=message)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)
