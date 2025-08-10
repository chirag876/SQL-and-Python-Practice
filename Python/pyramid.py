heightofpyramid = 5
spaces = " "
stars = "*"
for i in range(1, heightofpyramid+1):
    spacesres = spaces*(heightofpyramid-i)
    starsres = stars*(2*i-1)
    print(spacesres+starsres)
