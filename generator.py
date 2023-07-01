def generator_function():
    for i in range(10):
        yield i



gen = generator_function()
print(next(gen))
print(next(gen))

my_string = "Yasoob"
my_iter = iter(my_string)
print(next(my_iter))
