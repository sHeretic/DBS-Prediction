#!/usr/bin/env python
# coding: utf-8

# In[1]:


from flask import Flask, render_template, request
# render_template - render the template (in this case it is index.html)
# request - in this case, request for Flask


# In[2]:


app = Flask(__name__)
# double underscore __name__ to ensure that one of the main commands is not incorrectly used.


# In[3]:


import joblib

@app.route("/", methods = ["GET","POST"]) # this is other peoples' program.
# for repetitive code, would use generator/iterator etc. - to save time.
# for generator, use "@"

# now this is my program,
def index():
    if request.method == "POST":
        # AI engine wil be filled here.
        rate = float(request.form.get("rate"))
        print(rate)
        model = joblib.load("DBS_Prediction")
        pred = model.predict([[rate]])
        
        return(render_template("index.html", result=pred)) 
        # return the template & the result value; unknown later will be replaced with the actual result value.
    else:
        return(render_template("index.html", result="waiting"))


# In[ ]:


if __name__ == "__main__":
    app.run()


# ^ Only now then will take the link and copy over to the actual index.html
# <br> Flask is using the 5000 port number.

# In[ ]:




