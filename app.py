from flask import Flask, render_template, redirect


app = Flask(__name__)



@app.route('/') #Rota principal

def index():
    return render_template('index.html')


@app.route("/contatos")

def pagContatos():
    return render_template("contatos.html")

if __name__ == '__main__':
    app.run(debug=True)


