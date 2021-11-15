textsee=open('worded.txt','r')
textnew=open('newtext.txt','w')

sentence=textsee.read().split("\n")
numberlines= 1

for line in sentence:
    textnew.write(str(numberlines)+ " "+ line+ "\n")
    numberlines= numberlines+1
