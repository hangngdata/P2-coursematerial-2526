def repeat(function, n):
    for i in range(0, n):
        function()


def say_hello():
    print("Hello!")

repeat(say_hello, 5)