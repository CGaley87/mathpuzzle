#Curtis Galey
#Mathpuzzle.py
#Finding a number that when multiplied can result in a  mirror of itself as an answer

def digit_range(x: int, m: int) -> tuple[int, int]:
    low = 10 ** (x-1) #lowest possible solution
    high = (10 ** x - 1) // m #highest possible solution because of digit limit and it
                            #must be a solution multiplied by m. Limiting upper range
    return low, high

def solution(a: int, b: int, m: int) -> list[int]:
    solved = [] #empty list to store solutions
    for num in range(a, b):
        if num * m == int(str(num)[::-1]): #comparing number to its inverse
            solved.append(num) #adding number if it matches
    return solved

while True:
    retry = input("Would you like to test a combination of digits and multipliers? Y or N: ").strip().lower()
    if retry == 'y':
        while True:
            digit_count = int(input("Please enter how many digits the number can be between 3 and 8: "))
            if 3 <= digit_count <= 8: #limiting to ensure quickly computable
                break
            print("Please enter a number from 3 to 8.")

        while True:
            multiplier = int(input("Please enter a multiplier between 3 and 9: "))
            if 3 <= multiplier <= 9: #limiting to single digit multiplier to increase result chance
                break
            print("Please enter a nunber from 3 to 9.")

        low, high = digit_range(digit_count, multiplier) #finding range

        solved = solution(low, high, multiplier) #finding solutions

        if solved:
            print("Solutions found:")
            for num in solved:
                print(num)
        else:
            print("No soltion found")
    else:
        print("Program exited.")
        break