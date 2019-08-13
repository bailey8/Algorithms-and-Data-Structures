word = 'paper'
len(word)
words = ['banana', 'pie', 'Washington', 'book']
sorted(words, key=len)

#KEY MUST CONFORM TO ALL ITERABLE VALUES
values_to_cast = ['1', '2', '3', 'four']
sorted(values_to_cast, key=int)

words = ['banana', 'pie', 'Washington', 'book']
sorted(words, key=lambda x: x[::-1])