import unittest

digits = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
digits_as_words = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
max_digit_length = max(len(word) for word in digits_as_words)

def find_digit_from_word(digit_word):
   return str(digits_as_words.index(digit_word) + 1)

def first_and_last_digit(digit_tuple_1, digit_tuple_2):
   if digit_tuple_1 == None:
      return digit_tuple_2
   if digit_tuple_2 == None:
      return digit_tuple_1
      
   (digit, li1, ri1) = digit_tuple_1
   (digit, li2, ri2) = digit_tuple_2
   return (digit, min(li1, li2), max(ri1, ri2))

def read_calibration_line(line):
    matching_digits = [(digit, line.find(digit), line.rfind(digit)) 
                       for digit in digits if digit in line]
    found_digits_dict = {digit[0]: digit for digit in matching_digits}

    matching_digits_words = [(find_digit_from_word(digit), line.find(digit), line.rfind(digit)) 
                             for digit in digits_as_words if digit in line]
    found_digits_words_dict = {digit[0]: digit for digit in matching_digits_words}

    found_digits = {k: first_and_last_digit(found_digits_dict.get(k), found_digits_words_dict.get(k))
                         for k in set(found_digits_dict) | set(found_digits_words_dict)}

    if not found_digits:
        raise ValueError(f"Invalid line provided: {line}")

    first_digit = min(found_digits.values(), key=lambda x: x[1])[0]
    last_digit = max(found_digits.values(), key=lambda x: x[2])[0]

    return int(f"{first_digit}{last_digit}")

def read_calibration(calibration_data):
    lines = calibration_data.splitlines()
    return sum([read_calibration_line(line) for line in lines if line.strip() != ""])

class TestReadCalibration(unittest.TestCase):
    
  def test_read_calibration_line(self):
      self.assertEqual(read_calibration_line('1213twonem'), 11)
      self.assertEqual(read_calibration_line('1abc2'), 12)
      self.assertEqual(read_calibration_line('pqr3stu8vwx'), 38)
      self.assertEqual(read_calibration_line('a1b2c3d4e5f'), 15)
      self.assertEqual(read_calibration_line('treb7uchet'), 77)
      self.assertEqual(read_calibration_line('two1nine'), 29)
      self.assertEqual(read_calibration_line('eightwothree'), 83)
      self.assertEqual(read_calibration_line('abcone2threexyz'), 13)
      self.assertEqual(read_calibration_line('xtwone3four'), 24)
      self.assertEqual(read_calibration_line('4nineeightseven2'), 42)
      self.assertEqual(read_calibration_line('zoneight234'), 14)
      self.assertEqual(read_calibration_line('7pqrstsixteen'), 76)
      self.assertEqual(read_calibration_line('784dxxcpszbzkdlsrgnnqfsixone7twonemvh'), 71)

  def test_read_calibration(self):
      calibration_data = '''1abc2
                            pqr3stu8vwx
                            a1b2c3d4e5f
                            treb7uchet'''

      result = read_calibration(calibration_data)

      self.assertEqual(result, 142)

  def test_read_calibration_improved(self):
      calibration_data = '''two1nine
                            eightwothree
                            abcone2threexyz
                            xtwone3four
                            4nineeightseven2
                            zoneight234
                            7pqrstsixteen'''

      result = read_calibration(calibration_data)

      self.assertEqual(result, 281)

if __name__ == '__main__':
  # unittest.main()

  with open('inputs/day1.txt', 'r') as file:
     content = file.read()

  calibration = read_calibration(content)
  print(f"Calibration is {calibration}")
