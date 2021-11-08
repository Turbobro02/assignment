j=open('C:/Users/LENOVO/OneDrive/Desktop/textdoctime.txt',"r")
scanned=j.read()
cut=scanned.split()

counted={}
for word in cut:
    counted[word]=counted.get(word,0)+1

for key,value in counted.items():
    if value ==1:
        print(key)
