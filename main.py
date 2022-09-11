
nested_list = [
    ['a', 'b', 'c'],
    ['d', 'e', 'f', 'h', False],
    [1, 2, None],
]

# Задание 1


class FlatIterator:
    def __init__(self, some_objects):
            self.some_objects = some_objects
            self.current = 0
            self.next = 0

    def to_start(self):
        self.current = 0
        self.next = 0

    def to_current(self, value, values):
            self.current = value
            self.next = values

    def __iter__(self):
        return self

    def __next__(self):
        while self.current < len(self.some_objects):
            if self.next < len(self.some_objects[self.current]):
                result = self.some_objects[self.current][self.next]
                self.next += 1
                return result
            self.current += 1
            self.next = 0
        raise StopIteration


# Задание 2


def flat_generator(nested_list):
    start = 0
    next = 0
    while start < len(nested_list):
        while next < len(nested_list[start]):
            yield nested_list[start][next]
            next += 1
        next = 0
        start += 1


#Задание №4


def list_generator(list_):
    for item in list_:
        if type(item) == list:
           for item in list_generator(item):
               yield item
        elif type(item) != list:
            yield item



if __name__ == '__main__':
    print('Задание №1')
    for item in FlatIterator(nested_list):
        print(item)
    flat_list = [item for item in FlatIterator(nested_list)]
    print(flat_list)
    print('Задание №2')
    for item in flat_generator(nested_list):
        print(item)
    print('Задание №4')
    for item in list_generator(nested_list):
        print(item)



