
class ToDo(object):

    _list = []

    def __init__(self, *args):
        self._list.extend(args)

    def __len__(self):
        return len(self._list)


todo = ToDo('go to work', 'buy new notebook', 'pay bills')
print("Total:{}".format(len(todo)))

