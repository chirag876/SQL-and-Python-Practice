import textwrap


def textwrapcheck(string, maxwidht):
    return textwrap.fill(string, maxwidht)


s = 'Chirag'
maxwidth = 1

print(textwrapcheck(s, maxwidth))
