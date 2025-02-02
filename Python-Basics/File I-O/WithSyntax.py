with open("Filing_read01.txt","r") as f:
    print(f.read())

with open("Filing_read01.txt", "a") as f:
    f.write("\nAppending with the With Syntax")