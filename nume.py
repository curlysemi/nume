# -*- coding: utf-8 -*-
vowels     = [u'A',u'À',u'Á',u'Â',u'Ã',u'Ä',u'Å',u'Ā',u'Ą',u'E',u'È',u'É',u'Ê',u'Ë',u'Ē',u'Ĕ',u'Ė',u'Ę',u'Ě',u'I',u'Ì',u'Í',u'Î',u'Ï',u'Ĩ',u'Ī',u'Ĭ',u'Į',u'O',u'Ò',u'Ó',u'Ô',u'Õ',u'Ö',u'Ø',u'Ō',u'Ŏ',u'Ő',u'U',u'Ù',u'Ú',u'Û',u'Ü',u'Ũ',u'Ū',u'Ŭ',u'Ů',u'Ű']
consonants = [u'B',u'C',u'Ç',u'Ĉ',u'Č',u'D',u'Ď',u'F',u'G',u'Ĝ',u'Ģ',u'H',u'Ĥ',u'Ħ',u'J',u'Ĵ',u'K',u'Ķ',u'L',u'Ĺ',u'Ļ',u'Ł',u'M',u'N',u'Ņ',u'Ň',u'P',u'Þ',u'Q',u'Ŗ',u'Ř',u'R',u'S',u'Ŝ',u'Ş',u'Š',u'T',u'Ţ',u'Ť',u'Ŧ',u'V',u'W',u'Ŵ',u'X',u'Y',u'Ŷ',u'Z',u'Ž']

# The following is essentially a lookup table used to strip the accents
# from complete numes.
lookups = {
    # vowels
    u'A': 'A',
    u'À': 'A',
    u'Á': 'A',
    u'Â': 'A',
    u'Ã': 'A',
    u'Ä': 'A',
    u'Å': 'A',
    u'Ā': 'A',
    u'Ą': 'A',

    u'E': 'E',
    u'È': 'E',
    u'É': 'E',
    u'Ê': 'E',
    u'Ë': 'E',
    u'Ē': 'E',
    u'Ĕ': 'E',
    u'Ė': 'E',
    u'Ę': 'E',
    u'Ě': 'E',

    u'I': 'I',
    u'Ì': 'I',
    u'Í': 'I',
    u'Î': 'I',
    u'Ï': 'I',
    u'Ĩ': 'I',
    u'Ī': 'I',
    u'Ĭ': 'I',
    u'Į': 'I',

    u'O': 'O',
    u'Ò': 'O',
    u'Ó': 'O',
    u'Ô': 'O',
    u'Õ': 'O',
    u'Ö': 'O',
    u'Ø': 'O',
    u'Ō': 'O',
    u'Ŏ': 'O',
    u'Ő': 'O',

    u'U': 'U',
    u'Ù': 'U',
    u'Ú': 'U',
    u'Û': 'U',
    u'Ü': 'U',
    u'Ũ': 'U',
    u'Ū': 'U',
    u'Ŭ': 'U',
    u'Ů': 'U',
    u'Ű': 'U',

    # consonants
    u'B': 'B',
    u'C': 'C',
    u'Ç': 'C',
    u'Ĉ': 'C',
    u'Č': 'C',
    u'D': 'D',
    u'Ď': 'D',
    u'F': 'F',
    u'G': 'G',
    u'Ĝ': 'G',
    u'Ģ': 'G',
    u'H': 'H',
    u'Ĥ': 'H',
    u'Ħ': 'H',
    u'J': 'J',
    u'Ĵ': 'J',
    u'K': 'K',
    u'Ķ': 'K',
    u'L': 'L',
    u'Ĺ': 'L',
    u'Ļ': 'L',
    u'Ł': 'L',
    u'M': 'M',
    u'N': 'N',
    u'Ņ': 'N',
    u'Ň': 'N',
    u'P': 'P',
    u'Þ': 'P',
    u'Q': 'Q',
    u'Ŗ': 'R',
    u'Ř': 'R',
    u'R': 'R',
    u'S': 'S',
    u'Ŝ': 'S',
    u'Ş': 'S',
    u'Š': 'S',
    u'T': 'T',
    u'Ţ': 'T',
    u'Ť': 'T',
    u'Ŧ': 'T',
    u'V': 'V',
    u'W': 'W',
    u'Ŵ': 'W',
    u'X': 'X',
    u'Y': 'Y',
    u'Ŷ': 'Y',
    u'Z': 'Z',
    u'Ž': 'Z'
}

# If experimenting with the character sets, this is the constraint that
# must be met for efficient transformations.
assert(len(vowels) == len(consonants))

size = len(vowels)

def is_odd(number): return number % 2 != 0

def next_character(number, use_vowel_set):
    val = number % size
    rem_val = (number - val) / size
    if use_vowel_set:
        return vowels[val], False, rem_val
    else:
        return consonants[val], True, rem_val

def to_nume_inner(number):
    nume = ''
    # This was a completely arbitrary choice, but odd numbers start
    # with vowels and even numbers start with consonants.
    use_vowel_set = is_odd(number)
    while (number > 0):
        c, use_vowel_set, number = next_character(number, use_vowel_set)
        nume = nume + c
    return nume

def format_nume(nume):
    # These values should probably be constants declared at the top,
    # or, better yet, computed from `size` and 160 (number of bits in
    # an Ethereum address).
    f,m,l=8,12,9
    first, middle, last = nume[0:f].title(), nume[f:(f+m)].title(), nume[f+m:].title()
    return (first + " " + middle + " " + last).strip()

def to_nume(number):
    nume = to_nume_inner(number)
    return format_nume(nume)

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

def strip_accents(nume):
    clean_nume = ''
    for n in nume:
        clean_nume = clean_nume + lookups[n]
    return format_nume(clean_nume)

def format_segments(segments, will_strip_accents = True):
    concatenated_nume = ''.join(segments)
    if will_strip_accents:
        return strip_accents(concatenated_nume)
    else:
        return format_nume(concatenated_nume)

# Here's a `Nume` class to make consuming the relatively low-level
# methods defined above a bit easier.
class Nume:
    def __init__(self, number):
        self.number = number
        self.full_nume = [s.upper() for s in to_nume(number).split(' ')]
        self.form_index = 0

    def get_form(self, form_index = None):
        if form_index is None:
            form_index = self.form_index
        if form_index is 0:
            # 0 <=> cleaned first-name
            return format_segments(self.full_nume[0:1])
        elif form_index is 1:
            # 1 <=> cleaned first-name and last-name
            # NOTE: If one is experimenting, there is a bit of a gotcha
            # here with `format_segments(...)`, which adds spaces at
            # certain indices. We avoid strange spaces by using the
            # last-name (which is shorter that the middle-name).
            return format_segments([self.full_nume[0], self.full_nume[2]])
        elif form_index is 2:
            # 2 <=> cleaned first-name, middle-name and last-name
            return format_segments(self.full_nume)
        else:
            # * <=> accented first-name, middle-name and last-name
            return format_segments(self.full_nume, will_strip_accents = False)

    def set_form(self, form_index = None):
        if form_index is None:
            form_index = self.form_index + 1
        self.form_index = form_index

# 'MUFs,' or 'minimally unique forms' are context-dependent forms for
# numes. They depend on the other numes in the set, and are the bare
# minimum form in order for every nume-representation in the set to be
# distinct.

def get_mufs(numbers):
    numes = []
    for number in numbers:
        numes.append(Nume(number))
    nume_collection = numes
    collisions = []
    muf_numes = []
    mufs = []
    while True:
        for nume in nume_collection:
            muf = nume.get_form()
            if muf in mufs:
                other = muf_numes[mufs.index(muf)]
                mufs.remove(muf)
                muf_numes.remove(other)
                collisions.append(nume)
                collisions.append(other)
                nume.set_form()
                other.set_form()
            else:
                mufs.append(muf)
                muf_numes.append(nume)
        if len(collisions) > 0:
            nume_collection = collisions
            collisions = []
        else:
            break
    return mufs


# `randint` is the only import, and it's used for the following test.
from random import randint

TEST_SIZE = 2**16
def test(test_size = None):
    if test_size is None:
        test_size = TEST_SIZE
    numbers = []
    for i in xrange(test_size):
        numbers.append(randint(0, 2**160))
    mufs = get_mufs(numbers)
    # Assert that there are no duplicates (every MUF should be unique
    # in order to be considered a MUF).
    assert(len(set([x for x in mufs if mufs.count(x) > 1])) is 0)
    return mufs