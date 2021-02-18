# try。。except 详细用法


# 1。使用try。。except 处理指定的异常。如果引发了非指定的异常，则无法处理
try:
    s1 = 'hello'
    int(s1) # 会引发 ValueError
except ValueError as e:
# except IndexError as e:  #如果引发了非指定的异常，则无法处理
    print(e)


# 2。 多分支处理异常类.不同的异常会走向不同的except处理
s1 = 'hello'
try:
    # int(s1) # ValueError
    s1[5]    # IndexError
except IndexError as e:
    print('IndexError',e)
except KeyError as e:
    print('KeyError',e)
except ValueError as e:
    print('ValueError',e)


# 3。通用异常类 Exception
s1 = 'world'
try:
    int(s1)
except Exception as e:
    print('Exception ===',e)


# 4. 多分支异常类+通用异常类.这样引发异常后会按照从上往下的顺序去执行对应的异常处理类。
s1 = 'hello'
try:
    # int(s1) # ValueError
    s1[5]    # IndexError
except IndexError as e:
    print('IndexError',e)
except KeyError as e:
    print('KeyError',e)
except ValueError as e:
    print('ValueError',e)
except Exception as e:
    print('Exception',e)


# 5。 try...except...else...
s1 = 'hello'
try:
    str(s1)
except IndexError as e:
    print('IndexError',e)
except ValueError as e:
    print('ValueError',e)
except Exception as e:
    print('Exception',e)
else:
    print('try代码块中没有引发异常时，执行')

# 6。try...except..else..finally
# finally 无论是否引发异常，都会执行。通常情况下用于执行一些清理工作。
s1 = 'hello'
try:
    int(s1)
    print('如果前面的代码引发了异常，这个代码块将不在继续执行。。')
except IndexError as e:
    print('IndexError',e)
except ValueError as e:
    print('ValueError',e)
except Exception as e:
    print('Exception',e)
else:
    print('try代码块中没有引发异常时，执行')
finally:
    print('无论是否引发了异常，都会执行这个代码块')

print('如果上面的代码有异常并且进行了处理，那么后面的代码将继续执行')


# 7。使用 raise ，主动抛出异常
try:
    #可以使用 raise 主动抛出异常，并设置异常信息
    raise Exception('发生错误')
except Exception as e:
    print('Exception',e)


#8。 assert 断言
assert 1 == 1 # 如果后面的表达式正确，则什么也不做
assert 2 == 1 # 如果后面的表达式错误，则直接抛出 AssertionError

