# nume: number name scheme

**v0.9.0**

For too long have we had to communicate base-58 or hexadecimal numbers! And the auction-based name systems and first-come-first-serve name systems are not ideal either. This repo contains a new class of encoding scheme: _pronounceable_ (more-or-less) encodings.

The basic idea is the inversion of the usual approach to account names: force names upon the users, much like how they have gotten their own names.

The scheme implemented in less than 50 lines of python is a simple special case: two character sets of equal order. One set contains vowels and the other set contains consonants. Simply take a character from either set in an alternating fashion. With our character set selections, we have essentially base-48.

### Example
```python
>>> nume = to_nume(0x18b676bae1e0d99c03c63114fb116ef9d976c13e)
>>> print nume
Jàňèdűřů Lãbôťĩqůwąqê Þŏķĩwįbec
>>> print hex(to_number(nume))
0x18b676bae1e0d99c03c63114fb116ef9d976c13e
```

### Possible Use for Accounts:
Since numes can be split up into three segments  (first, middle, last), an account could be displayed initially with only the first segment. The third segment (and then the second segment, if necessary) can be displayed as disambiguator.

This scheme could make accounts more 'searchable.' A system could likely be implemented to result in an experience similar to how, in real life, you can tell someone your account name on a legacy social media platform, they search for it and show you the results,and you can point at the correct one.

### TODOs:
* Python3 support

#### Non-normative notes:
* My earlier attempts at pronounceable encoding schemes envisioned 'asymmetrical' encoding, where the two character sets used were not isomorphic to eachother. While an interesting algorithm/formula for determining the number of elements per 'digit' was discovered, it was not that useful and no efficient conversion algorithm was discovered. Had such an algorithm been discovered, the next progression would have been dynamic character sets that would permit consecutive consonants and vowels if they were part of common sequences (such as 'tr', 'th', and so on). Despair took over and I implemented the special case on my flight back from Prague. — {;
