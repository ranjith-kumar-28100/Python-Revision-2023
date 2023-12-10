import logging

logging.basicConfig(filename='mylog.log', filemode='a', level=logging.DEBUG)
f = open('f.txt', 'w')
a, b = [int(x) for x in input('enter two numbers: ').split(' ')]
try:
    c = a / b
except ZeroDivisionError:
    logging.error("Division by Zero is not allowed")
else:
    f.write(str(c))
finally:
    f.close()
    print("File Closed")
print("code after exception")
