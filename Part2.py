from functools import reduce
import random
import string
import math
from functools import partial

#################################################################################################################################
# 1. Write a function using only list filter lambda that can tell whether a number is a Fibonacci number or not. 
#    You can use a pre-calculated list/dict to store fab numbers till 10000
#################################################################################################################################

def generate_fibonacci_seq(n: "non negative int") -> list:
    '''generates fibonacci seq till nth element'''

    if not isinstance(n, int):
        raise TypeError(f"n must be a int, not {type(n).__name__}")

    if n < 0:
        raise ValueError("n must be a non negative integer")

    if n == 0:
        return None
    elif n == 1: 
        return [0]
    else:
        fibonacci_seq = [0, 1]
        reduce(lambda a, b: len(fibonacci_seq) < n and (fibonacci_seq.append(a+b) or a+b), fibonacci_seq, 1)
    return fibonacci_seq

def is_fibonacci(num: "non negative int") -> bool:
    '''checks if the input number is a fibonacci number'''

    if not isinstance(num, int):
        raise TypeError(f"num must be a int, not {type(num).__name__}")

    if num < 0:
        raise ValueError("num must be a non negative integer")

    fibonacci_seq_10000 = generate_fibonacci_seq(10000)

    is_fib = lambda x: True if x in fibonacci_seq_10000 else False
    return is_fib(num)

#################################################################################################################################
# 2. Using list comprehension (and zip/lambda/etc if required) write expressions that:
#################################################################################################################################

################################################################################################################
#    a. add 2 iterables a and b such that a is even and b is odd
################################################################################################################
a = random.sample(range(1, 100), 10)
b = random.sample(range(1, 100), 10)

result = [i+j for i,j in zip(a,b) if (i+j)%2==1]   


################################################################################################################
#    b. strips every vowel from a string provided (tsai>>t s)
################################################################################################################
word = ''.join(random.choices(string.ascii_letters, k = 20))

out_str = "".join([l for l in word if l.lower() in "aeiou"])


################################################################################################################
#    c. acts like a sigmoid function for a 1D array
################################################################################################################
lst = [random.uniform(-6, 6) for i in range(10)]

sigmoid = lambda x: 1/(1+math.exp(-x))

sig_lst = [sigmoid(x) for x in lst]


################################################################################################################
#    d. takes a small character string and shifts all characters by 5 (handle boundary conditions) tsai>>yxfn
################################################################################################################
lower = string.ascii_lowercase
upper = string.ascii_uppercase

char_str = ''.join(random.choices(string.ascii_letters, k = 5))

shift_str = ''.join([ lower[(lower.index(i) + 5)%len(lower)] if i.islower() else upper[(upper.index(i) + 5)%len(upper)] for i in char_str ])


#################################################################################################################################
# 3. A list comprehension expression that takes a ~200-word paragraph, 
#    and checks whether it has any of the swear words mentioned in:
#    https://github.com/RobertJGabriel/Google-profanity-words/blob/master/list.txt
#################################################################################################################################
with open('toxic_comment.txt') as f:
    paragraph = f.read()
with open("list.txt") as f:
    swear_words = f.read().splitlines()

is_toxic_statement = any([True for word in paragraph if word in swear_words])


#################################################################################################################################
# 4. Using reduce function
#################################################################################################################################


################################################################################################################
#    a. add only even numbers in a list
################################################################################################################
lst = [random.randint(-100, 100) for i in range(10)]

sum_red_fil = reduce(lambda a, b: a+b, filter(lambda a: a%2==0, lst)) # using filter

sum_red = reduce(lambda a, b: a+b if b%2==0 else a, lst, 0) # without using filter, using initializer


################################################################################################################
#    b. find the biggest character in a string (printable ASCII characters)
################################################################################################################
char_str = ''.join(random.choices(string.printable, k = 5))

max_char = reduce(lambda a, b: a if ord(a)>ord(b) else b, char_str)


################################################################################################################
#    c. adds every 3rd number in a list
################################################################################################################
lst = [random.randint(-100, 100) for i in range(10)]

sum_3rd = reduce(lambda a,b: a+b, list(zip(*filter(lambda a: a[0]%3==2, enumerate(lst))))[1])



################################################################################################################
# 5. Using randint, random.choice and list comprehensions, 
#    write an expression that generates 15 random KADDAADDDD number plates, 
#    where KA is fixed, D stands for a digit, and A stands for Capital alphabets. 10<<DD<<99 & 1000<<DDDD<<9999
################################################################################################################
random_plate = lambda : "KA" + str(random.randint(10, 99)) + str(random.choice(string.ascii_uppercase)) + str(random.choice(string.ascii_uppercase)) + str(random.randint(1000, 9999))

plates = [random_plate() for i in range(10)]




################################################################################################################
# 6. Write the above again from scratch where KA can be changed to DL, and 1000/9999 ranges can be provided. 
#    Now use a partial function such that 1000/9999 are hardcoded, but KA can be provided
################################################################################################################
random_plate = lambda state, r1, r2: state + str(random.randint(10, 99)) + str(random.choice(string.ascii_uppercase)) + str(random.choice(string.ascii_uppercase)) + str(random.randint(r1, r2))

random_plates_fixed_range = partial(random_plate, r1 = 1000, r2 = 9999)

plates = [random_plate("DL", 1000, 9999) for i in range(10)]

plates_fixed_range = [random_plates_fixed_range("KA") for i in range(10)]

