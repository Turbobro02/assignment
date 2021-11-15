totalwords=open('text.txt','r')

words=totalwords.read().split()
allwrd=len(words)

letters=0

for word in words:
    letters=letters + len(word)

print(round((letters/allwrd)))
