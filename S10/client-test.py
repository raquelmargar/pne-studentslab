from P02_RAQUEL_MARTIN.Client0 import Client

PORT = 8080
IP = "212.128.255.97"

c = Client (IP, PORT)
print("Sending a message to the server")
for i in range(5):

    print(f"To Server: Message{i}")
    response = c.talk(f"Message {i}")

    print(f"From Server: {response}")
