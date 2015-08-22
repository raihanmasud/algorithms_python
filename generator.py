__author__ = 'raihan'


def gen_iterator(items):
    for item in items:
        yield item


#test generator
items = [x for x in range(1, 10) if x % 2 == 0 ]
print(items)
it = gen_iterator(items)
print(next(it))
