from flask import Flask,render_template,url_for
from form import GraphForm
import numpy as np
from generator import Polynomial,Trignometric,Logarithmic,Exponential
import matplotlib
import matplotlib.pyplot as plt
matplotlib.use('Agg')


app=Flask(__name__)
app.config["SECRET_KEY"]="key"

p=Polynomial()
t=Trignometric()
l=Logarithmic()
e=Exponential()

count=0

@app.route('/',methods=['POST','GET'])
@app.route('/home',methods=['POST','GET'])
def home():
    return render_template('index.html')



@app.route('/generator',methods=['POST','GET'])
def graphgen():
    val=False
    form=GraphForm()
    if form.validate_on_submit():
        global count
        count+=1
        eq=form.Equation.data 
        val=True
        if (eq[0]=='s')|(eq[0]=='c')|(eq[0]=='t'):
            t.draw(eq)
            t.x_final=np.array([])
            t.y_final=[]
        elif eq[0]=='l':
            l.draw(eq)
            l.x_final=np.array([])
            l.y_final=[]
        elif (eq[0]=='x')|(eq[0]=='-'):
            p.draw(eq)
            p.x_final=np.array([])
            p.y_final=[]
        else :
            e.draw(eq)
            e.x_final=np.array([])
            e.y_final=[]
        return render_template('gen.html',form=form,val=val,eq=eq,url='static/test{}.png'.format(count))
    return render_template('gen.html',form=form,val=val)

if __name__=='__main__':
    app.run(debug=True)
   
        
