with open("notes.txt","r") as file:
    for _ in range(10):
        print(file.readline().strip())