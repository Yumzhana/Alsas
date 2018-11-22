# работает с фласком, отвечает за функции фласка и вычисления
from flask import Flask, render_template as templateHTML

class Configuration():
    DEBUG = True

app = Flask(__name__)
app.config.from_object( Configuration )


