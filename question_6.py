def number_to_words(n):
    if 1 <= n <= 19:
        return ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"][n-1]
    elif 20 <= n <= 99:
        tens = ["","","twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
        return tens[n // 10] + ("" if n % 10 == 0 else number_to_words(n%10))
    elif 100 <= n <= 999:
        return number_to_words(n // 100) + "hundred" + ("" if n % 100 == 0 else "and" + number_to_words(n%100))
    elif n == 1000:
        return "onethousand"
    else:
        return ""

def count_letters_in_range(start, end):
    total_letters = 0
    for number in range(start, end + 1):
        words = number_to_words(number)
        total_letters += len(words)
    return total_letters

total_letters = count_letters_in_range(1, 1000)
print(total_letters)