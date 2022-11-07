from trial import enterInput,checkInput
from tud_test_base import set_keyboard_input, get_display_output

def test_1():
      set_keyboard_input(["Manila","Q"])

      enterInput()

      output = get_display_output()
      assert output == ["Starting Location: ","Destination: "]


def test_2():
      output = checkInput("quit", "q")
      
      assert output == "EXIT"

def test_3():
      output = checkInput("222", "q")
      
      assert output == "EXIT"

def test_3():
      output = checkInput("222", "123")
      
      assert output == "NUMERIC"
      




