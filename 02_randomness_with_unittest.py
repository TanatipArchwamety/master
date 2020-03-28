#!/bin/python
import random
import unittest

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

    def sorted_pick_set(self):
        return sorted(self.pick_set())


class TestLottery(unittest.TestCase):
    test_times = 1000

    def test_amount(self):
        for i in range(self.test_times):
            self.assertEqual(len(Lottery(10).sorted_pick_set()) , 10)

    def test_duplicate(self):
        for i in range(self.test_times):
            self.assertEqual(len(Lottery(10).sorted_pick_set()) , len(set(Lottery(10).sorted_pick_set())))

    def test_sorted(self):
        for i in range(self.test_times):
            pick_list = Lottery(10).sorted_pick_set()
            self.assertEqual(pick_list , sorted(pick_list))

    def test_range(self):
        for i in range(self.test_times):
            self.assertEqual([i for i in Lottery(10).sorted_pick_set() if i <= 0] , [])
            self.assertEqual([i for i in Lottery(10).sorted_pick_set() if i > 50] , [])

if __name__ == '__main__':

    suite = unittest.TestLoader().loadTestsFromTestCase(TestLottery)
    unittest.TextTestRunner(verbosity=2).run(suite)


    random_amount=10

    print("creating 50-ball Lottery, and pick %d times" % random_amount)
    Lottery  = Lottery(random_amount)
    print("Now, we've got : %s" % str(Lottery.sorted_pick_set()))