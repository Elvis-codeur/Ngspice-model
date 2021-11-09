
import re 

f = open("DIODE.LIB","r").read()

a = re.match("(**********)(*)(**********)")
print(a)