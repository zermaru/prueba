#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 21 19:31:37 2022

@author: User
"""

class CalculatorI():
    '''
    This class is a simple calculator with:
        * Addition
        * Subtraction
        * Multiplication
        * Division
        * Floor division
    '''

    def __init__(self, input_a: float, input_b: float) -> None:

        self.num_a = input_a
        self.num_b = input_b

    def add(self):

        num_a = self.num_a
        num_b = self.num_b

        result = num_a + num_b

        return result

    def floor_div(self):

        result = self.num_a // self.num_b

        return result
