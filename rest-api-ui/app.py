from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/find')
def find_password():
    return render_template('find_password.html')

@app.route('/discard')
def discard_member():
    return render_template('discard.html')

@app.route('/board_list')
def board_list():
    return render_template('board_list.html')

@app.route('/board')
def board_detail():
    return render_template('board.html')

@app.route('/board_edit')
def board_edit():
    return render_template('board_edit.html')

@app.route('/comment_edit')
def comment_edit():
    return render_template('comment_edit.html')


if __name__ == '__main__':
    app.run(debug=True)
