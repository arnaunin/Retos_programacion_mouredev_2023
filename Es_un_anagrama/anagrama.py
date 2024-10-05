def es_un_anagrama(word1, word2):
    word1 = word1.lower()
    word2 = word2.lower()

    if len(word1) != len(word2) or word1 == word2:
        return False
    else:
        for letter in word1:
            if letter not in word2:
                return False
            
        return True
    
print(es_un_anagrama('castor','Castro'))
