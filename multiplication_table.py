def multiplication_table(x, y):
    for i in range(x):
        for j in range(y):
            print(f'{i+1}x{j+1}={(i+1)*(j+1)}')


multiplication_table(8, 15)
