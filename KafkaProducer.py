#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install kafka-python


# In[2]:


conda install -c conda-forge kafka-python


# In[1]:


from kafka import KafkaProducer


# In[2]:


from time import sleep


# In[3]:


import json


# In[4]:


from datetime import datetime


# In[6]:


producer=KafkaProducer(bootstrap_servers=['localhost:9092'],api_version=(0,10,1))


# In[7]:


producer.send('kafkastreaming',b'Hello,Kafka')


# In[8]:


now=datetime.now()
now


# In[10]:


current_time=now.strftime("%d/%m/%Y %H:%M:%S")
current_time


# In[ ]:


for i in range(10):
    message="Message {}".format(str(datetime.now().time()))
    producer.send('kafkastreaming',json.dumps(message).encode('utf-8'))
    sleep(2)
    print("Message Sent",i)


# In[ ]:





# In[ ]:





# In[ ]:




