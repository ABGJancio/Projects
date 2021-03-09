'''
print("Witaj, ten program pomoże Ci sprawdzić czy jesteś pełnoletni/a")
adult = None
sex = input("Podaj proszę swoją płeć [M/K]: ")
   age = int(input("Twój wiek? "))
    adult = age >= 18
elif sex == 'K':
    print("Kobiet o wiek się nie pyta, więc zrobię to delikatnie.")
    over18_yesno = input("Czy miałaś już osiemnastkę? [T/N]?")
    adult = (over18_yesno == 'T')
else:
    print("Nie ma takiej płci!")
    exit(1)
print("Już wiem. Twoja pełnoletniość w boolean to %s" % str(adult))
'''

import sys
import logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(message)s', filename="sex_loggs.log")

def print_maturity(age):
    if age >= 18:
        logging.info("You are an adult")
    else:
        logging.info("You are a kiddo!")

if __name__ == "__main__":
    logging.debug("The program was called with this parameters %s" % sys.argv[1:])
    logging.debug("First parameter is %s" % sys.argv[1])
    age = int(sys.argv[1])
    print_maturity(age)

