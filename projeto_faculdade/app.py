from flask import Flask, request, jsonify, render_template, json, redirect, url_for
from main import  ler_dados, atualizar_nota, criar_novo_usuario_e_nota, deletar_usuario, login_de_usuario, matricular_aluno
from tabelas import Usuario, Nota

app = Flask(__name__)

@app.route("/", methods=['GET','POST'])
def index():

    if request.method=='GET':

        return render_template('index.html')
    
    elif request.method=='POST':

        data=request.get_data()

        usuario_e_nota = json.loads(data)

        user = Usuario(

            nome=usuario_e_nota["usuario"],
            email=usuario_e_nota["email"],
            senha_hash=usuario_e_nota["senha"]
        )

        note = Nota(

            titulo=usuario_e_nota["titulo"],
            conteudo = usuario_e_nota["nota"]    
        )

        app.logger.info("usuario está criando nota e usuario associado ")


        criar_novo_usuario_e_nota(user, note)

        return jsonify({"message": "Usuário e nota criados com sucesso!"}), 201
    else:

        return jsonify({'error': 'pagina não encontrada'}), 404   

@app.route("/api/users", methods=["GET"])
def api_users():

    try:
        data = ler_dados()

        return jsonify({"success": True, "data": data}),  200
    
    except Exception as e:

        return jsonify({"success": False, "error": str(e)}), 500
    
@app.route("/home", methods={"GET"})
def home():
    return render_template("home.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        data = request.get_data()
        usuario = json.loads(data)
        user = Usuario(email=usuario["email"], senha_hash=usuario["senha_hash"])

        try:
            usr= login_de_usuario(user)
            app.logger.info("Usuário de email %s  logado" % usuario["email"])
            return  redirect(url_for("home", data=usr))

        except Exception as e:
            app.logger.error("Erro no servidor: ", str(e))
            return jsonify({"success": False, "error": str(e)}), 500
    else:
        return render_template('login.html')
    


@app.route("/remover/usuarios/<int:id_usuario>", methods=['GET', 'POST'])
def remover_usuario(id_usuario):
    if request.method == "POST":
        try:
            deletar_usuario(id_usuario=id_usuario)
            app.logger.info(f"Usuário do id: {id_usuario} foi removido com sucesso")
            return redirect(url_for("index"))
        except Exception as e:
            app.logger.error(f"Erro na remoção do usuário: {str(e)}")
            return jsonify({"success": False, "error": str(e)}), 500
    else:
        # Aqui, você pode buscar o usuário específico para mostrar na confirmação, se quiser:
        usuarios = ler_dados()
        usuario = next((u for u in usuarios if u['id'] == id_usuario), None)
        return render_template('remove.html', usuario=usuario)

    

@app.route("/usuarios")
def usuarios():
    try:
        data = ler_dados()
        return render_template("users.html", usuarios=data)
    except Exception as e:
        return render_template("users.html", usuarios=[], error=str(e))

@app.route("/matricula/<id_usuario>/<id_curso>", methods=['GET', 'POST'])
def matricula(id_usuario, id_curso):
    print(id_usuario, id_curso)
    if request.method=='POST':
        try:
            matricular_aluno(id_usuario, id_curso)
            app.logger.info("Usuario do id %d foi matriculado" % int(id_usuario))
            return redirect(url_for('home'))
        except Exception as e:
            app.logger.error("Erro ao matricular usuario", str(e))
            return jsonify({"sucess": False, "error": str(e)}), 500
        
    else:
        return render_template('matricula.html', id_usuario=id_usuario, id_curso=id_curso)


if __name__=="__main__":

    app.run()