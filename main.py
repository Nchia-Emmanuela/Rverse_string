def spin_words(sentence):
   split_word = sentence.split('')
   new_words = []
   for word in split_word:
       if len(word) >= 2:
           new_words.append(word[::-1])
        else:
            new_words.append(word)
    return ' '.join(new_word)