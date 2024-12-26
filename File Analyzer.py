try:
    with open("gude",'r') as file:
        content=file.read()
        lines=content.split('\n')
        words=content.split()
        char=len(content)
        print("number of lines are:",len(lines))
        print("number of words:",len(words))
        print("number of characters:",char)
except FileNotFoundError:
    print("Error: File not found.")
