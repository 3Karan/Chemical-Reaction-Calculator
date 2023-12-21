from flask import Flask,render_template,jsonify, request, send_file 
from flask_cors import CORS, cross_origin
import json
import os


app=Flask(__name__)

  
@app.route("/")
def home_view():
        return render_template('index.html')


cors = CORS(app, resources={r"/*": {"origins": "*"}})
@app.route("/chemicalCALC", methods = ['POST','OPTIONS'])
@cross_origin()
def disp():
     body=request.json
     #print(body)
     output = chemicalCALC(body)
     #print(output)
     return {'data': output}


@app.route('/download')
def download_file():
  p = "reaction.xml"
  result = send_file(p,as_attachment=True)
  #os.remove(p)
  return result

import numpy as np
import pandas as pd
#from lxml import etree


def chemicalCALC(expression):
  
  exp = str(expression.get('exp'))
  return evaluate(exp) 


def CreateReactions(left,right,rate):
  rea = ""
  for i in range(len(left)):
      if i == len(left) - 1:
        rea = rea + left[i]
      else : 
        rea = rea + left[i] + " + "
      

  rea = rea + " --" + "("+ rate+")"+ "--> "

  for i in range(len(right)):
      if i == len(right) - 1:
        rea = rea + right[i]
      else : 
        rea = rea + right[i] + " + "
  
  return rea

# Variables for Additon 
Xlable = "X"
Glable = "G"
Ylable = "Y"
X1lable = "X1" 
X2lable = "X2" 
Xablable = "Xab"
Gablable = "Gab"
X1ablable = "X1ab"
X2ablable = "X2ab"
Zlable = "Z"
Philable = "phi"
ilable = "i"
Y1lable = "Y1" 

I =  0
Y1  = 0
X =  0  
Y = 0
G =  0
X1 = 0 
X2  = 0
Xab = 0
Gab = 0
X1ab = 0
X2ab = 0 
Z=0
Phi = 0


varAddition = [Xlable,Ylable,Glable,X1lable,X2lable,Xablable,Gablable,X1ablable,X2ablable,Zlable]
varSubstraction = [Xlable,Ylable,Glable,X1lable,X2lable,Xablable,Gablable,X1ablable,X2ablable,Zlable]
varMultiplication = [Xlable,Ylable,ilable,Y1lable,Zlable]
varDivision = [Xlable,Ylable,Glable,X1lable,X2lable,Xablable,Gablable,X1ablable,X2ablable,Zlable]



#Additon 

def eveluateReactionsAdd(reactions,historyTable,x,y):
  #reactions
  rea1 = reactions[0]
  rea2 = reactions[1]
  rea3 = reactions[2]
  rea4 = reactions[3]
  rea5 = reactions[4]
  rea6 = reactions[5]

  global X  
  global G  
  global Y
  global Z
  global X1  
  global X2  
  global Xab 
  global Gab 
  global X1ab 
  global X2ab  
  global Phi

  Y=y

  X1 = x
  X = 0 
  
  numberOfItr = x; 

  historyTable.loc[len(historyTable)] = [rea1,numberOfItr,X,Y,G,X1,X2,Xab,Gab,X1ab,X2ab,Z]

  #rea2 
  #rea1  
  Xab = G
  historyTable.loc[len(historyTable)] = ["adding Xab",0,X,Y,G,X1,X2,Xab,Gab,X1ab,X2ab,Z]
  
  G = 0
  Xab = 0 
  numberOfItr = G; 

  historyTable.loc[len(historyTable)] = [rea2,numberOfItr,X,Y,G,X1,X2,Xab,Gab,X1ab,X2ab,Z]

  #rea3 
  
  Gab = X1 
  historyTable.loc[len(historyTable)] = ["adding Gab",0,X,Y,G,X1,X2,Xab,Gab,X1ab,X2ab,Z]
  
  Gab = 0
  X = x-1
  X2 = X 
  X1 = 1 
   
  numberOfItr = X; 

  historyTable.loc[len(historyTable)] = [rea3,numberOfItr,X,Y,G,X1,X2,Xab,Gab,X1ab,X2ab,Z]

  #rea4 
  
  numberOfItr = X2 ; 
  X2 = 0
  
  historyTable.loc[len(historyTable)] = [rea4,numberOfItr,X,Y,G,X1,X2,Xab,Gab,X1ab,X2ab,Z]


  #rea5 
  
  Gab = X1 
  X2ab = X1 
  historyTable.loc[len(historyTable)] = ["adding X2ab and Gab",0,X,Y,G,X1,X2,Xab,Gab,X1ab,X2ab,Z]

  
  G2ab = 0 
  X2ab = 0

  numberOfItr = X1; 
  X1 = 0
  X = X + 2
  
  historyTable.loc[len(historyTable)] = [rea5,numberOfItr,X,Y,G,X1,X2,Xab,Gab,X1ab,X2ab,Z]

  #rea6

  Z = X

  historyTable.loc[len(historyTable)] = [rea6,numberOfItr,X,Y,G,X1,X2,Xab,Gab,X1ab,X2ab,Z]

 
  return historyTable

def eveluateSubReactionsAdd(reactions,x,y):
      
    global X  
    global  G  
    global Y
    global Z
    global X1  
    global X2  
    global Xab 
    global Gab 
    global X1ab 
    global X2ab  
    global Phi


        
    X =  x
    G =  x
    Y = y
    Z = 0


    X1 = 0 
    X2  = 0
    Xab = 0
    Gab = 0
    X1ab = 0
    X2ab = 0 
    Phi = 0



    
    historyTable = pd.DataFrame(columns=["reaction", "NumberOfIterations", Xlable, Ylable, Glable, X1lable, X2lable, Xablable, Gablable, X1ablable, X2ablable, Zlable])
    historyTable = historyTable.append({"reaction": "Intial Values", "NumberOfIterations": 0, Xlable: X, Ylable: Y, Glable: G, X1lable: X1, X2lable: X2, Xablable: Xab, Gablable: Gab, X1ablable: X1ab, X2ablable: X2ab, Zlable: Z}, ignore_index=True )

    while y>0 : 
      eveluateReactionsAdd(reactions,historyTable,X,y) 
      y = y - 1 


    return Z,historyTable   

def Addition(x,y):

  print(x,y)
  #chemical reaction for Addition
  rea1 = CreateReactions (np.array([Xlable,Glable]),np.array([X1lable,Glable]),"Slow")
  rea2 = CreateReactions (np.array([Glable,Xablable]),np.array([Philable]),"Slow")
  rea3 = CreateReactions (np.array(["2"+X1ablable,Gablable]),np.array([Zlable,X1lable,X2lable]),"fast")
  rea4 = CreateReactions (np.array([X2lable]),np.array([Philable]),"Slow")
  rea5 = CreateReactions (np.array([X1lable,X2lable,Gablable]),np.array([Xlable]),"Slow")
  rea6 = CreateReactions (np.array([Xlable]),np.array([Zlable]),"Slow")

  s = "Addition of "+ str(x) + " and " + str(y)
  reactions = []
  reactions.append(rea1)
  reactions.append(rea2)
  reactions.append(rea3)
  reactions.append(rea4)
  reactions.append(rea5)
  reactions.append(rea6)

  for i in range(6):
    print(reactions[i])



  pd.set_option('display.max_rows', None)
  pd.set_option('display.max_columns', None)
  pd.set_option('display.width', 1000)
  pd.set_option('display.colheader_justify', 'center')
  pd.set_option('display.precision', 2)

    
  ans,historyTable=  eveluateSubReactionsAdd(reactions,x,y)

  return s,reactions,ans,historyTable.values.tolist(),varAddition,historyTable



#Substraction 

def eveluateReactionsSub(reactions,historyTable,x,y):
  #reactions
  rea1 = reactions[0]
  rea2 = reactions[1]
  rea3 = reactions[2]
  rea4 = reactions[3]
  rea5 = reactions[4]
  rea6 = reactions[5]

  global X  
  global G  
  global Y
  global Z
  global X1  
  global X2  
  global Xab 
  global Gab 
  global X1ab 
  global X2ab  
  global Phi

  Y=y

  #rea1  
  X1 = x
  X = 0 
  
  numberOfItr = x; 

  historyTable.loc[len(historyTable)] = [rea1,numberOfItr,X,Y,G,X1,X2,Xab,Gab,X1ab,X2ab,Z]

  #rea2 
  Xab = G
  historyTable.loc[len(historyTable)] = ["adding Xab",0,X,Y,G,X1,X2,Xab,Gab,X1ab,X2ab,Z]
  
  G = 0
  Xab = 0 
  numberOfItr = G; 

  historyTable.loc[len(historyTable)] = [rea2,numberOfItr,X,Y,G,X1,X2,Xab,Gab,X1ab,X2ab,Z]

  #rea3 
  
  Gab = X1 
  historyTable.loc[len(historyTable)] = ["adding Gab",0,X,Y,G,X1,X2,Xab,Gab,X1ab,X2ab,Z]
  
  Gab = 0
  X = x-1
  X2 = X 
  X1 = 1 
   
  numberOfItr = X; 

  historyTable.loc[len(historyTable)] = [rea3,numberOfItr,X,Y,G,X1,X2,Xab,Gab,X1ab,X2ab,Z]

  #rea4 
  
  numberOfItr = X2 ; 
  X2 = 0
  
  historyTable.loc[len(historyTable)] = [rea4,numberOfItr,X,Y,G,X1,X2,Xab,Gab,X1ab,X2ab,Z]


  #rea5 
  
  Gab = X1 
  X2ab = X1 
  historyTable.loc[len(historyTable)] = ["adding X2ab and Gab",0,X,Y,G,X1,X2,Xab,Gab,X1ab,X2ab,Z]

  
  G2ab = 0 
  X2ab = 0

  numberOfItr = X1; 
  X1 = 0
  
  historyTable.loc[len(historyTable)] = [rea5,numberOfItr,X,Y,G,X1,X2,Xab,Gab,X1ab,X2ab,Z]

  #rea6

  Z = X

  historyTable.loc[len(historyTable)] = [rea6,numberOfItr,X,Y,G,X1,X2,Xab,Gab,X1ab,X2ab,Z]

 
  return historyTable

def eveluateSubReactionsSub(reactions,x,y):
      
    global X  
    global  G  
    global Y
    global Z
    global X1  
    global X2  
    global Xab 
    global Gab 
    global X1ab 
    global X2ab  
    global Phi 

        
    X =  x
    G =  x
    Y = y
    Z = 0

    X1 = 0 
    X2  = 0
    Xab = 0
    Gab = 0
    X1ab = 0
    X2ab = 0 
    Phi = 0

    historyTable = pd.DataFrame(columns =["reaction","NumberOfIterations",Xlable,Ylable,Glable,X1lable,X2lable,Xablable,Gablable,X1ablable,X2ablable,Zlable])
    historyTable = historyTable.append ({"reaction":"Intial Values","NumberOfIterations" : 0,Xlable : X,Ylable : Y,Glable:G,X1lable : X1,X2lable :X2,Xablable:Xab,Gablable:Gab,X1ablable:X1ab,X2ablable:X2ab,Zlable:Z}, ignore_index = True)

    
    while y>0 : 
      eveluateReactionsSub(reactions,historyTable,X,y) 
      y = y - 1 



    return Z,historyTable   

def Substraction(x,y):

  #chemical reaction for sub 
  rea1 = CreateReactions (np.array([Xlable,Glable]),np.array([X1lable,Glable]),"Slow")
  rea2 = CreateReactions (np.array([Glable,Xablable]),np.array([Philable]),"Slow")
  rea3 = CreateReactions (np.array(["2"+X1ablable,Gablable]),np.array([Xlable,X1lable,X2lable]),"fast")
  rea4 = CreateReactions (np.array([X2lable]),np.array([Philable]),"Slow")
  rea5 = CreateReactions (np.array([X1lable,X2lable,Gablable]),np.array([Philable]),"Slow")
  rea6 = CreateReactions (np.array([Xlable]),np.array([Zlable]),"Slow")
  s = "Substraction of "+ str(x) + " and " + str(y)
  reactions = []
  reactions.append(rea1)
  reactions.append(rea2)
  reactions.append(rea3)
  reactions.append(rea4)
  reactions.append(rea5)
  reactions.append(rea6)

  for i in range(6):
    print(reactions[i])



  pd.set_option('display.max_rows', None)
  pd.set_option('display.max_columns', None)
  pd.set_option('display.width', 1000)
  pd.set_option('display.colheader_justify', 'center')
  pd.set_option('display.precision', 2)

  
  ans,historyTable  =  eveluateSubReactionsSub(reactions,x,y)

  print(historyTable.values.tolist())

  return s,reactions,ans,historyTable.values.tolist(),varSubstraction,historyTable



#division 
def evaluateDivisionSub(x,y,historyTable,reactions):
    global X  
    global G  
    global Y
    global Z
    global X1  
    global X2  
    global Xab 
    global Gab 
    global X1ab 
    global X2ab  
    global Phi 

    X =  x
    G =  x
    Y = y
    Z = 0
    X1 = 0 
    X2  = 0
    Xab = 0
    Gab = 0
    X1ab = 0
    X2ab = 0 
    Phi = 0

    while y>0 : 
      eveluateReactionsSub(reactions[6:12],historyTable,X,y) 
      y = y - 1 


    return Z   
  
def evaluateDivisionAdd(x,y,historyTable,reactions):
    global X  
    global G  
    global Y
    global Z
    global X1  
    global X2  
    global Xab 
    global Gab 
    global X1ab 
    global X2ab  
    global Phi 
    
    X =  x
    G =  x
    Y = y
    Z = 0
    X1 = 0 
    X2  = 0
    Xab = 0
    Gab = 0
    X1ab = 0
    X2ab = 0 
    Phi = 0

    

    while y>0 : 
       eveluateReactionsAdd(reactions[0:6],historyTable,X,y) 
       y = y - 1 


    return Z   

def Division(x,y):
  rea1 = CreateReactions (np.array([Xlable,Glable]),np.array([X1lable,Glable]),"Slow")
  rea2 = CreateReactions (np.array([Glable,Xablable]),np.array([Philable]),"Slow")
  rea3 = CreateReactions (np.array(["2"+X1ablable,Gablable]),np.array([Zlable,X1lable,X2lable]),"fast")
  rea4 = CreateReactions (np.array([X2lable]),np.array([Philable]),"Slow")
  rea5 = CreateReactions (np.array([X1lable,X2lable,Gablable]),np.array([Xlable]),"Slow")
  rea6 = CreateReactions (np.array([Xlable]),np.array([Zlable]),"Slow")
  rea7 = CreateReactions (np.array([Xlable,Glable]),np.array([X1lable,Glable]),"Slow")
  rea8 = CreateReactions (np.array([Glable,Xablable]),np.array([Philable]),"Slow")
  rea9 = CreateReactions (np.array(["2"+X1ablable,Gablable]),np.array([Xlable,X1lable,X2lable]),"fast")
  rea10 = CreateReactions (np.array([X2lable]),np.array([Philable]),"Slow")
  rea11 = CreateReactions (np.array([X1lable,X2lable,Gablable]),np.array([Philable]),"Slow")
  rea12 = CreateReactions (np.array([Xlable]),np.array([Zlable]),"Slow")

  reactions = []
  s = "Division of "  + str(x) + " and " + str(y)
  reactions.append(rea1)
  reactions.append(rea2)
  reactions.append(rea3)
  reactions.append(rea4)
  reactions.append(rea5)
  reactions.append(rea6)
  reactions.append(rea7)
  reactions.append(rea8)
  reactions.append(rea9)
  reactions.append(rea10)
  reactions.append(rea11)
  reactions.append(rea12)

  for i in range(12):
    print(reactions[i])


  pd.set_option('display.max_rows', None)
  pd.set_option('display.max_columns', None)
  pd.set_option('display.width', 1000)
  pd.set_option('display.colheader_justify', 'center')
  pd.set_option('display.precision', 2)


  global X  
  global  G  
  global Y
  global Z
  global X1  
  global X2  
  global Xab 
  global Gab 
  global X1ab 
  global X2ab  
  global Phi 

        
  X =  x
  G =  x
  Y = y
  Z = 0
  X1 = 0 
  X2  = 0
  Xab = 0
  Gab = 0
  X1ab = 0
  X2ab = 0 
  Phi = 0

  historyTable = pd.DataFrame(columns =["reaction","NumberOfIterations",Xlable,Ylable,Glable,X1lable,X2lable,Xablable,Gablable,X1ablable,X2ablable,Zlable])
  historyTable = historyTable.append ({"reaction":"Intial Values","NumberOfIterations" : 0,Xlable : X,Ylable : Y,Glable:G,X1lable : X1,X2lable :X2,Xablable:Xab,Gablable:Gab,X1ablable:X1ab,X2ablable:X2ab,Zlable:Z}, ignore_index = True)
 
  # Calculate sign 
  if((x<0)^(y<0)):
    sign = -1
  else :
    sign = 1  
	
	# Update both divisor and
	# dividend positive
  x = abs(x)
  y = abs(y)
	
	# Initialize the quotient
  quotient = 0
  print(x,y)

  while(x>=y):
    x =  evaluateDivisionSub(x,y,historyTable,reactions)
    quotient=evaluateDivisionAdd(quotient,1,historyTable,reactions)
		
	#if the sign value computed earlier is -1 then negate the value of quotient

  if sign==-1:
    quotient=-quotient
  
  return s,reactions,quotient,historyTable.values.tolist(),varDivision,historyTable

def eveluateReactionsMul(reactions,historyTable,x,y):
  rea1 = reactions[0]
  rea2 = reactions[1]
  rea3 = reactions[2]
  rea4 = reactions[3]

  global X  
  global I  
  global Y  
  global Y1  
  global Z 
  global Phi

  #rea1  
  
  I = I + 1 
  X = x - 1 

  
  numberOfItr = x; 

  historyTable.loc[len(historyTable)] = [rea1,numberOfItr,X,Y,I,Y1,Z]

  #rea2 
  Y = 0
  Y1 = y
  Z = Z + y
  
  numberOfItr = y

  historyTable.loc[len(historyTable)] = [rea2,numberOfItr,X,Y,I,Y1,Z]

  #rea3 
  
  numberOfItr = I; 
  I = 0
  

  historyTable.loc[len(historyTable)] = [rea3,numberOfItr,X,Y,I,Y1,Z]

  #rea4 
  numberOfItr = Y1
  Y = Y1
  Y1 = 0


  historyTable.loc[len(historyTable)] = [rea4,numberOfItr,X,Y,I,Y1,Z]
 
  return historyTable

def eveluateSubReactionsMul(reactions,x,y):
      
    global X  
    global I  
    global Y  
    global Y1  
    global Z 
    global Phi

        
    X =  x
    Y = y
    I =  0
    Y1  = 0
    Z = 0
    Phi = 0

    historyTable = pd.DataFrame(columns =["reaction","NumberOfIterations",Xlable,Ylable,ilable,Y1lable,Zlable])
    historyTable = historyTable.append ({"reaction":"Intial Values","NumberOfIterations" : 0,Xlable : X,Ylable : Y,ilable:I,Y1lable:Y1,Zlable:Z}, ignore_index = True)

    
    while x>0 : 
      eveluateReactionsMul(reactions,historyTable,X,Y) 
      x = x - 1 

    
    
    return Z ,historyTable  




def Multiplication(x,y):

  #chemical reaction for Multiplication
  rea1 = CreateReactions (np.array([Xlable]),np.array([ilable]),"slowest")
  rea2 = CreateReactions (np.array([ilable,Ylable]),np.array([ilable,Y1lable,Zlable]),"fastest")
  rea3 = CreateReactions (np.array([ilable]),np.array([Philable]),"fast")
  rea4 = CreateReactions (np.array([Y1lable]),np.array([Ylable]),"slow")

  reactions = []
  reactions.append(rea1)
  reactions.append(rea2)
  reactions.append(rea3)
  reactions.append(rea4)
  s = "Multiplication of "+ str(x) + " and " + str(y)
  for i in range(4):
    print(reactions[i])


  pd.set_option('display.max_rows', None)
  pd.set_option('display.max_columns', None)
  pd.set_option('display.width', 1000)
  pd.set_option('display.colheader_justify', 'center')
  pd.set_option('display.precision', 2)

  
  ans ,historyTable =  eveluateSubReactionsMul(reactions,x,y)
  return s,reactions,ans,historyTable.values.tolist(),varMultiplication,historyTable

  
# Python3 program to evaluate a given
# expression where tokens are
# separated by space.
 
# Function to find precedence
# of operators.
def precedence(op):
     
    if op == '+' or op == '-':
        return 1
    if op == '*' or op == '/':
        return 2
    return 0
 
# Function to perform arithmetic
# operations.
def applyOp(x, y, op):
     
    #print(x,y)
    if op == '+': 
      print("Addition of ",x, " and ",y)
      return Addition(x,y) 
    if op == '-': 
      print("Substraction of ",x," and ",y)
      return Substraction(x,y) 
     
    if op == '*': 
      print("Multiplication of ",x," and ",y)
      return Multiplication(x,y) 
      
    if op == '/': 
      print("Division of ",x," and ",y)
      return Division(x,y) 
      
  
# Function that returns value of
# expression after evaluation.
def evaluate(tokens):
    # stack to store integer values.
    values = []
    historyTable =[]
    answer = [] 
    variables = []
    S = []
    reactions = []
    # stack to store operators.
    ops = []
    i = 0
    #xml_table = pd.DataFrame(columns = ['reaction'])
    xml_table = []
     
    while i < len(tokens):
         
        # Current token is a whitespace,
        # skip it.
        if tokens[i] == ' ':
            i += 1
            continue
         
        # Current token is an opening
        # brace, push it to 'ops'
        elif tokens[i] == '(':
            ops.append(tokens[i])
         
        # Current token is a number, push
        # it to stack for numbers.
        elif tokens[i].isdigit():
            val = 0
             
            # There may be more than one
            # digits in the number.
            while (i < len(tokens) and
                tokens[i].isdigit()):
             
                val = (val * 10) + int(tokens[i])
                i += 1
             
            values.append(val)
             
            # right now the i points to
            # the character next to the digit,
            # since the for loop also increases
            # the i, we would skip one
            #  token position; we need to
            # decrease the value of i by 1 to
            # correct the offset.
            i-=1
         
        # Closing brace encountered,
        # solve entire brace.
        elif tokens[i] == ')':
         
            while len(ops) != 0 and ops[-1] != '(':
             
                val2 = values.pop()
                val1 = values.pop()

                op = ops.pop()
                s,res,ans,his,var,xml = applyOp(val1, val2, op)
                S.append(s)
                reactions.append(res)
                values.append(ans)
                historyTable.append(his)
                 
                xml_table.extend(xml['reaction'].tolist())
                variables.append(var)

             
            # pop opening brace.
            ops.pop()
         
        # Current token is an operator.
        else:
         
            # While top of 'ops' has same or
            # greater precedence to current
            # token, which is an operator.
            # Apply operator on top of 'ops'
            # to top two elements in values stack.
            while (len(ops) != 0 and
                precedence(ops[-1]) >=
                   precedence(tokens[i])):
                         
                val2 = values.pop()
                val1 = values.pop()

                print(val1," ",val2)
                op = ops.pop()

                s,res,ans,his,var,xml = applyOp(val1, val2, op)
                
                values.append(ans)
                S.append(s)
                reactions.append(res)
                historyTable.append(his)
                xml_table.extend(xml['reaction'].tolist())
                variables.append(var)

  
            # Push current token to 'ops'.
            ops.append(tokens[i])
         
        i += 1
     
    # Entire expression has been parsed
    # at this point, apply remaining ops
    # to remaining values.
    while len(ops) != 0:
         
        val2 = values.pop()
        val1 = values.pop()
        op = ops.pop()
        s,res,ans,his,var,xml = applyOp(val1, val2, op)
        values.append(ans)
        S.append(s)
        reactions.append(res)
        historyTable.append(his) 
        xml_table.extend(xml['reaction'].tolist()) 
        variables.append(var)

    # Top of 'values' contains result,
    # return it.

    xml_table = pd.DataFrame(xml_table)
    xml_table.columns=['Reactions']
    print("XML TABLE :", xml_table)
    xml_table.to_xml('reaction.xml') 
    answer.append(S)
    answer.append(reactions)
    answer.append(historyTable)
    answer.append(variables)
  
    return answer
 
if __name__ == "__main__":
        app.debug = True
        app.run()



