import os
import openai
import time
from openai import OpenAI
from dotenv import load_dotenv
load_dotenv()
from ute import init_openai, read_page_list, rdweb, embedpagelist, sepstr
from ute import SEP, get_embedding, cosine_similarity
import numpy as np

# Print all the fields of the message object:
def pr_messagefields(message):
    for field in message:
        print(field)

# The following function prints the fields of an object (e.g. a message)
# If the field itself is another class, then it prints its fields as well 
# on separate lines intended by 4 spaces
def pr_objfields(obj):
    for field in obj:
        print(field)
        if isinstance(field, object):
            for subfield in field:
                print("    ", subfield) 
# It is however easier to use the VS Code Debugger to inspect the object
# When using the debugger, it is easier if I do things in separate functions so that
# the scope is limited ot the variables in that function


(Client, LLM)=init_openai()
#
thread_id="thread_0CFhVKH2HIXDPwv89mjBATZZ" # This is copied from Playground
#
thread = Client.beta.threads.retrieve(thread_id) # Retrieve the thread with the given ID string
#
thread_messages=Client.beta.threads.messages.list(thread_id) # Retrieve the list of messages for the thread
#
last_answer=thread_messages.data[0].content[0].text.value # Retrieve the system response to the last question
#
runs = Client.beta.threads.runs.list(thread_id) # Retrieve the list of runs for the thread
pass

print(runs.data[1].instructions)
print(last_answer)