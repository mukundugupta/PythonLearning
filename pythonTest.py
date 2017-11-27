#!/usr/bin/env python

import sys
import re
from urlparse import urlparse
import json
import os
import threading
import time
from threading import Thread



#data types in python
print "Variables in python : "
int_value = 10
float_value = 10.10
string_value = 'This is string '
list_arr = [1,2,3,4,5,6,7,8,9,10,'ac']
dict_val = {'test' : 1 , 'DEV' : 2 , 'both' : 3}
tup_val = (1,2,3,{'abc': 1},5)


print type(int_value) , ' not mutable'
print type(float_value) , ' not mutable'
print type(string_value) , ' not mutable'
print type(list_arr) , ' mutable'
print type(dict_val) , ' mutable'
print type(tup_val) , ' not mutable'

print int_value
print float_value
print string_value
