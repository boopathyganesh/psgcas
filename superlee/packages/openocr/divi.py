import string
def num(inputString):
 value =set(string.ascii_lowercase)
 print(set(inputString.lower()) >= value)
inputString = input("Type a Sentence: ")
num(inputString)
