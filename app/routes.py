from flask import Blueprint, render_template, request, redirect, url_for
from .models import insert_record, init_db, get_connection
from .utils import export_to_excel

main = Blueprint('main', __name__)

@main.before_app_request
def initialize_database():
    init_db()

@main.route('/', methods=['GET', 'POST'])
def form(): 
    if request.method == 'POST':
        laptop = request.form['laptop']
        serial_number = request.form['serial_number']
        code = request.form['code']
        password = request.form['password']

        insert_record(laptop, serial_number, code, password_value)
        return redirect(url_for('main.form'))
    return render_template('form.html')

@main.route('/export')
def export():
    file_path = export_to_excel()
    return f"Log exported successfully to {file_path}"
