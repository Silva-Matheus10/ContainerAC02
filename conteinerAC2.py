from flask import Flask

app = Flask(__name__)

@app.route("/")
def ra_aluno():
    return "Meu RA: 2201792"

app.run()