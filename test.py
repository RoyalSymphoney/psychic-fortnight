score = int(input('Write your score : '))
if (score >= 16 and score <= 20) :
    print('Passed')
elif score<16 and score >= 0 :
    print('Failed')
elif score > 20 or score < 0 :
    print('Illogical number')
con= input('Press any key to exit')
