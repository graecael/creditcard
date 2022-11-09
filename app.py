#!/usr/bin/env python
# coding: utf-8

# In[1]:


from flask import Flask, request, jsonify, render_template
import joblib


# In[2]:


app = Flask(__name__)


# In[3]:


#Values

#Variable 4: Gender
male = 0


#Variable 5: Family Status
widow = 0

#Final Predict
randomforest_pred = 0
decisiontree_pred = 0
logregression_pred = 0

variables_int=[]


# In[4]:


@app.route('/')
def abc():
    return render_template("index.html")

@app.route('/', methods=['POST'])

def index():
    #Variable 1: Age
    age = int(request.form.get('age'))

    #Variable 2: Years Employed
    yearsemployed = int(request.form.get('yearsemployed'))

    #Variable 3: Annual Income Amount
    amtincometotal = int(request.form.get('amtincometotal'))

    #Variable 4: Gender
    gender = request.form.get('gender')
    global male
    if gender == "Male":
        male = 1
    else:
        male = 0

    #Variable 5: Family Status
    family = request.form.get('family')
    global widow
    if family == "Widow":
        widow = 1
    else:
        widow = 0

    #Variable 6: Family Members
    familymem = int(request.form.get('familymem'))

    #Model Runs
    randomforest = joblib.load("randomforest_model")
    decisiontree = joblib.load("decisiontree_model")
    logregression = joblib.load("logregression_model")

    #Array of variables
    variables=[age,yearsemployed,amtincometotal,male,widow,familymem]

    for i in variables:
        variables_int.append(int(i))

    rf1 = randomforest.predict([variables_int])
    dt1 = decisiontree.predict([variables_int])
    lr1 = logregression.predict([variables_int])


    #Indicator
    if rf1 == 0:
        rfvalue = "The assessment shows that you are uneligible for the credit card. Please contact the bank for more enquiries."
    elif rf1 ==1:
        rfvalue = "The assessment shows that you are eligible for the credit card. Please proceed to www.abc.sg/creditcard for further registeration."

    if dt1 == 0:
        dtvalue = "The assessment shows that you are uneligible for the credit card. Please contact the bank for more enquiries."
    elif dt1 ==1:
        dtvalue = "The assessment shows that you are eligible for the credit card. Please proceed to www.abc.sg/creditcard for further registeration."

    if lr1 == 0:
        lrvalue = "The assessment shows that you are uneligible for the credit card. Please contact the bank for more enquiries."
    elif lr1 ==1:
        lrvalue = "The assessment shows that you are eligible for the credit card. Please proceed to www.abc.sg/creditcard for further registeration."

    return(render_template("index.html",result1=rfvalue,result2=dtvalue,result3=lrvalue))


# In[ ]:


if __name__ == "__main__":
    app.run()


# In[ ]:




