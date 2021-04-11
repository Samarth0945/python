a=input('Enter your string')
words=a.split()
word2=''
long_word_len=len(words[0])
short_word_len=len(words[0])
for i in words:
    word_length=len(i)
    if(word_length>long_word_len):
        long_word_len=word_length
        word1=i
    elif(word_length<short_word_len):
        short_word_len=word_length
        word2=i    
print(word1)
print(word2)        