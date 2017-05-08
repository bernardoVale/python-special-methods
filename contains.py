
class ToDo(object):

    _list = []

    def __init__(self, *args):
        self._list.extend(args)

    def __len__(self):
        return len(self._list)

    def __iter__(self):
        for it in self._list:
            yield "Item: {}".format(it)

    def __contains__(self, item):
        return [True for x in self._list if x == item]


todo = ToDo('go to work', 'buy new notebook', 'pay bills')
print("Total:{}".format(len(todo)))

if 'go to work' in todo:
    print("Gotta go to work =)")
