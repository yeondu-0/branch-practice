for j in range(1, 30+1):
    if j % 3 == 0:
        if j % 5 == 0:
            print('fizzbuzz')
        else:        
            print('fizz')
    elif j % 5 == 0:
        print('buzz')
    else: 
        print(j)
