from flask import Flask, render_template, request, redirect, url_for, session
import hashlib
import csv
import os

app=Flask(__name__)

app.secret_key=os.urandom(32)

@app.route("/")
def a():
    return render_template("home.html", x="")


@app.route("/auth", methods=['POST'])
def b():
    #fd=open('data/up.csv','a')
    #row="fklsd,hfsdjkfh"
    #fd.write(row)
    #fd.close
    #print "\n\n\n"
    #print "diagnostic"
    #print app
    #print "request"
    #print request.headers
    #print request.method
    #print request.args
    print request.form
    #print "url"
    #print url_for("js")
    if "username" in request.form:
        un=request.form["username"]
        pw=request.form["password"]
    lr=request.form["lorr"]
    #if un=="homer" and pw=="simpson":
        #return render_template("result.html", yesno="success")
    #return render_template("result.html", yesno="failure")

    if lr=="register":
        #register
        c=open("data/up.csv")
        combos=csv.reader(c)
        for i in combos:
            if un==i[0]:
                return render_template("home.html", x="username already registered")
        mho=hashlib.sha1()
        mho.update(pw)
        c.close()
        fd=open('data/up.csv','a')
        row=un+","+mho.hexdigest()
        fd.write(row)
        fd.close()
        return render_template("home.html", x="account created")
    if lr=="login":
        #login
        combos=csv.reader(open("data/up.csv"))
        for i in combos:
            if un==i[0]:
                mho=hashlib.sha1()
                mho.update(pw)
                if i[1]==mho.hexdigest():
                    session['username']=un
                    return render_template("welcome.html")
                return render_template("home.html", x="bad password")
        return render_template("home.html", x="bad username")
    if lr=="logout":
        session.pop('username') 
        return redirect(url_for('a'))

@app.route("/jacobo")
def js():
    return redirect(url_for('a'))

    

if __name__=="__main__":
    app.run(debug=True)



"""
request.headers   html headers fr client browser

request.method   get or post

request.args    args as a querystring from get request, immutable dictionary

request.form    args sent via post request

return redirect(url_for('foo'))
    
"""
