from flask import render_template, Blueprint

accounting_blueprint = Blueprint('accounting', __name__, template_folder='templates')

@accounting_blueprint.route('/')
def index():
    return render_template('index.html')
