#!/usr/bin/python
# -*- coding: UTF-8 -*-

import lldb

import imp
import os


def __lldb_init_module(debugger, dict):
    filePath = os.path.realpath(__file__)
    lldbHelperDir = os.path.dirname(filePath)

    for file in os.listdir(lldbHelperDir):
        fileName, fileExtension = os.path.splitext(file)

        # 场景：引入第三方库导致异常被抛出，第三方库内部又把异常进行了捕获，导致不会触发crash
        # Xcode提供的异常断点，仍然会因为上述场景触发断点，导致时间上面的浪费
        # 下面的逻辑，可以根据用户在 config.py 里面的配置，自动忽略前 n 次的异常抛出
        if fileName == 'config' and fileExtension == '.py':
            module = imp.load_source(
                fileName, os.path.join(lldbHelperDir, file))
            print(module)

            if hasattr(module, 'IGNORE_CXX_COUNT') and hasattr(module, 'IGNORE_CXX_CONDITION'):
                addBreakpoint('__cxa_throw', module.IGNORE_CXX_COUNT,
                              module.IGNORE_CXX_CONDITION)
            if hasattr(module, 'IGNORE_OC_COUNT') and hasattr(module, 'IGNORE_OC_CONDITION'):
                addBreakpoint('objc_exception_throw',
                              module.IGNORE_OC_COUNT, module.IGNORE_OC_CONDITION)


def addBreakpoint(name, ignoreCount, condition):
    lldb.debugger.HandleCommand(
        'br set -n {} -i {} -c \'{}\''.format(name, ignoreCount, condition))
