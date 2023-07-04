from flask import Flask, request
from model.main import insertUsuario
from model.main import selectUser #import insertUsuario

app = Flask("MinhaAPI")

@app.route("/olamundo", methods = ["GET"])
def olaMundo():
    return {"ola": "mundo"}

@app.route("/users", methods = ["GET"])
def users():
    try:
        users = []
        users = selectUser()
        usersList = []

        for item in users:
            user = {}
            user["id"] = item.id
            user["nome"] = item.nome
            
            usersList.append(user)
            
        return geraResponse(200,"Sucesso", "Usuarios", usersList)
    
    except Exception as ex:
        return geraResponse(400, f"{ex}")

@app.route("/cadastra/usuario", methods =["POST"])
def cadastraUsuario():
    body = request.get_json()
    
    if("nome" not in body):
        return geraResponse(400, "Parametro nome não enviado" )
        # return{"status": 400,"mensagem": "Parametro nome não enviado"}

    usuario = insertUsuario(body["nome"], body["email"], body["senha"])

    return geraResponse(200, "Usuario criado", "user", usuario)

def geraResponse(status, mensagem, nome_do_conteudo=False, conteudo=False):
    response = {}
    response["status"] = status
    response["mensagem"] = mensagem

    if(nome_do_conteudo and conteudo):
        response[f"{nome_do_conteudo}"] = conteudo

    return response

app.run()