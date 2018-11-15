# -*- coding: utf-8 -*-
vowels     = [u'A',u'À',u'Á',u'Â',u'Ã',u'Ä',u'Å',u'Ā',u'Ą',u'E',u'È',u'É',u'Ê',u'Ë',u'Ē',u'Ĕ',u'Ė',u'Ę',u'Ě',u'I',u'Ì',u'Í',u'Î',u'Ï',u'Ĩ',u'Ī',u'Ĭ',u'Į',u'O',u'Ò',u'Ó',u'Ô',u'Õ',u'Ö',u'Ø',u'Ō',u'Ŏ',u'Ő',u'U',u'Ù',u'Ú',u'Û',u'Ü',u'Ũ',u'Ū',u'Ŭ',u'Ů',u'Ű']
consonants = [u'B',u'C',u'Ç',u'Ĉ',u'Č',u'D',u'Ď',u'F',u'G',u'Ĝ',u'Ģ',u'H',u'Ĥ',u'Ħ',u'J',u'Ĵ',u'K',u'Ķ',u'L',u'Ĺ',u'Ļ',u'Ł',u'M',u'N',u'Ņ',u'Ň',u'P',u'Þ',u'Q',u'Ŗ',u'Ř',u'R',u'S',u'Ŝ',u'Ş',u'Š',u'T',u'Ţ',u'Ť',u'Ŧ',u'V',u'W',u'Ŵ',u'X',u'Y',u'Ŷ',u'Z',u'Ž']

assert(len(vowels) == len(consonants))

size = len(vowels)

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
    f,m,l=8,12,9
    first, middle, last = nume[0:f].title(), nume[f:(f+m)].title(), nume[f+m:].title()
    return first + " " + middle + " " + last

def to_number(nume):
    nume = nume.replace(' ', '').upper()
    number = 0
    nume_list = []
    for c in nume:
        nume_list.append(c)
    for i,c in enumerate(nume_list):
        try:
           val = vowels.index(c)
        except:
            try:
                val = consonants.index(c)
            except:
                pass
        number = number + (size**i * val)
    return number

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
