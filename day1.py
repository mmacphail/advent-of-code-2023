from itertools import groupby
import unittest

digits = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
digits_as_words = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

digits_representations = digits_as_words + digits

def numeric_representation(digit):
   return digit if digit in digits else str(digits_as_words.index(digit) + 1)

def find_first_and_last_digit(digit, locations):
   first_location = min(locations, key=lambda x: x[1])[1]
   last_location = max(locations, key=lambda x: x[2])[2]
   return (digit, first_location, last_location)

def read_calibration_line(line):
    print(line)

    matching_digits = [(numeric_representation(digit), line.find(digit), line.rfind(digit))
                       for digit in digits_representations if digit in line]

    matching_digits.sort(key=lambda x: x[0])

    found_digits = {digit: find_first_and_last_digit(digit, list(locations))
                    for digit, locations in groupby(matching_digits, key=lambda x: x[0])}

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
  unittest.main()

  with open('inputs/day1.txt', 'r') as file:
     content = file.read()

  calibration = read_calibration(content)
  print(f"Calibration is {calibration}")
