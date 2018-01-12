def count_vowels(word):
    a_counts = word.count('a')
    e_counts = word.count('e')
    i_counts = word.count('i')
    o_counts = word.count('o')
    u_counts = word.count('u')

    return a_counts + e_counts + i_counts + o_counts + u_counts

print(count_vowels("aovvouOucvicIIOveeOIclOeuvvauouuvciOIsle"))
print(count_vowels("aaassseefffgggiiijjjoOOkkkuuuu"))
