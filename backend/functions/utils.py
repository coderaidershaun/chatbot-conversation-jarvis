import os
import json
import random

# Save messages for retrieval later on
def get_recent_messages(request_message):

  # Define the file name
  file_name = "stored_data.json"
  learn_instruction = {"role": "system", "content": "You are a teacher, the user is called Shaun. "}
  is_language = False
  messages = []
  
  # Add Language teaching element - Spanish
  if "spanish" in request_message.lower():
    is_language = True
    learn_instruction["content"] = learn_instruction["content"] + "You are teaching me Spanish. "

  # Add Language teaching element - Chinese
  if "chinese" in request_message.lower():
    is_language = True
    learn_instruction["content"] = learn_instruction["content"] + "You are teaching me Chinese. "

  # Add Sales Element
  if not is_language:
    learn_instruction["content"] = learn_instruction["content"] + "You really want to give a discount to your new Udemy course. "

  # Add Random Element
  x = random.uniform(0, 1)
  if x < 0.3:
    learn_instruction["content"] = learn_instruction["content"] + "Your response will have dry and sometimes sarcastic humour. "
  else:
    learn_instruction["content"] = learn_instruction["content"] + "You will be encouraging. "

  # Append instruction to message
  messages.append(learn_instruction)

  # Get last messages
  try:
    with open(file_name) as user_file:
      data = json.load(user_file)
      
      # Append last 3 rows of data
      if data:
        if len(data) < 3:
          for item in data:
            messages.append(item)
        else:
          for item in data[-3:]:
            messages.append(item)
  except:
    pass

  
  # Return messages
  return messages


# Save messages for retrieval later on
def store_messages(request_message, response_message):

  # Define the file name
  file_name = "stored_data.json"

  # Get recent messages
  messages = get_recent_messages(request_message)[1:]

  # Add messages to data
  user_message = {"role": "user", "content": request_message}
  assistant_message = {"role": "assistant", "content": response_message}
  messages.append(user_message)
  messages.append(assistant_message)

  # Save the updated file
  with open(file_name, "w") as f:
    json.dump(messages, f)

