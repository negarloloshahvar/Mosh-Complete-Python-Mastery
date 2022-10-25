from abc import ABC, abstractmethod

class UIControl(ABC):
    #define the common behaviour/methods that  we need in its derivatives/children.
    @abstractmethod
    def draw(self):
        pass

class TextBox(UIControl):
    #method
    def draw(self):
        print('TextBox')

class DropDownList(UIControl):
    def draw(self):
        print('DropDownList')

#function
def draw(controls):
    for control in controls:
        control.draw()


ddl = DropDownList()
textbox = TextBox()
# print(isinstance(ddl, UIControl))
draw([ddl, textbox])