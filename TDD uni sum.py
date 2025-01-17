def test_fizz_buzz():
    assert fizz_buzz (9) == 'Fizz'
    assert fizz_buzz (10) == 'Buzz'
    assert fizz_buzz (15) == 'FizzBuzz'

def fizz_buzz(number):
    if number % 3 == 0 and number % 5 == 0:
        return 'FizzBuzz'
    elif number % 3 == 0:
        return 'Fizz'
    elif number % 5 == 0:
        return 'Buzz'
    
test_fizz_buzz()