
class Database(object):

    _db = {
        'foo': 'bar'
    }

    def __getitem__(self, item):
        return self._db[item]


db = Database()

print(db['foo'])  # Will return `bar`
