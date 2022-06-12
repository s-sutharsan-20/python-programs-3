def anagram(word1,word2):
    word1=word1.lower()
    word2=word2.lower()
    return sorted(word1)==sorted(word2)
a=input("Enter any word  :")
b=input("Enter another word  :")
print(anagram(a,b))
