import sys
try:
    int('34')
    'we' + 123
    8/0
    import module99
    open('Except.py')
except ModuleNotFoundError:
    print(' kk Module is not defined')
except NameError:
    print(' name is not defined please define')
except TypeError:
    print(' TYPE ERROR')
except FileNotFoundError as e:
    print(' Please define fine', e)
except:
    print(' Try block got failed due to : ', sys.exc_info()[1])
else:
    print(' else block')
finally:
    print(' Finally block')
