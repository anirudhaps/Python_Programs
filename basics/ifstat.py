age = int(input('Enter the age:'))
rel = input('Enter the relationship status(married/single):')
if age == 24:
    print('you are 24 years old')
    print('it is the upper age limit')
    if rel == 'single':
        print('go ahead! get married')
    else:
        print('I don\'t know what to do')
elif age > 24:
    print('you are overage')
    print('Alas! you can\'t do anything about that')
    if rel == 'single':
        print('Hey! why are you single?')
    else:
        print('I am glad that you are married')
else:
    print('you are well below the upper age limit')
    print('complete your studies before getting married')
