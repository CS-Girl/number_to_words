def nums_to_words(string):
    string = int(string)  # Convert the string to an integer
    one_ten = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven',
               'eight', 'nine']
    ten_nineteen = ['ten', 'eleven', 'twelve', 'thirteen', 'fourteen',
                    'fifteen',
                    'sixteen', 'seventeen', 'eighteen', 'nineteen']
    twenty_ninety = [' ', ' ', 'twenty', 'thirty', 'forty', 'fifty', 'sixty',
                     'seventy', 'eighty',
                     'ninety']
    temp_str = ""
    if string == 0:  # If the string given equals to 0
        temp_str = 'zero '  # Assign the word zero to the var temp_str
    # Do the calculation to find each digit of the str given
    first_digit = string // 1000000
    second_digit = (string % 1000000) // 100000
    third_digit = (string % 100000) // 10000
    fourth_digit = (string % 10000) // 1000
    fifth_digit = (string % 1000) // 100
    sixth_digit = (string % 100) // 10
    seventh_digit = (string % 10)
    if first_digit > 0:
        temp_str = temp_str + one_ten[first_digit] + ' million '
    if second_digit > 1:
        temp_str = temp_str + one_ten[second_digit] + ' hundred '
    if third_digit > 1:
        temp_str = temp_str + twenty_ninety[third_digit] + ' '
    if fourth_digit > 0:
        temp_str = temp_str + one_ten[fourth_digit] + ' thousand '
    # one_ten[first_digit] gets you the number you need from one_ten and you add thousand (since we're trying to convert to words ofc)
    # You do the same for the rest...
    if fifth_digit > 0:
        temp_str = temp_str + one_ten[fifth_digit] + ' hundred '
    if sixth_digit > 1:
        temp_str = temp_str + twenty_ninety[sixth_digit] + " "
    if seventh_digit == 1:
        temp_str = temp_str + ten_nineteen[seventh_digit] + " "
    else:
        if seventh_digit:
            temp_str = temp_str + one_ten[fourth_digit] + " "
    if temp_str[-1] == " ":  # If the last index is a space
        temp_str: str = temp_str[0:-1]  # Slice it

        return temp_str
string = input("Enter the value: ")

print("\n")
print(nums_to_words(string))
