'''
1. else block will execute when the try block executed successfully with out any errors
'''

try:
    a = 10
    b = 'ok'
    c = a + b
except:
    print('Try block got failed')
else:
    print('Else block is')