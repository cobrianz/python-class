message = input('> ')
words = message.split(' ')
emojis = {
    ':)' : '😊',
    ':D' : '😃',
    ':-(' : '😞',
    ':-D' : '😁'
}
output = ''
for word in words:
    output += emojis.get(word, word) + ' '
print(output)