while True:
    while (choice := input('a : ')) in ['a', 'b']:
        print(f'while: a: {choice}')
    else:
        print(f'else: a: {choice}')
        if choice == 'quit':
            print('break')
            break
