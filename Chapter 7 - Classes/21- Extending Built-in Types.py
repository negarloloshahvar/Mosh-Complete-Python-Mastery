class Text(str):
    def duplicate(self):
        return self + self

class TrackableList(list):
    def append(self, object):
        print('Append called.')
        super().append(object)


text = Text('Negar')
print(text.duplicate())

list = TrackableList()
list.append('1')
print(list)