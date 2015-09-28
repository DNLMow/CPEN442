import binascii
import random
import string


def main():
    input_sample = string.lowercase + string.digits
    counter = 0
    student_id = 'F126A6B25737F666ED81A8C360135CCC'
    input_str1 = (''.join(random.sample(input_sample, student_id)))
    while 1 == 1:
            x = 32
            input_str2 = (''.join(random.sample(input_sample, x)))

            if (counter % 320000) == 0:
                print(str(counter) + " of 320000 rotation passed.")

            counter += 1

            if (binascii.crc32(input_str1) == binascii.crc32(input_str2) and
               input_str1 != input_str2):
                print("Collision found:")
                print("String1: " + input_str1)
                print("String2: " + input_str2)

if __name__ == "__main__":
    main()
