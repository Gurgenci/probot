import os
import openai
import time
from openai import OpenAI
from dotenv import load_dotenv
load_dotenv()


from ute import init_openai

(Client, LLM)=init_openai()

# Upload a file with an "assistants" purpose
File = Client.files.create(
  file=open("data/elon.txt", "rb"),
  purpose='assistants'
)

# Add the file to the assistant
Assistant = Client.beta.assistants.create(
  model="gpt-4-1106-preview",
  instructions="You are a school teacher answering students questions about the course material provided to you in text files. If the \
 response is not in the text files, you can respond with 'I don't know'.",
  tools=[{"type": "retrieval"}],
  file_ids=[File.id]
)
Thread = Client.beta.threads.create()

Message = Client.beta.threads.messages.create(
    thread_id=Thread.id,
    role="user",
    content="What is ZeroGen?",
    file_ids=[File.id]
)

run = Client.beta.threads.runs.create(
  thread_id=Thread.id,
  assistant_id=Assistant.id,
  instructions="Please use the information in the files.  If the files do not have the information, \
    answer `I do not know`."
)

print("RUN STARTED.  run id: ", run.id)

print(run.status, end=" ")
while run.status != "completed":
    run = Client.beta.threads.runs.retrieve(thread_id=run.thread_id, run_id=run.id)
    print(run.status, end=" ")
    if run.status == "completed":
        print("Completed")
        break
    else:
        time.sleep(1)

messages = Client.beta.threads.messages.list(thread_id=Thread.id)
print(messages.data[0].content[0].text.value)

