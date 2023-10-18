from flask import (
    Blueprint, render_template
)

view_bp = Blueprint('View', __name__, url_prefix='/wheather')


@view_bp.route('/home', methods=['GET', 'POST'])
def index():
    return render_template('index.html')
