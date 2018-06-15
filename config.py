#!/usr/bin/python
# -*- coding: UTF-8 -*-

# condition = '(![(NSString *)[[NSThread callStackSymbols] description] containsString:@"test1"])&&(![(NSString *)[[NSThread callStackSymbols] description] containsString:@"test2"])'

condition = '1'
# 忽略 C++ 的异常
IGNORE_CXX_COUNT = 5
IGNORE_CXX_CONDITION = condition


# 忽略 OC 的异常
IGNORE_OC_COUNT = 1
IGNORE_OC_CONDITION = condition
