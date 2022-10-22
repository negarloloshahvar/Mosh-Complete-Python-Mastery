class BlogTags:
    def __init__(self):
        self.__tags = {}

    def show(self):
        print(self.__tags)

    def add(self, tag):
       self.__tags[tag.lower()] = self.__tags.get(tag.lower(), 0) + 1

    def __getitem__(self, tag):
        return self.__tags.get(tag.lower(), 0)

    def __setitem__(self, tag, count):
        self.__tags[tag.lower()] = count

    def __len__(self):
        return len(self.__tags)

    def __iter__(self):
        return iter(self.__tags)

cloud = BlogTags()

cloud.add('Python')
cloud.add('python')
cloud.add('python')
cloud.add('python')
cloud.add('java')
cloud.add('java')
cloud.add('css')
cloud.add('javascript')
cloud['html'] = 10

cloud.show()
print(cloud['PYTHON'])

