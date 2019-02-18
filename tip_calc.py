while True:
    try:
        total_bill = float(input('Total bill amount? '))

        while True:
            service_level = input('Level of service? ').lower()
            if service_level == 'good':
                tip = total_bill * .2
                break
            elif service_level == 'fair':
                tip = total_bill * .15
                break
            elif service_level == 'bad':
                tip = total_bill * .1
                break
            else:
                print('thats not an option: please enter good, fair, or bad')
                

        final_bill = total_bill + tip

        print('Tip amount: $%.2f \nTotal amount: $%.2f' % (tip, final_bill))
        break
    except ValueError:
        print("try again bucko")

