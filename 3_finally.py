'''
1. finally block will execute both times when try block executed successfully or fail.
2. it is used to do cleanup process.
'''
try:
    a = '10'
    b = 'ok'
    c = a + b
except:
    print('Try block got failed')
else:
    print('Else block is')
finally:
    print('Finally block ')