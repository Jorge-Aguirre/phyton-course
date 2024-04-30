def show_messages(messages):
    for message in messages:
        print(f"{message.title()}")

messages = [
    'hello world',
    'for the horde',
    'you know nothing jhon snow',
    'fire and blood'
]

show_messages(messages)