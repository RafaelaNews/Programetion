from flask import Flask

app = Flask("meu app")

posts = [
   {
     "titulo" : "Minha primeira postagem",
     "texto" : "teste"
   },
   {
      "titulo": "Minha segunda postagem",
      "texto": "outro teste"
   }
]
@app.route('/')
def exibir_entradas():
    entradas = posts #MOCK
    return render_template('exibirentradas.html')
