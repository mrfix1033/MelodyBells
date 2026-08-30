with open("files/file.py") as file:
    for index, line in enumerate(file.readlines(), start=1):
        print(f"{index}) {line[:-1]}")
