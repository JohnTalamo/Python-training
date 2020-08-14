for number in range(3):
    print("Check")
for number in range(5):
    print("test")
for number in range(3):
    print("Check", number + 1)
for number in range(1, 4):
    print("Check", number, number * ".")
for number in range(1, 10, 2):
    print("Check", number, number * 2)
#######
success = True
for number in range(3):
    print("Attempt")
    if success:
        print("Success")
        break
success = False
for number in range(3):
    print("Attempt")
    if success:
        print("success")
        break
else:
    print("Attempted 3 times and failed")
