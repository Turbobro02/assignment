wrd=open('wordsentence.txt','r',encoding='utf-8')
splitter=wrd.read().split()

unless=['Mr.','Ms','Mrs','Dr','Jr.']
sentence=""
for word in splitter:
    if '?' not in word and '!' not in word:
        sentence= (sentence + word + " ")
        if '.' in word[-1] and word in unless:
            pass
        elif '.' in word[-1] and '.' in word[-3] and '.' not in word[-2] :
            pass
        elif '.' in word[-1] and word not in unless:
            sentence= sentence + '\n'
        elif '.' in word[-1] and '.' in word[-2]:
            sentence= sentence + '\n'
    else:
        sentence= sentence + word + "\n"

print(sentence) 
