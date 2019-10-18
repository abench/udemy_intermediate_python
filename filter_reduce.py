x = filter(str.isalpha, ['1', '2', '3', 'a', 'b'])
print(x)
print(list(x))

from functools import reduce

def add(x,y):
    return x+y

z= reduce(add, [1,2,3,4,5,6,7,8,9,10],0)

print(z)

lines = ["hello, computer.", "how are You",
         "Now, when is it a good idea to use this feature in your own Python code?",
         "My rule of thumb is that if a function doesn’t have a return value (other languages would call this a procedure ), then I will leave out the return statement.",
         "Adding one would just be superfluous and confusing.",
         "An example for a procedure would be Python’s built-in print function which is only called for its side-effects (printing text) and never for its return value.",
         "Let’s take a function like Python’s built-in sum.",
         "It clearly has a logical return value, and typically sum wouldn’t get called only for its side-effects.",
         "Its purpose is to add a sequence of numbers together and then deliver the result.",
         "Now, if a function does have a return value from a logical point of view, then you need to decide whether to use an implicit return or not."]


from collections import defaultdict
def count_words(s):
    counts = defaultdict(int)

    for word in s.split():
        counts[word] += 1

    return dict(counts)


print(dict(count_words(lines[0])))

