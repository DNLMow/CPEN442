"""
This script provides analysis to the ciphertext.
"""
import fileinput
import collections
import operator

ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def main():
    # parse command line options
    frequency_dict = collections.OrderedDict() 
    bigram_dict = {}
    trigram_dict = {}
    quadgram_dict = {}
    pentagram_dict = {}
    counter = 0

    for key in ALPHABET:
        frequency_dict[key] = 0

    for line in fileinput.input():
        print('Length of ciphertext is:' + str(len(line) - 1))
        for key in line:

            if key == '\n':
                continue

            try:
                bigram_text = line[counter] + line[counter + 1]
                if bigram_text in bigram_dict:
                    bigram_dict[bigram_text] += 1
                else:
                    bigram_dict[bigram_text] = 1
            except:
                pass

            try:
                trigram_text = (line[counter] + line[counter + 1] +
                               line[counter + 2])
                if trigram_text in trigram_dict:
                    trigram_dict[trigram_text] += 1
                else:
                    trigram_dict[trigram_text] = 1
            except:
                pass

            try:
                quadgram_text = (line[counter] + line[counter + 1] +
                                line[counter + 2] + line[counter + 3])
                if quadgram_text in quadgram_dict:
                    quadgram_dict[quadgram_text] += 1
                else:
                    quadgram_dict[quadgram_text] = 1
            except:
                pass

            try:
                pentagram_text = (line[counter] + line[counter + 1] +
                                 line[counter + 2] + line[counter + 3] +
                                 line[counter + 4])
                if pentagram_text in pentagram_dict:
                    pentagram_dict[pentagram_text] += 1
                else:
                    pentagram_dict[pentagram_text] = 1
            except:
                pass
            
            counter += 1

            frequency_dict[key] += 1
            
    sorted_bigram = sorted(bigram_dict.items(), key=operator.itemgetter(1), reverse=True)
    sorted_trigram = sorted(trigram_dict.items(), key=operator.itemgetter(1), reverse=True)
    sorted_quadgram = sorted(quadgram_dict.items(), key=operator.itemgetter(1), reverse=True)
    sorted_pentagram = sorted(pentagram_dict.items(), key=operator.itemgetter(1), reverse=True)

    print('frequency analysis:')
    print(frequency_dict)

    print('bigram frequency:')
    print(sorted_bigram)
    
    print('trigram frequency:')
    print(sorted_trigram)

    print('quadgram frequency:')
    print(sorted_quadgram)

    print('pentagram frequency:')
    print(sorted_pentagram)

if __name__ == "__main__":
    main()
