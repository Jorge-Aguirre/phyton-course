messages = [
    'hello world',
    'for the horde',
    'you know nothing jhon snow',
    'fire and blood'
]

sent_messages = []

def send_messages(messages, sent_messages):
    while messages:
        message = messages.pop()
        sent_messages.append(message)

send_messages(messages[:], sent_messages)
print(messages)
print(sent_messages)