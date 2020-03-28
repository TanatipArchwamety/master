#!/bin/python

import unittest

class Number:
    def int_to_Roman(self, num):


        #Ref: https://en.wikipedia.org/wiki/Roman_numerals
        #Symbol	I	V	X	L	C	D	M
        #Value	1	5	10	50	100	500	1,000


        """
        #Straight algorithm
        roman_dict= {   "I" : 1,
                        "V" : 5,
                        "X" : 10,
                        "L" : 50,
                        "C" : 100,
                        "D" : 500,
                        "M" : 1000}

        result =""

        while num >= 1000:
            result += "M"
            num -= 1000

        while num >= 900:
            result += "CM"
            num -= 900

        while num >= 500:
            result += "D"
            num -= 500

        while num >= 400:
            result += "CD"
            num -= 400

        while num >= 100:
            result += "C"
            num -= 100

        while num >= 90:
            result += "XC"
            num -= 90

        while num >= 50:
            result += "L"
            num -= 50

        while num >= 40:
            result += "XL"
            num -= 40

        while num >= 10:
            result += "X"
            num -= 10

        if num == 9: result += "IX"
        if num == 5: result += "V"
        if num == 4: result += "IV"
        if num == 1: result += "I"

        return result
        """

        #Shorten code
        base_num = num
        roman_dict= [   ("M"  , 1000),
                        ("CM" , 900),
                        ("D"  , 500),
                        ("CD" , 400),
                        ("C"  , 100),
                        ("XC" , 90),
                        ("L"  , 50),
                        ("XL" , 40),
                        ("X"  , 10),
                        ("IX" , 9),
                        ("V"  , 5),
                        ("IV" , 4),
                        ("I"  , 1)    ]

        result=""
        for rd in roman_dict:
            for i in range(num // rd[1]):
                result += rd[0]
                num -= rd[1]
        return result
        return "%s converted to %s" % (base_num, result)

class TestRomanMethods(unittest.TestCase):

    def test_1digit(self):
        self.assertEqual(Number().int_to_Roman(1)      , 'I')
        self.assertEqual(Number().int_to_Roman(2)      , 'II')
        self.assertEqual(Number().int_to_Roman(3)      , 'III')
        self.assertEqual(Number().int_to_Roman(4)      , 'IV')
        self.assertEqual(Number().int_to_Roman(5)      , 'V')
        self.assertEqual(Number().int_to_Roman(6)      , 'VI')
        self.assertEqual(Number().int_to_Roman(7)      , 'VII')
        self.assertEqual(Number().int_to_Roman(8)      , 'VIII')
        self.assertEqual(Number().int_to_Roman(9)      , 'IX')

    def test_2digit(self):
        self.assertEqual(Number().int_to_Roman(39)      , 'XXXIX')
        self.assertEqual(Number().int_to_Roman(40)      , 'XL')
        self.assertEqual(Number().int_to_Roman(90)      , 'XC')

    def test_3digit(self):
        self.assertEqual(Number().int_to_Roman(246)     , 'CCXLVI')
        self.assertEqual(Number().int_to_Roman(789)     , 'DCCLXXXIX')

    def test_4digit(self):
        self.assertEqual(Number().int_to_Roman(2421)    , 'MMCDXXI')
        self.assertEqual(Number().int_to_Roman(1009)    , 'MIX')
        self.assertEqual(Number().int_to_Roman(1066)    , 'MLXVI')
        self.assertEqual(Number().int_to_Roman(2020)    , 'MMXX')
        self.assertEqual(Number().int_to_Roman(3999)    , 'MMMCMXCIX')

if __name__ == '__main__':

    suite = unittest.TestLoader().loadTestsFromTestCase(TestRomanMethods)
    unittest.TextTestRunner(verbosity=2).run(suite)


    input_list = [39, 246, 789, 2421, 1009, 1066, 2020, 3999]
    for input in input_list:
        print("%d converted into %s" % (input, Number().int_to_Roman(input)))
