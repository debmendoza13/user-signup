from flask import Flask, request, redirect, render_template
import cgi
import string

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/")
def index():
    return render_template("signup.hml")
    
    #signup_form.format(username="", name_error="", pw="", pw_error="", ver_pw="", ver_pw_err="", email="", em_err="")

@app.route("/", methods=["POST"])
def validate_form():
    
    username = request.form['username'] 
    pw = request.form['pw']
    ver_pw = request.form['ver_pw']
    email = request.form['email']

    name_error=""
    pw_error=""
    ver_pw_error = ""
    em_err = ""

    #Verify username
    for char in username:
        if char == " ":
            name_error = "No spaces allowed"
            break
        else:
            name_error = ""

    if username is None:
        name_error = "Please enter username"
        username = ""

    if len(username) < 3 or len(username) > 20:
        name_error = "Username length needs to be > 3 and < 20 "

    return render_template("signup.html", username=username, name_error=name_error, email=email, em_err=em_err)

    #Verify password
    if pw is None:
        pw_error = "Pleast enter password"
        pw = ""

    if " " in pw:
        pw_error = "No spaces in password"
        pw = ""
    else:
        pw_error = ""

    if len(pw) < 3 or len(pw) > 20:
        pw_error = "Password length must be > 3 and < 20 characters"
        pw = ""

    else: 
        return render_template("signup.html", username=username, name_error=name_error, pw_error=pw_error, ver_pw_error=ver_pw_error, email=email, em_err=em_err)

    #Verify verify-password
    if ver_pw != pw:
        ver_pw_error = "Passwords do not match" 
    else: 
        return render_template("signup.html", username=username, name_error=name_error, pw_error=pw_error, email=email, em_err=em_err)
    
    #Verify email
    if " " in email:
        em_err = "Please enter email"
    if "@" not in email:
        em_err = "Invalid email"
    if "." not in email:
        em_err = "Invalid email"
    if len(email) < 3 or len(email) > 20:
        em_err = "Email must be < 3 and < 20 characters"

    else:
        return render_template("signup.html", username=username, name_error=name_error, email=email, em_err=em_err)

    if not name_error and not pw_error and not ver_pw_error and not em_err:
        return redirect("/welcome-page", username=username)
    else: 
        return render_template("signup.html", username=username, name_error=name_error, pw_error=pw_error, email=email, em_err=em_err)
        
        #return signup_form.format(name_error=name_error, pw_error=pw_error, ver_pw_error=ver_pw_error, 
        #    em_err=em_err, username=uesrname, pw=pw, ver_pw=ver_pw, email=email)

app.run()
