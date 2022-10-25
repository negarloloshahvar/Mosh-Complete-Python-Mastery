# If it walks like a duck and quacks like a duck ===> It is duck!

class TextBox():
    #method
    def draw(self):
        print('TextBox')

class DropDownList():
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