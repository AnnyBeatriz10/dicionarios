fd = open("logs.txt","r")
logs = {}

for linha in fd:
   hora = linha.split()[0][1:]
   logs[hora] = logs.get(hora,0) +1 # acesse logs[hora] e pegue o seu valor, caso o índice não exista, traga zero

print(logs)

fd.close()

print(k)

maxkey = None # None = Nada
for key in logs.key():
   if maxkey == None or logs[key] > logs[maxkey]:
      maxkey = key
print(maxkey)

keys = log.keys()
maxkey = keys[0]
for key in keys: # keys : o key vai ser cada uma das chaves no conjunto de chaves
    if log[key] > logs[maxkey]:
      maxkey = key
print(maxkey, logs[maxkey])

# bigChars