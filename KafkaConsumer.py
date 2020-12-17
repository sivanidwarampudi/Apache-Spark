#!/usr/bin/env python
# coding: utf-8

# In[1]:


from kafka import KafkaConsumer
from json import loads
import json


# In[2]:


consumer=KafkaConsumer("kafkastreaming",bootstrap_servers=['localhost:9092'],
                      api_version=(0,10),consumer_timeout_ms=10
                      )


# In[4]:


for message in consumer:
    print(message.value)

