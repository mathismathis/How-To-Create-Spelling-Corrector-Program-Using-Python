from textblob import TextBlob

file1=open("1.txt","r+")
a=file1.read()
b=TextBlob(a)

print(str(b.correct()))
print(b.translate(to="ta"))
file1.close()

file=open("1.txt","w")
file.write(str(b.translate(to="ta")))
file.close()



