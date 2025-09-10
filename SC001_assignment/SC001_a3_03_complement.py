"""
File: complement.py
Name: Sanny Lin
----------------------------
This program uses string manipulation to
tackle a real world problem - finding the
complement strand of a DNA sequence.
THe program provides different DNA sequence as
a python string that is case-sensitive.
Your job is to output the complement of them.
"""


def main():
    """
    function: reply the complement strand of the inputted DNA sequence
    """
    print(build_complement('ATC'))
    print(build_complement(''))
    print(build_complement('ATGCAT'))
    print(build_complement('GCTATAC'))


def build_complement(dna):
    """
    :param dna: str, inputted DNA sequence
    :return result: str, which is the string of the complement strand of the inputted DNA sequence
                    regulation: "A" <-> "T" ; "C" <-> "G"
    * if no inputted DNA sequence: print "DNA strand is missing."
    """
    if dna == '':
        return 'DNA strand is missing.'
    else:
        result = ''
        for i in range(len(dna)):
            if dna[i] == 'A':
                result += 'T'
            elif dna[i] == 'T':
                result += 'A'
            elif dna[i] == 'C':
                result += 'G'
            elif dna[i] == 'G':
                result += 'C'
    return result


if __name__ == '__main__':
    main()
