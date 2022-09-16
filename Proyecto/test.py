from utils.main import isValidInput

tests = [
  isValidInput('sadsadsa', 10) == False,
  isValidInput(23, 12) == False,
  isValidInput('12', 23) == True,
  isValidInput('12.3', 1) == False,
  isValidInput('-10', 10) == False,
]

for testResult in tests:
  print('👌 passed'if testResult else '❎ not passed')




