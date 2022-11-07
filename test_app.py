from app import enterInput
from tud_test_base import set_keyboard_input, get_display_output

def test_1():
      set_keyboard_input(["Manila","Q"])

      enterInput()

      output = get_display_output()

      assert output == ['\033[1m' + "\nStarting Location: " + '\033[0m','\033[1m' + "Destination: "  + '\033[0m',"\nProgram Terminated."]