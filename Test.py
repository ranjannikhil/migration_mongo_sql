#!/usr/bin/env python
# coding: utf-8

# In[2]:


import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="rohit"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE Nikhil")


# In[4]:


mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="rohit",
  database="Nikhil"
)
mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE users (name VARCHAR(200), address VARCHAR(200),mobileno varchar(13))")


# In[ ]:



sql = "INSERT INTO users (name, address,mobileno) VALUES ('sharma', 'Noida',1111106070)"


mycursor.execute(sql)

mydb.commit()

print(mycursor.rowcount, "record inserted.")


# In[ ]:


pip install pyodbc


# In[ ]:


import pandas as pd
sql_query = pd.read_sql_query('''
                              select * from Nikhil.users
                              '''
                              ,mydb) 

df = pd.DataFrame(sql_query)
df.to_csv (r'C:\Users\ROHIT RAJ\Desktop\Nikhil\exported_data.csv', index = False) 


# In[ ]:


pip install PyMongo


# In[13]:


import pymongo

if __name__=="__main__":
    print("welcome to pyMongo")
    client=pymongo.MongoClient("mongodb://localhost:27017/")
    print(client)
    db=client['harry']
    collection=db['sample']
    dictionary={'name':'Nikhil-1','marks':60}
    collection.insert_one(dictionary)


# In[25]:


import pymongo
import pandas as pd
import json

client=pymongo.MongoClient("mongodb://localhost:27017/")
df=pd.read_csv(r"C:\Users\ROHIT RAJ\Desktop\Nikhil\exported_data.csv")


# In[26]:


df.head()


# In[27]:


data=df.to_dict(orient="records")
data


# In[28]:


db=client["harry"]


# In[29]:


print(db)


# In[30]:


db.Iris.insert_many(data)


# In[ ]:




