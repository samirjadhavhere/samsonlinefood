
from flask import *

from dbm import *

from dbm import deleterec

from dbm import displayrec


app=Flask(__name__) #app class & Flask(__name__) is an object.


@app.route("/") #method of flask class is route(decorator function under method)
@app.route("/home")
def home():
    return render_template("welcome.html") 

@app.route("/register")
def reg():
    return render_template("register.html")

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/details")
def details():
    #d=displayrec()
    return render_template("details.html")

@app.route("/edit")
def ed():
    edit_email=request.args.get("email1")
    info=sel(edit_email)
    return render_template("edit.html",elist=info)

@app.route("/delete")
def dele():
    em=request.args.get("email1")
    deleterec(em)
    return redirect("/details")

    

@app.route("/insert",methods=["post"])
def ins():
    
    name=request.form["uname"]
    email=request.form["email"]
    password=request.form["passw"]
    contact=request.form["con"]
    t=(name,email,password,contact)
    insertrec(t)
    return redirect("/")

@app.route("/log",methods=["post"])
def log():
    email1=request.form["email1"]
    password1=request.form["password1"]
    t=(email1,password1)
    print(t)
    t1=selectrec(email1)
    print(t1)
    elist=selectrec1(email1)
    print(elist)
    if t in t1:
        return render_template("details.html",elist=elist)
    else:
        return redirect("/login")



@app.route("/update",methods=["post"])
def up():
    name=request.form["uname"]
    email=request.form["email1"]
    password=request.form["passw"]
    contact=request.form["con"]
    t=(name,email,password,contact,email)
    updaterec(t)
    elist=displayrec()
    return render_template("login.html",elist=elist)

@app.route("/order")
def order():
    return render_template ("order.html")



if __name__=="__main__":
    app.run(debug=True) 