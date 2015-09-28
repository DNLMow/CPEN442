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
    fairplay_str = ""
    counter = 0
    fairplay_str_counter = 0

    for key in ALPHABET:
        frequency_dict[key] = 0

    for line in fileinput.input():
        print('Length of ciphertext is:' + str(len(line) - 1))
        for key in line:
            
            if fairplay_str_counter != 0 and fairplay_str_counter % 2 == 0:
                fairplay_str += ' '

            fairplay_str += key

            fairplay_str_counter += 1

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
            
            counter += 2

            frequency_dict[key] += 1
            
    sorted_bigram = sorted(bigram_dict.items(), key=operator.itemgetter(1), reverse=True)

    print('frequency analysis:')
    print(frequency_dict)

    print('bigram frequency:')
    print(sorted_bigram)

    print('better display for fairplay ciphertext:')
    print(fairplay_str)

if __name__ == "__main__":
    main()
