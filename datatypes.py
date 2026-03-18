# price = 1500
# tax = 0.18
# total = price + (price * tax)
# print(f"The total price is {total}")


# username = "Marius"
# message = "Welcome back {}".format(username)
# print(message)


# messages = ["Hi", "How are you?", "I'm fine"]

# messages.append("What about you?")
# print(messages[0])

# user = {
#     "id":1,
#     "name":"Marius",
#     "email":"mariussangwa@gmail.com",
    
# }

# print(user)


messages = [
    {"sender": "A", "text": "Hi"},
    {"sender": "B", "text": "Hello"}
]

for msg in messages:
    print(msg["text"])
