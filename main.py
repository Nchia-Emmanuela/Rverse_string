def spin_words(sentence):
   split_word = sentence.split('')
   new_word = []
   for word in split_word:
       if len(word) >= 2:
           new_word.append(word[::-1])