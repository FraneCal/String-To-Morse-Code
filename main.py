from morse_code import MORSE_CODE_DICT

def to_morse(string):
  """Function takes a string as input and returns a space-separated string of the Morse code equivalent of the input string. 
  Space between the words is separated by '/' symbol."""
  alphabet_solution = []
  for letter in string:
    #The space between words is separated by the '/' symbol
    if letter == ' ':
      alphabet_solution.append('/')
    else:
      morse_code = MORSE_CODE_DICT.get(letter)
      alphabet_solution.append(morse_code)
  return ' '.join(alphabet_solution)


user_input = input('Enter a word you want to convert to Morse code: ').upper()
