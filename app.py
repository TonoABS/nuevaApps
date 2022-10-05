"""
[Aplicacion basica del microframework Flask de Python]
Author: Fortinux
Date: [05/10/2022]
"""

from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def home():
    #return "<H1>Hola Mundo!</H1>"
    return render_template("index.html")

@app.route("/servicios")
def servicios():
    #return "<H1>Esta es la página de servicios</H1>"
    return render_template("base.html")

@app.route("/contacto")
def contacto():
    #return "<H1>Esta es la página de contacto</H1>"
    return render_template("base.html")

@app.route("/admin")
def admin():
    #return "<H1>Esta es la página de admin</H1>"
    return render_template("base.html")

