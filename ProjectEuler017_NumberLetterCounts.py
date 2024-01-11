# 23.8.2023

# Project Euler 17
# Number Letter Counts

# If the numbers to are written out in words: one, two, three, four, five, then there are 19 letters used in total.
# If all the numbers from 1 to 1000 inclusive were written out in words, how many letters would be used?

digits_teens = [None,"one","two","three","four","five","six","seven","eight","nine","ten","eleven","twelve","thirteen","fourteen","fifteen","sixteen","seventeen","eighteen","nineteen"]
tens = [None,None,"twenty","thirty","forty","fifty","sixty","seventy","eighty","ninety"]

def write_number(n):

                            # This bit is a hack, for this problem alone! I'd like to code a full number-speller.
    if n == 1000:
        return "one thousand"

    word = ""

                            # Hundreds column, if appropriate:
    if n//100 > 0 and n//100 < 10:
        word += digits_teens[n//100] + " hundred"
        if n % 100 != 0:
            word += " and "

                            # Tens column
                            # Check for 1-20
    if n % 100 < 20 and n % 100 > 0:
        word += digits_teens[n % 100]

                            # Twenty upward
    if n % 100 > 19:
                            # take the tens column alone: (divide by ten, round, then mod ten)
                            # and dig it from the array of "ten" words...
        word += tens[n//10 % 10]
                            # if it's NOT a flat ten, then, add a hyphen and then the last digit
        if n % 10 != 0:
            word += "-" + digits_teens[n % 10]

    return word


if __name__ == "__main__":
    chunk = ""
    for n in range(1001):
        word = write_number(n)
        print(word)
        chunk += word
    chunk = chunk.replace("-","")
    chunk = chunk.replace(" ", "")
    print("\nTotal letters used in counting from 1 to 1000: " + str(len(chunk)))