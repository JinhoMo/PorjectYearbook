import os

names = []
passed = ""

while True:
    user = input("Name : ")
    with open(f"{os.getcwd()}\\list.txt", "r") as f:
        names = [i.strip("\n") for i in map(str.lower, f.readlines())]
        # print(names)
        with open(f"{os.getcwd()}\\list.txt", "w") as file:
            try:
                names.remove(user.lower())
                passed = user.lower()
            except Exception:
                print("non-existing name")
                file.write("\n".join(names))
                continue

            file.write('\n'.join(names))

        with open(f"{os.getcwd()}\\passed.txt", "a") as f:
            f.write(passed + "\n")
