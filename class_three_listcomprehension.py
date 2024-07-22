#[expression for item in iterable if condition]
squares = [x**2 for x in range(10)]
print(squares)

evens = [x for x in range(10) if x % 2== 0]
print(evens)

matrix = [[i+j for j in range(3)] for i in range(3)]
print(matrix)


numbers = [1,2,3,4,5]
modified_numbers  = [x**2 if x% 2 == 0 else x**3 for x in numbers]
print(modified_numbers)


numbers = [1,2,3,4,5]
number_tuples = [(x,x**2)for x in numbers]
print(number_tuples)


combinations = [(x,y) for x in range(3) for y in range(3)]
print(combinations)


words = ['hello', 'world', 'python', 'list', 'comprehension']
lengths = [len(word) for word in words]
print(lengths)


numbers = [1,2,3,4,5]
formatted_numbers = [f'Number {x} has square {x**2}'for x in numbers]
print(formatted_numbers)



