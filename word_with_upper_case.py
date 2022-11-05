sentence = 'this is very large sentence'
new_sentence = ''
new_sentence += sentence[0].upper()

for i in range(1, len(sentence)):
    if sentence[i-1] == ' ':
        new_sentence += sentence[i].upper()
    else:
        new_sentence += sentence[i]

print(new_sentence)
