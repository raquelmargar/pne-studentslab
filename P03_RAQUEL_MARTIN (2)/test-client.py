from P02_RAQUEL_MARTIN.Client0 import Client

c = Client("127.0.0.1", 8080)

print("* Testing PING...")
print(c.talk("PING"))

print("* Testing GET...")
seq0 = c.talk("GET 0")
print("GET 0:", seq0)

print("* Testing INFO...")
print(c.talk(f"INFO {seq0}"))

print("* Testing COMP...")
print(c.talk(f"COMP {seq0}"))

print("* Testing REV...")
print(c.talk(f"REV {seq0}"))

print("* Testing GENE U5...")
print(c.talk("GENE U5"))