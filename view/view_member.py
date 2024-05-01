from app import app



@app.route('/login')
def login():
    return 'login_member'

@app.route('/join')
def join():
    return 'join_member'

@app.route('/findpw')
def findpw():
    return 'find_member_password'

@app.route('/edit')
def editinfo():
    return 'edit_member_info'

@app.route('/discard')
def discard():
    return 'discard_member_info'