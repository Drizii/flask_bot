from flask import Flask, request, jsonify
import random, logging


response = ['I to jest fakt']

app = Flask(__name__)

@app.route('/bot', methods=['POST', 'GET'])
def bot():
    if request.method == 'POST':
        text = request.form.get('text')
        return jsonify(random.choice(response))

    return ''' <form method="POST">
                Witaj, co u Ciebie? <input type="text" name="witaj">
                <input type="submit" value="Wyslij"><br>
            </form>'''
@app.route('/form-example', methods=['GET', 'POST']) #allow both GET and POST requests
def form_example():
    if request.method == 'POST':  #this block is only entered when the form is submitted
        language = request.form.get('language')
        framework = request.form['framework']

        return '''<h1>The language value is: {}</h1>
                  <h1>The framework value is: {}</h1>'''.format(language, framework)

    return '''<form method="POST">
                  Language: <input type="text" name="language"><br> 
                  Framework: <input type="text" name="framework"><br>
                  <input type="submit" value="Submit"><br>
              </form>''' # to daje pola do wpisania wartości

if __name__ == "__main__":
    app.run(debug=True)


