f = open("newfile.txt", "a")
lines = ["Hello","World","What is going on","Studying IO"]
text = "\n".join(lines)
f.writelines(text)

f.close()