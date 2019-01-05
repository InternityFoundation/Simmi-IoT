
file = input("Enter file name  write content: ")
c = open(file, "w")
print(" write on the file: ")
sent = input()
c.write(sent)
c.write("\n")
c.close()
print("\nContent successfully placed inside the file.!!")