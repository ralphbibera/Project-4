from app import enterInput
from tud_test_base import set_keyboard_input, get_display_output

def test_1():
      set_keyboard_input(["Manila","Q"])

      enterInput()

      output = get_display_output()

      assert output == ["Starting Location: Manila","Destination: Q","Program Terminated."]


def test_2():
      assert 0 == 1

