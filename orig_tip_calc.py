total_bill = float(input('Total bill amount? '))
service_level = input('Level of service? ')


if service_level == 'good':
    tip = total_bill * .2
elif service_level == 'fair':
    tip = total_bill * .15
elif service_level == 'bad':
    tip = total_bill * .1
else:
    print('thats not an option: good, fair, bad')

final_bill = total_bill + tip

print('Tip amount: $%.2f \nTotal amount: $%.2f' % (tip, final_bill,))
