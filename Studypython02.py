#no java, não embaralhar
#for (i = 0; i <= 10; i++)
#inicio, fim, salto
for i in range(10):
  print(i)
#-------------------  
  nome = 'fulano'
for x in nome:
  print(x)
  print(nome)
 #---------------------
 i = 0
while i < 6:
 print(i)
 i += 1
 # ou 
 #i = i + 1
#-----------------  
texto = input('digite uma palavra com a ')
#print(texto[0])
while texto[0] != 'a' and texto[0] != 'A':
  print('Digite de novo')
  texto = input()
print ('a palavra foi ', texto)
 
