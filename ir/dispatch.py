import re 

SUBCKT_FOLDER = "IRFMOSFET/"
MODELS_FOLDER = "IRFDIODES/"

text = open("IR.LIB").read()
# On coupe le texte 
a = text.split("**********")

# On prend les subckt d'un côté et les models d'un côté
models = []
subckt = []
for i in a:
    if ".SUBCKT" in i:
        subckt.append(i)
    elif ".MODEL" in i:
        models.append(i)

def get_name(text,pos):
    """ Recupère le nom du composant 
    qui se trouve juste après le .subckt ou le .model"""
    i = 0
    for i in range(pos,len(text)):
        if(text[i] == " "):
            break 
    return text[pos:i]

# On écrit les subckt
for i in subckt:
    name = get_name(i,i.find(".SUBCKT") + 8)
    f = open(SUBCKT_FOLDER+name+".lib","w")
    f.write(i)
    f.close()
    
# On écrit les models
for i in models:
    name = get_name(i,i.find(".MODEL") + 8)
    f = open(MODELS_FOLDER+name+".lib","w")
    f.write(i)
    f.close()   

models.sort()
print(models)