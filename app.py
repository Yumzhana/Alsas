from flask import Flask, render_template

class Configuration():
    DEBUG = True

app = Flask(__name__)
app.config.from_object( Configuration )

def templateHTML( index ):
    return render_template( index )


