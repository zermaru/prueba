#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 21 19:48:29 2022

@author: User
"""
#     script           clase        alias
from cal_class import CalculatorI as CL

in_a = 13
in_b = 7

classObj = CL(input_a=in_a, input_b=in_b)

result01 = classObj.add()
result02 = classObj.floor_div()

print(f'El resultado de la suma es = {result01}')
print(f'El resultado de la suma es = {result02}')