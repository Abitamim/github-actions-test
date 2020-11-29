from push_receiver import register, listen
import json
from os import system
from pathlib import Path

SENDER_ID = 896342988239

def on_notification(obj, notification, data_message):
  idstr = data_message.persistent_id + "\n"

  # check if we already received the notification
  with open("persistent_ids.txt", "r") as f:
    if idstr in f:
      return

  # new notification, store id so we don't read it again
  with open("persistent_ids.txt", "a") as f:
    f.write(idstr)

  # print notification
  n = notification["notification"]
  text = n["title"]
  if n["body"]:
    text += ": " + n["body"]
  print(text)
  system("bash -c 'git pull'")
  arduino_run = Path ("run_code.txt").read_text()
  system(arduino_run)


if __name__ == "__main__":

  try:
    # already registered, load previous credentials
    with open("credentials.json", "r") as f:
      credentials = json.load(f)

  except FileNotFoundError:
    # first time, register and store credentials
    credentials = register(sender_id=SENDER_ID)
    with open("credentials.json", "w") as f:
      json.dump(credentials, f)

  print("send notifications to {}".format(credentials["fcm"]["token"]))

  with open("persistent_ids.txt", "a+") as f:
    received_persistent_ids = [x.strip() for x in f]

  listen(credentials, on_notification, received_persistent_ids)