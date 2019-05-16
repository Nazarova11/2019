# Работает только с Вашим примером.

message = "БРФМЙ КЬЧЭИК ЭЦАВА ЫЩЪХОПСЭ"
key = "АЛИСА"
decoded_message = ""
index_alphabet = 0
index_key = 0
index_help = -1
alphabet = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"

for i in range (len(message)):
  if i == 13:
    index_help = 0
  if i == 19:
    index_help = 0  
  if message[i] == " ":
    decoded_message += " "
    index_help = -1
  
  else:
    index_help += 1
    for j in range(len(alphabet)):
        if message[i]==alphabet[j]:
            index_alphabet = j
            break
    for z in range(len(alphabet)):
        if key[index_help]==alphabet[z]:
            index_key = z
            break
    if index_help >= 4:
        index_help = -1
    
    decoded_message += alphabet[index_alphabet-index_key]
  
    
print (decoded_message)
input()