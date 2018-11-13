# -*- coding: utf-8 -*-
# all_characters='AÀÁÂÃÄÅĀĂĄBCÇĆĈĊČDÐĎEÈÉÊËĒĔĖĘĚFGĜĞĠĢHĤĦIÌÍÎÏĨĪĬĮJĴKĶLĹĻĽĿŁMNÑŃŅŇOÒÓÔÕÖØŌŎŐPÞQŔŖŘRSŚŜŞŠTŢŤŦUÙÚÛÜŨŪŬŮŰŲVWŴXYÝŶZŹŻŽ'
all_characters=u'AÀÁÂÃÄÅĀĂĄBCÇĈČDÐĎEÈÉÊËĒĔĖĘĚFGĜĢHĤĦIÌÍÎÏĨĪĬĮJĴKĶLĹĻŁMNŅŇOÒÓÔÕÖØŌŎŐPÞQŖŘRSŜŞŠTŢŤŦUÙÚÛÜŨŪŬŮŰVWŴXYŶZŽ'
vowels=u'AÀÁÂÃÄÅĀĄEÈÉÊËĒĔĖĘĚIÌÍÎÏĨĪĬĮOÒÓÔÕÖØŌŎŐUÙÚÛÜŨŪŬŮŰ'
# consonants='BCÇĆĈĊČDÐĎFGĜĞĠĢHĤĦJĴKĶLĹĻĽĿŁMNÑŃŅŇPÞQŔŖŘRSŚŜŞŠTŢŤŦVWŴXYÝŶZŹŻŽ'
consonants=u'BCÇĈČDĎFGĜĢHĤĦJĴKĶLĹĻŁMNŅŇPÞQŖŘRSŜŞŠTŢŤŦVWŴXYŶZŽ'
size=48 # some characters were omitted because the lower case forms were iffy

# size=50
# vowels='a'*size
# consonants='b'*size
# consonants='BCÇĆĈĊČDÐĎFGĜĞĠĢHĤĦJĴKĶLĹĻĽĿŁMNÑŃŅŇPÞQŔŖŘRSŚŜŞŠTŢŤŦVWŴXYÝŶZŹŻŽ'

# len(vowels) is incorrect... It doesn't seem to handle extended unicode well?

def is_odd(number): return number % 2 != 0

def next_character(number, use_vowel_set): # returns (character, new_set, rem_val)
    val = number % size
    rem_val = (number - val) / size
    if use_vowel_set:
        return vowels[val], False, rem_val
    else:
        return consonants[val], True, rem_val

def to_nume_inner(number):
    nume = ''
    use_vowel_set = is_odd(number)
    while (number > 0):
        c, use_vowel_set, number = next_character(number, use_vowel_set)
        nume = nume + c
    return nume

def to_nume(number):
    nume = to_nume_inner(number)
    #8 12 9
    f,m,l=8,12,9
    first, middle, last = nume[0:f].title(), nume[f:(f+m)].title(), nume[f+m:].title()
    return first + " " + middle + " " + last

#160

"""
We could make our own alphabet, in a way . . .
Custom font for now, mapped to an extended unicode . . .
I think LaTeX allows for adding any accent marker to a character,
so this wouldn't be too hard to specify formally.

(accents per vowel)    (eth addr size)
10                  => 29
15                  => 26
20                  => 23

Numes could be split up into three (first, middle, last)
(Middles only displayed if collision between two users and
un-accented names)
(Accent marks resolve all collisions, except for crypto collisions!)

göţįlãqãtâņūŷôŷåbėrožüsěĵíłũð
"""

print((to_nume(2**160)))