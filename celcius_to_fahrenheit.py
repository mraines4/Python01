c_temp = int(input('Temperature in C? '))

f_conversion = c_temp * 1.8 +32

if f_conversion.is_integer():
    print('%d F' % f_conversion)
else:
    print('%.1f F' % f_conversion)




