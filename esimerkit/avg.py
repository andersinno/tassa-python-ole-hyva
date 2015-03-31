numbers = []

while True:
    s = input("Enter a number or empty to calculate the average: ")
    if not s:
        break
    try:
        numbers.append(int(s))
    except:
        print("That didn't look like a number, try again?")

print("The average is %s" % (sum(numbers) / len(numbers)))
