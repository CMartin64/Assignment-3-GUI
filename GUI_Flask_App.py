from flask import Flask, render_template, request, redirect, url_for
print('got here')
# def create_app():


bookDetails = {}
bookDetails['Title'] = 'Mr Smithsonian'
bookDetails['Author'] = 'Mrs Smithsonian'
bookDetails['Genre'] = 'Biographical'


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/', methods=['POST', 'GET'])
def upload_file():
    
        uploaded_file = request.files['file']
        if uploaded_file.filename != '':
            uploaded_file.save(uploaded_file.filename)
        return redirect(url_for('index'))


@app.route('/bookDetails')
def book_details():
    return render_template('book_details.html', bookDetails=bookDetails, image = 'static/pic_trulli.jpg')

if __name__ == '__main__':
    app.run(debug=True)
