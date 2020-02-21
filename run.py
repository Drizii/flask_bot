from flask import Flask, request, render_template
import random


question = ['ktory jest glupi ', 'ktory jest z policji ', 'ktory pije kawe ', 'ktory je zupe', 'który śpi ', 'którego, gówno to obchodzi']
answer = ['dupa', 'gówno', 'nie interesuj sie', 'A zasadził ktoś, kiedyś panu kopa w dupę?', 'Jełopie, jeden zasrany', 'W tym kraju nie ma pracy dla ludzi z moim wykształceniem']

app = Flask(__name__)




@app.route('/a', methods=['POST', 'GET'])
def bot1():
    if request.method =="GET":
        return render_template("index.html")
    elif request.method =="POST":
        text = request.form["text"]
        y = (random.choice(question))
        xd = (random.choice(answer))
        success = text
        quest = "Jak nazywa sie " + text + " " + y + "?"
        ans = xd
        return render_template("index.html",
        questResponse = quest, ansResponse = ans if success else "Failed")


@app.route('/bot', methods=['POST', 'GET'])
def bot2():
    if request.method == 'POST':
        text = request.form.get('text')
        y = (random.choice(question))
        xd = (random.choice(answer))
        #return jsonify(random.choice(response))"
        return '''Jak nazywa się: {}, {} ? <br> <br>
                    {}'''.format(text, y, xd)


    return ''' <form method="POST"><br>
                Wpisz imie osoby o ktorej chcesz uslyszec zart <br>
                <input type="text" name="text"><br> <br>
                <input type="submit" value="Wyslij"><br></form>''' 


if __name__ == "__main__":
    app.run(debug=True, )