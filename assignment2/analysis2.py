"""
This script provides analysis to the ciphertext.
"""
import fileinput
import collections
import operator

ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
COMMA_CONST = 'WHID'

def main():
    # parse command line options
    frequency_dict = collections.OrderedDict() 
    bigram_dict = {}
    quadgram_dict = {}
    hexagram_dict = {}
    comma_list = set()
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
            
            try:
                quadgram_text = (line[counter] + line[counter + 1] +
                                 line[counter + 2] + line[counter + 3])
                if quadgram_text == COMMA_CONST:
                    comma_set_text = (line[counter - 2] + line[counter - 1] + 
                                      line[counter] + line[counter + 1] +
                                      line[counter + 2] + line[counter + 3])
                    comma_list.add(comma_set_text)
                if quadgram_text in quadgram_dict:
                    quadgram_dict[quadgram_text] += 1
                else:
                    quadgram_dict[quadgram_text] = 1
            except:
                pass

            try:
                hexagram_text = (line[counter] + line[counter + 1] +
                                 line[counter + 2] + line[counter + 3] +
                                 line[counter + 4] + line[counter + 5])
                if hexagram_text in hexagram_dict:
                    hexagram_dict[hexagram_text] += 1
                else:
                    hexagram_dict[hexagram_text] = 1
            except:
                pass

            counter += 2

            frequency_dict[key] += 1
            
    sorted_bigram = sorted(bigram_dict.items(), key=operator.itemgetter(1), reverse=True)
    sorted_quadgram = sorted(quadgram_dict.items(), key=operator.itemgetter(1), reverse=True)
    sorted_hexagram = sorted(hexagram_dict.items(), key=operator.itemgetter(1), reverse=True)

    print('frequency analysis:')
    print(frequency_dict)

    print('bigram frequency:')
    print(sorted_bigram)

    print('quadgram frequency:')
    print(sorted_quadgram)

    print('hexagram frequency:')
    print(sorted_hexagram)

    print('better display for fairplay ciphertext:')
    print(fairplay_str)

    print('list for word "comma":')
    print(comma_list)

if __name__ == "__main__":
    main()
