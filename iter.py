
class ToDo(object):

    _list = []

    def __init__(self, *args):
        self._list.extend(args)

    def __len__(self):
        return len(self._list)

    def __iter__(self):
        for it in self._list:
            yield "Item: {}".format(it)


todo = ToDo('go to work', 'buy new notebook', 'pay bills')
print("Total:{}".format(len(todo)))

# Iterate our object like a boss :)
for item in todo:
    print(item)
