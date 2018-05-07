import os
import random
import spacy
keys=[]
trian_dic=dict()
for files in os.listdir('C:/Users/bahy\Downloads\english'):
    data = open('C:/Users/bahy\Downloads\english/' + files,'r').readlines()
    for i in range(0,(len(data)-1)):
        x=data[i]
        if x.startswith("- -"):
            y=x.replace('-','')
            y = y.replace('\n', '')
            if not y in keys:
                keys.append(y)
            while i < len(data)-1 and not data[i+1].startswith("- -") :
                i+=1
                x = data[i].replace('-', '')
                x = x.replace('\n', '')
                if y in trian_dic:
                    trian_dic[y].append(x)
                else:
                  trian_dic[y] = [x]
nlp = spacy.load('en')
def replay(mess):

    doc = nlp(mess)
    key=""
    max=-1.1
    for x in keys:
            sim=doc.similarity(nlp(x))
            if sim > max:
                max=sim
                key=x

    #print(key)
    return random.choice(trian_dic[key])

message = input('you :')

print('smsm :' + replay(message))

