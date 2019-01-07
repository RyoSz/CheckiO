##### Multiply (Intro) #####

print("\n##### Multiply (Intro) #####")
def mult_two(a, b):
    # your code here
    return a*b


if __name__ == '__main__':
    print("Example:")
    print(mult_two(3, 2))
    
    # These "asserts" are used for self-checking and not for an auto-testing
    assert mult_two(3, 2) == 6
    assert mult_two(1, 0) == 0
    print("Coding complete? Click 'Check' to earn cool rewards!")


##### Say Hi #####

print("\n##### Say Hi #####")
# 1. on CheckiO your solution should be a function
# 2. the function should return the right answer, not print it.

def say_hi(name: str, age: int) -> str:
    return "Hi. My name is " + name + " and I'm " + str(age) + " years old"

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert say_hi("Alex", 32) == "Hi. My name is Alex and I'm 32 years old", "First"
    assert say_hi("Frank", 68) == "Hi. My name is Frank and I'm 68 years old", "Second"
    print('Done. Time to Check.')


##### Correct Sentence #####

print("\n##### Correct Sentence #####")
def correct_sentence(text: str) -> str:
    """
        returns a corrected sentence which starts with a capital letter
        and ends with a dot.
    """
    # your code here
    if (text[0].islower() and text.endswith('.')):
        return text[0].upper() + text[1:]
    elif (text[0].islower() and not text.endswith('.')):
        return text[0].upper() + text[1:] + "."
    elif (text[0].isupper() and not text.endswith('.')):
        return text + "."
    else:
        return text    

if __name__ == '__main__':
    print("Example:")
    print(correct_sentence("greetings, friends"))
    
    # These "asserts" are used for self-checking and not for an auto-testing
    assert correct_sentence("greetings, friends") == "Greetings, friends."
    assert correct_sentence("Greetings, friends") == "Greetings, friends."
    assert correct_sentence("Greetings, friends.") == "Greetings, friends."
    assert correct_sentence("hi") == "Hi."
    assert correct_sentence("welcome to New York") == "Welcome to New York."
    
    print("Coding complete? Click 'Check' to earn cool rewards!")


text = "Hello world"
print(len(text))
print(range(len(text)))
print(text)
print(text[0:len(text)])
for i in text[0:len(text)]:
    print(i)


##### First Word #####

# print("\n##### First Word #####")
# def first_word(text: str) -> str:
#     """
#         returns the first word in a given text.
#     """
#     # your code here
#     """
#     transaction should be
#     1. eliminate space and dots if it's at the beggining of words.
#     2. take each element of string from the start and until it hits a space or dot.
#     """
#     text = text.strip()
#     text = text.strip('.')
#     # for s in text:
#     #     if s == " " or s == ".":
#     #         break
#     #     else:
#     #         return s
#     for s in text[0:len(text)]:
#         return s


# if __name__ == '__main__':
#     print("Example:")
#     print(first_word("Hello world"))
    
#     # These "asserts" are used for self-checking and not for an auto-testing
#     assert first_word("Hello world") == "Hello"
#     assert first_word(" a word ") == "a"
#     assert first_word("don't touch it") == "don't"
#     assert first_word("greetings, friends") == "greetings"
#     assert first_word("... and so on ...") == "and"
#     assert first_word("hi") == "hi"
#     assert first_word("Hello.World") == "Hello"
#     print("Coding complete? Click 'Check' to earn cool rewards!")


















