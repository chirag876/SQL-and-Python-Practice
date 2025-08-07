text = "Hello World"
words = text.split()  # This will split the string into a list of words
print("Split text:", words)

text2 = "apple,banana,cherry"
words_with_commas = text2.split(',')  # This will split the string by commas
print("Split text by commas:", words_with_commas)

text3 = "one;two;three"
words_with_semicolons = text3.split(';')  # This will split the string by semicolons
print("Split text by semicolons:", words_with_semicolons)