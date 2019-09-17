ROLLER_ONE = ['E','K','M','F','L','G','D','Q','V','Z','N','T','O','W','Y','H','X','U','S','P','A','I','B','R','C','J']	
ROLLER_TWO = ['A','J','D','K','S','I','R','U','X','B','L','H','W','T','M','C','Q','G','Z','N','P','Y','F','V','O','E']	
ROLLER_THEREE = ['B','D','F','H','J','L','C','P','R','T','X','V','Z','N','Y','E','I','W','G','A','K','M','U','S','Q','O']	
ROLLER_FOUR = ['E','S','O','V','P','Z','J','A','Y','Q','U','I','R','H','X','L','N','F','T','G','K','D','C','M','W','B']	
ROLLER_FIVE = ['V','Z','B','R','G','I','T','Y','U','P','S','D','N','H','L','X','A','W','M','J','Q','O','F','E','C','K']
UKW_B = ['Y','R','U','H','Q','S','L','D','P','X','N','G','O','K','M','I','E','B','F','Z','C','W','V','J','A','T']
DEFAULT = ['ABCDEFGHIJKLMNOPQRSTUVWXYZ']

def reflector(list, n):
  return list[n]

def roller(ROLLER_LIST, start, turn, in_out, input):
  index = (start + turn) % 26
  if in_out:
    return ROLLER_LIST[index]
  else:
    return DEFAULT[ROLLER_LIST.find(input)]

def main():
  print('result')

if __name__ == '__main__':
    main()
