from flask import Blueprint, render_template, request, jsonify, redirect, url_for, session
from ..utils.pdf_handler import pdf_to_string
from ..utils.prompt import welcome_users, comments, revise, keywords

routes = Blueprint('routes', __name__)

@routes.route('/')
def index():
    return render_template('index.html')

@routes.route('/result')
def result():
    return render_template('result.html')

@routes.route('/jobmatch')
def jobmatch():
    return render_template('jobmatch.html')

@routes.route('/upload', methods=['POST'])
def upload_file():
    if 'pdf_file' not in request.files:
        return jsonify({"error": "No file part"}), 400
    
    file = request.files['pdf_file']
    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400
    
    if not file.filename.lower().endswith('.pdf'):
        return jsonify({"error": "File is not a PDF"}), 400
    
    # read the pdf file and save it to the session
    session['pdf_context'] = pdf_to_string(file)

    # redirect to the result page
    return redirect(url_for('routes.result'))

@routes.route('/prompt', methods=['POST'])
def prompt():
    action = request.form.get('action')
    pdf_text = session.get('pdf_context')
    if action == 'welcome':
        response = welcome_users(pdf_text)
    elif action == 'comments':
        response = comments(pdf_text)
    elif action == 'revise':
        response = revise(pdf_text)
    elif action == 'keywords':
        response = keywords(pdf_text)
    else:
        response = "Invalid action."

    return jsonify({"response": response})


