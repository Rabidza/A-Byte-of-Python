# def reverse(text):
#     return text[::-1]

# def is_palindrome(text):
#     return text == reverse(text)

# something = raw_input("Enter text: ")
# if is_palindrome(something):
#     print "Yes, it is a palindrome."
# else:
#     print "No it is not a palindrome."

# 15.1.1 Homework Exercise
forbidden =  ('.', '?', '!', ':', ';', '-', '(', ')', '[', ']', '...', "'", '"', '/', ',')

def reverse(text):
    check = ''
    text = text.lower().replace(' ', '')
    for letter in text:
        if letter not in forbidden:
            check += letter
    return check[::-1]

def is_palindrome(text):
    check = ''
    text = text.lower().replace(' ', '')
    for letter in text:
        if letter not in forbidden:
            check += letter
    return check == reverse(text)

something = raw_input("Enter text: ")
if is_palindrome(something):
    print "Yes, it is a palindrome."
else:
    print "No it is not a palindrome."