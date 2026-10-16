from pydoc import replace


#reemplazamos las vocales del nombre
original="Samuel Junior Agramonte"

for vocal in "aeiou":
    original=original.replace(vocal,"***")
print(original)