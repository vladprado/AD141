sentence = input("Entre com uma sentença; ")

print(f"O primeiro caracter é {sentence[0]} \
e tem {sentence.count(sentence[0])} ocorrências.")
         
print(f"O último caracter é {sentence[len(sentence) - 1]} \
e tem {sentence.count(sentence[len(sentence) - 1])} ocorrências")
