import random
from flask import Flask
from flask import render_template
app=Flask("Genskill")
@app.route("/")
def hello():
    return render_template("index.html")
@app.route("/pi")
def estimate_pi(iters=15000):
    inside=0.0
    for _ in range(iters):
        x=random.random()
        y=random.random()
        if (x**2+y**2)<=1:
            inside+=1
    estimate=4*inside/iters 
    return render_template("estimate.html",algorithm="Monte Carlo simulation",iters=iters,estimate=estimate)
    
@app.route("/pi2")
def estimate_wallis(iters=1000):
    cap=0.0
    acc=1.0
    for n in range(1,iters+1):
        acc=acc*(4*(n**2))/(4*(n**2)-1)
    acc=2*acc
    return render_template("estimate.html",algorithm="Wallis product",iters=cap,estimate=acc)
if __name__=="__main__":
    app.run()
    
