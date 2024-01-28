import unittest
import examples

class TestExamples(unittest.TestCase):
  def test_expected_say_hi(self):
    name   = "Lucas"
    result = examples.say_hi(name)

    self.assertEqual(result, f"hi, #{name}")

if __name__ == "__main__":
  unittest.main()
