# -*- coding: utf-8 -*-
VOWELS     = [u'A',u'À',u'Á',u'Â',u'Ä',u'Å',u'Ā',u'Ą',u'E',u'È',u'É',u'Ê',u'Ë',u'Ē',u'Ė',u'Ę',u'I',u'Ì',u'Í',u'Î',u'Ï',u'Ī',u'Ǐ',u'Į',u'O',u'Ò',u'Ó',u'Ô',u'Ö',u'Ø',u'Ō',u'Ő',u'U',u'Ù',u'Ú',u'Û',u'Ü',u'Ū',u'Ů',u'Ű']
CONSONANTS = [u'B',u'C',u'Ĉ',u'D',u'Ď',u'F',u'G',u'Ĝ',u'Ģ',u'H',u'Ĥ',u'J',u'Ĵ',u'K',u'Ķ',u'L',u'Ļ',u'M',u'N',u'Ņ',u'Ň',u'P',u'Q',u'R',u'Ŗ',u'Ř',u'S',u'Ŝ',u'Ş',u'T',u'Ť',u'Ŧ',u'V',u'W',u'Ŵ',u'X',u'Y',u'Ŷ',u'Z',u'Ž']

F,M,L=8,12,10

CLEAN='clean' # (all)
GRAVE='grave' # ` AEIOU
ACUTE='acute' # ´ AEIOU
CIRCUMFLEX='circumflex' # ^ AEIOUCGHJSWY
DIAERESIS='diaeresis' # ¨ AEIOU
RING='ring' # ° AU
CEDILLA='cedilla' # ¸ GKLNRS
OGONEK='ogonek' # AEI
STROKE='stroke' # OT
MACRON='macron' # ¯ AEIOU
DOT='dot'  # E
CARON='caron' # IDNRTZ
DOUBLE_ACUTE='double_acute' # OU

RESET='reset'
BLACK='black'
RED='red'
GREEN='green'
YELLOW='yellow'
BLUE='blue'
MAGENTA='magenta'
CYAN='cyan'
WHITE='white'

def get_color_for_character(c, accent):
    if accent is CLEAN:
        return BLACK
    if c in VOWELS:
        if accent is GRAVE:
            return MAGENTA
        if accent is ACUTE:
            return CYAN
        if accent is DIAERESIS:
            return GREEN
        if accent is MACRON:
            return YELLOW
        if accent is CIRCUMFLEX:
            return RED
        if c is 'A':
            if accent is RING:
                return BLUE
            if accent is OGONEK:
                return WHITE
        if c is 'E':
            if accent is OGONEK:
                return BLUE
            if accent is DOT:
                return WHITE
        if c is 'I':
            if accent is OGONEK:
                return BLUE
            if accent is CARON:
                return WHITE
        if c is 'O':
            if accent is STROKE:
                return BLUE
            if accent is DOUBLE_ACUTE:
                return WHITE
        if c is 'U':
            if accent is RING:
                return BLUE
            if accent is DOUBLE_ACUTE:
                return WHITE
    else: # consonant
        if accent is CIRCUMFLEX:
            return RED
        if accent is CEDILLA:
            return GREEN
        if accent is STROKE:
            return MAGENTA
        if accent is CARON:
            return WHITE
    raise Exception(c + ' ' + accent)

def get_ansi_color(color):
    from colorama import Fore, Back
    """
    Fore: BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE, RESET.
    Back: BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE, RESET.
    """
    if color is RESET:
        fore=Fore.RESET
        back=Back.RESET
    if color is BLACK:
        fore=Fore.WHITE
        back=Back.BLACK
    if color is RED:
        fore=Fore.WHITE
        back=Back.RED
    if color is GREEN:
        fore=Fore.BLACK
        back=Back.GREEN
    if color is YELLOW:
        fore=Fore.BLACK
        back=Back.YELLOW
    if color is BLUE:
        fore=Fore.WHITE
        back=Back.BLUE
    if color is MAGENTA:
        fore=Fore.WHITE
        back=Back.MAGENTA
    if color is CYAN:
        fore=Fore.WHITE
        back=Back.CYAN
    if color is WHITE:
        fore=Fore.BLACK
        back=Back.WHITE
    return fore+back

# The following is essentially a lookup table used to strip the accents
# from complete numes.
LOOKUPS = {
    # vowels
    u'A': ['A', CLEAN],
    u'À': ['A', GRAVE],
    u'Á': ['A', ACUTE],
    u'Â': ['A', CIRCUMFLEX],
    u'Ä': ['A', DIAERESIS],
    u'Å': ['A', RING],
    u'Ā': ['A', MACRON],
    u'Ą': ['A', OGONEK],
    u'E': ['E', CLEAN],
    u'È': ['E', GRAVE],
    u'É': ['E', ACUTE],
    u'Ê': ['E', CIRCUMFLEX],
    u'Ë': ['E', DIAERESIS],
    u'Ē': ['E', MACRON],
    u'Ė': ['E', DOT],
    u'Ę': ['E', OGONEK],
    u'I': ['I', CLEAN],
    u'Ì': ['I', GRAVE],
    u'Í': ['I', ACUTE],
    u'Î': ['I', CIRCUMFLEX],
    u'Ǐ': ['I', CARON],
    u'Ï': ['I', DIAERESIS],
    u'Ī': ['I', MACRON],
    u'Į': ['I', OGONEK],
    u'O': ['O', CLEAN],
    u'Ò': ['O', GRAVE],
    u'Ó': ['O', ACUTE],
    u'Ô': ['O', CIRCUMFLEX],
    u'Ö': ['O', DIAERESIS],
    u'Ø': ['O', STROKE],
    u'Ō': ['O', MACRON],
    u'Ő': ['O', DOUBLE_ACUTE],
    u'U': ['U', CLEAN],
    u'Ù': ['U', GRAVE],
    u'Ú': ['U', ACUTE],
    u'Û': ['U', CIRCUMFLEX],
    u'Ü': ['U', DIAERESIS],
    u'Ū': ['U', MACRON],
    u'Ů': ['U', RING],
    u'Ű': ['U', DOUBLE_ACUTE],
    # consonants
    u'B': ['B', CLEAN],
    u'C': ['C', CLEAN],
    u'Ĉ': ['C', CIRCUMFLEX],
    u'D': ['D', CLEAN],
    u'Ď': ['D', CARON],
    u'F': ['F', CLEAN],
    u'G': ['G', CLEAN],
    u'Ĝ': ['G', CIRCUMFLEX],
    u'Ģ': ['G', CEDILLA],
    u'H': ['H', CLEAN],
    u'Ĥ': ['H', CIRCUMFLEX],
    u'J': ['J', CLEAN],
    u'Ĵ': ['J', CIRCUMFLEX],
    u'K': ['K', CLEAN],
    u'Ķ': ['K', CEDILLA],
    u'L': ['L', CLEAN],
    u'Ļ': ['L', CEDILLA],
    u'M': ['M', CLEAN],
    u'N': ['N', CLEAN],
    u'Ņ': ['N', CEDILLA],
    u'Ň': ['N', CARON],
    u'P': ['P', CLEAN],
    u'Q': ['Q', CLEAN],
    u'R': ['R', CLEAN],
    u'Ŗ': ['R', CEDILLA],
    u'Ř': ['R', CARON],
    u'S': ['S', CLEAN],
    u'Ŝ': ['S', CIRCUMFLEX],
    u'Ş': ['S', CEDILLA],
    u'T': ['T', CLEAN],
    u'Ť': ['T', CARON],
    u'Ŧ': ['T', STROKE],
    u'V': ['V', CLEAN],
    u'W': ['W', CLEAN],
    u'Ŵ': ['W', CIRCUMFLEX],
    u'X': ['X', CLEAN],
    u'Y': ['Y', CLEAN],
    u'Ŷ': ['Y', CIRCUMFLEX],
    u'Z': ['Z', CLEAN],
    u'Ž': ['Z', CARON]
}

# If experimenting with the character sets, this is the constraint that
# must be met for efficient transformations.
assert(len(VOWELS) == len(CONSONANTS))

size = len(VOWELS)

def is_odd(number): return number % 2 != 0

def next_character(number, use_vowel_set):
    val = number % size
    rem_val = (number - val) / size
    if use_vowel_set:
        return VOWELS[val], False, rem_val
    else:
        return CONSONANTS[val], True, rem_val

def to_nume_inner(number):
    nume = ''
    # This was a completely arbitrary choice, but odd numbers start
    # with vowels and even numbers start with consonants.
    use_vowel_set = is_odd(number)
    while (number > 0):
        c, use_vowel_set, number = next_character(number, use_vowel_set)
        nume = nume + c
    return nume

def format_nume(nume, divs = None):
    # These values should probably be constants declared at the top,
    # or, better yet, computed from `size` and 160 (number of bits in
    # an Ethereum address).
    if divs is None:
        f,m,l=F,M,L
    else:
        f,m,l=divs
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
           val = VOWELS.index(c)
        except:
            try:
                val = CONSONANTS.index(c)
            except:
                pass
        number = number + (size**i * val)
    return number

def strip_accents(nume):
    clean_nume = ''
    for n in nume:
        if n is ' ':
            clean_nume = clean_nume + n
        else:
            clean_nume = clean_nume + LOOKUPS[n][0]
    return clean_nume

def format_segments(segments, will_strip_accents = True, divs = None):
    concatenated_nume = ''.join(segments)
    if will_strip_accents:
        clean_nume = strip_accents(concatenated_nume)
        return format_nume(clean_nume, divs)
    else:
        return format_nume(concatenated_nume, divs)

def format_char(c, color):
    ansi_color = get_ansi_color(color)
    return ansi_color + ' ' + c + ' '

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
            # 1 <=> cleaned first-name and last-initial
            return format_segments([self.full_nume[0], self.full_nume[2][0]])
        elif form_index is 2:
            # 1 <=> cleaned first-name and last-name
            # NOTE: If one is experimenting, there is a bit of a gotcha
            # here with `format_segments(...)`, which adds spaces at
            # certain indices. We avoid strange spaces by using the
            # last-name (which is shorter that the middle-name).
            return format_segments([self.full_nume[0], self.full_nume[2]])
        elif form_index is 3:
            # 2 <=> cleaned first-name, middle-name, and last-name
            return format_segments([self.full_nume[0], self.full_nume[1][0], self.full_nume[2]], will_strip_accents = True, divs=(F,1,L))
        elif form_index is 4:
            # 2 <=> cleaned first-name, middle-name, and last-name
            return format_segments(self.full_nume)
        else:
            # * <=> accented first-name, middle-name, and last-name
            return format_segments(self.full_nume, will_strip_accents = False)

    def set_form(self, form_index = None):
        if form_index is None:
            form_index = self.form_index + 1
        self.form_index = form_index

    def print_color(self):
        # TODO: May need below for Windows:
        # from colorama import init
        raw_nume = to_nume_inner(self.number)
        nume = ''
        for i,r in enumerate(raw_nume):
            char_info = LOOKUPS[r]
            character = char_info[0]
            color = get_color_for_character(character, char_info[1])
            if i is not 0:
                if i is not F and i is not (F+M):
                    character = character.lower()
                else:
                    nume = nume + format_char(' ', RESET)
            nume = nume + format_char(character, color)
        nume = nume + get_ansi_color(RESET)
        print(nume)

# 'Minimally unique forms' (or 'MUFs') are context-dependent forms for
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


# `randint` is the only import and it's used for the following test.
from random import randint

TEST_SIZE = 2**16
# NOTE: This test does not preserve the order of the elements. It
# should probably be updated to return tuples of numes and numbers
# (or just the `Nume` instances).
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