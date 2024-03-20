from flask import Flask, renderTemplate
dicionario ={

    app = Flask(__name__)

    @app.route("/personagem/<int:personagem_id>")
    def mostra_personagem(personagem_id):
    return renderTemplate('personagem.html',**dicionario[personagem_id])
    app.run(debut=True)
}