# 14. Обработка строк через преобразование в список
def make_censored(sentence, stop_words):
    seq = '$#%!'
    return ' '.join([seq if word in stop_words else word for word in sentence.split()])

sentence = 'When you play the game of thrones, you win or you die'
print(make_censored(sentence, ['die', 'play']))
# When you $#%! the game of thrones, you win or you $#%!

sentence2 = 'chicken chicken? chicken! chicken'
print(make_censored(sentence2, ['?', 'chicken']))
# '$#%! chicken? chicken! $#%!';