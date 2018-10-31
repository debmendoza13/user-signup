from flask import Flask, request, redirect, render_template
import cgi
import string

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/")
def index():
    return render_template("signup.html")
    
@app.route("/signup.html", methods=["POST"])
def validate_form():
    
    username = request.form['username'] 
    pw = request.form['password']
    ver_pw = request.form['verify']
    email = request.form['email']

    name_error = ""
    pw_error = ""
    ver_pw_error = ""
    em_err = ""

    #Verify username
    if username == "":
        name_error = "Please enter username"
        username = ""
        return render_template("signup.html", username=username, name_error=name_error)

    if len(username) < 3 or len(username) > 20:
        name_error = "Username must be between 3 and 20 characters"
        return render_template("signup.html", username=username, name_error=name_error)
    
    for char in username:
        if char == " ":
            name_error = "No spaces allowed"
            break
        else:
            name_error = ""
            continue
    else:
        name_error = ""

    #Verify password
    if pw == "":
        pw_error = "Please enter password"
        pw = ""
        return render_template("signup.html", username=username, name_error=name_error, pw_error=pw_error)
    
    if len(pw) < 3 or len(pw) > 20:
        pw_error = "Password must be between 3 and 20 characters"
        pw = ""
        return render_template("signup.html", username=username, name_error=name_error, pw_error=pw_error)

    if " " in pw:
        pw_error = "No spaces in password"
        pw = ""
        return render_template("signup.html", username=username, name_error=name_error, pw_error=pw_error)
    
    else:
        pw_error = ""

    #Verify verify-password
    if ver_pw != pw:
        ver_pw_error = "Passwords do not match" 
    else: 
        ver_pw_error = ""
    
    #Verify email
    if email == "":
        em_err = ""
        if not name_error and not pw_error and not ver_pw_error and not em_err:
            return render_template("welcome-page.html", username=username)

    else:
        if len(email) < 3 or len(email) > 20:
            em_err = "Email must be between 3 and 20 characters"
            return render_template("signup.html", username=username, name_error=name_error, pw_error=pw_error, ver_pw_error=ver_pw_error, email=email, em_err=em_err)
        if "@" not in email:
            em_err = "Invalid email"
            return render_template("signup.html", username=username, name_error=name_error, pw_error=pw_error, ver_pw_error=ver_pw_error, email=email, em_err=em_err)
        if "." not in email:
            em_err = "Invalid email"
            return render_template("signup.html", username=username, name_error=name_error, pw_error=pw_error, ver_pw_error=ver_pw_error, email=email, em_err=em_err)
    
    if not name_error and not pw_error and not ver_pw_error and not em_err:
        return render_template("welcome-page.html", username=username)
    else: 
        return render_template("signup.html", username=username, name_error=name_error, pw_error=pw_error, ver_pw_error=ver_pw_error, email=email, em_err=em_err)

app.run()
