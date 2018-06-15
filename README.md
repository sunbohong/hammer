# hammer

Set the number of times exception-throw is skipped before stopping

Set the contition fro exception-throw breakpoints 

# Why this？

* Forget add the exception breakpoints for new project ?

* Some exceptions in the third party or system library throw a exceptions and catch the exceptions(Which break the workflow) ?

* 新项目会忘记加异常断点？

* 第三方或者系统库内部的异常总会自动触发异常断点（内部捕获，而没有引起崩溃），破坏正常的工作流程？

# Installation


## Config .lldbinit 
```
touch ~/.lldbinit 
open ~/.lldbinit

```

Then add the following line to your ~/.lldbinit file.

```
# ~/.lldbinit
...
command script import /path/to/SUNIgnoreExceptionThrow.py
```


## Config config.py


```
#  Set the number of times this breakpoint is skipped before stopping with `__cxa_throw`
IGNORE_CXX_COUNT = 0

#  Set the number of times this breakpoint is skipped before stopping with `objc_exception_throw
IGNORE_OC_COUNT = 0
```

The config will be available the next time `Xcode` starts.


