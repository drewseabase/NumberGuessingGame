array = [2,5,25,55,100,900,1001]
low = 0
high = len(array) - 1
number = 100
iterations = 0

while low <= high:
    iterations += 1
    mid = low + (high - low) // 2
    if array[mid] == number:
        print("Got it!")
        print(iterations)
        break
    elif array[mid] < number:
        low = mid + 1

    else:
        high = mid - 1

if high == 0:
    print("Number isn't in the array")