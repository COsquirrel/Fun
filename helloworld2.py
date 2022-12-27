filename = input("What would you like to name your file?: ")
hello = input("write your Hello World text: ")

fh = open(filename + ".py", "w+")
fh.write("print('" + hello + "')")
fh.close()
