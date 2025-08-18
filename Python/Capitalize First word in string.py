def capitalizestring(s):
    
    return ' '.join(w.capitalize() for w in s.split(" ") )


s = "chirag gupta"
print(capitalizestring(s))