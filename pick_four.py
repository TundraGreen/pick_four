#!/usr/local/bin/python3

# pick_four.py
# @2022 William H. Prescott

# Given:
# a collection of letters
# a required letter
# a collection of vowels

# Output:
# a list of all four letter combinations drawn from the letters
# where each member of the list includes the required letter
# and at least one of the vowels

# Motivation:
# Usefol for the SpellingBee game.


# ***********************************************
def main():
  [letters, required, vowels] = read_letters()
  words = generate_word_list(letters, required, vowels)
  print_results(words)

# ***********************************************
def generate_word_list(letters, required, vowels):
  words = []
  for position_0 in letters:
    for position_1 in letters:
      for position_2 in letters:
        for position_3 in letters:
          answer = position_0 + position_1 + position_2 + position_3
          if required[0] in answer:
            print_flag = False
            for vowel in vowels:
              if vowel in answer:
                print_flag = True
                break
            if print_flag:
              words.append(answer)
  return words

# ***********************************************
def print_results(words):
  out_string = ""
  series = 0
  while series < len(words) + 15:
    for index in range(0, 15):
      if series + index >= len(words):
        break
      out_string += words[series + index] + "\t"
    out_string = out_string[0:len(out_string) - 1] + "\n"
    series += 15

  print(out_string)
  print('Count: %d' % len(words))

# ***********************************************
def read_letters():
  letters = convert_string_to_list(input( 'Enter letters (e.g. abcdefg):     '))
  required = convert_string_to_list(input('Enter required letter (e.g. c):  '))
  if len(required) != 1:
    exit('Required letter required!')
  vowels = convert_string_to_list(input(  'Enter vowels (e.g. ae):          '))
  print()
  print('Letters: %s' % letters)
  print('Required: %s' % required)
  print('Vowels: %s' % vowels)
  return [letters, required, vowels]

# ***********************************************
def convert_string_to_list(input_string):
  output_list = []
  for letter in input_string:
    output_list.append(letter)
  return output_list

# ***********************************************
main()


