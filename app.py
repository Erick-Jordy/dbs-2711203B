#!/usr/bin/env python
# coding: utf-8

# In[1]:


from flask import Flask,request,render_template


# In[ ]:


app = Flask(__name__)

@app.route('/', methods = ['GET','POST']) # Function that run before your actual functiin

def index():
    if request.method == 'POST':
        rate = float(request.form.get('rate'))
        print(rate)
        return (render_template('index.html', result = -50.6 * rate + 90.2))
    else:
        return(render_template('index.html', result = 'waiting for exchange rate'))
    
if __name__ == '__main__':
    app.run()


# In[1]:




