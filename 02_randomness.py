#!/bin/python
import random


class Lottery(object):
    max_ball = 50

    def __init__(self, random_amount):
        if isinstance(random_amount, int):
            self.random_amount = random_amount
        else:
            raise TypeError("random_amount must be interger type")

    def pick(self):
        return random.randrange(1, self.max_ball+1)

    def pick_set(self):
        return random.sample(range(1, self.max_ball+1), self.random_amount)

    """
    def pick_set(self):#nodup, bad performance
        result = []
        while len(result) < self.random_amount:
            tmp = self.pick()
            if tmp not in result: result.append(tmp)
        return result 
    """

    def sorted_pick_set(self):
        return sorted(self.pick_set())


if __name__ == '__main__':

    random_amount=10

    print("creating 50-ball Lottery with %d pick time" % random_amount)
    Lottery  = Lottery(random_amount)
    print("Now, we pick : %s" % str(Lottery.sorted_pick_set()))