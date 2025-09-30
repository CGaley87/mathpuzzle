#Curtis Galey
#Mathpuzzle.py
#Finding a number that when multiplied can result in a  mirror of itself as an answer
import time

def digit_range(dc: int, m: int) -> tuple[int, int]:
    low = 10 ** (dc-1) #lowest possible solution
    high = (10 ** dc - 1) // m #highest possible solution because of digit limit and it
                            #must be a solution multiplied by m. Limiting upper range
    return low, high

def solution(dc: int, m: int, start_time: float, max_seconds:float) -> list[int]:
    low, high = digit_range(dc, m) #finding range
    solved = [] #empty list to store solutions
    for num in range(low, high + 1):
        if time.monotonic() - start_time > max_seconds:
            return solved, True #added True to indicate timed out.
        if num * m == int(str(num)[::-1]): #comparing number to its inverse
            solved.append(num) #adding number if it matches
    return solved, False

while True:
    retry = input("Would you like to test a combination of digits and multipliers? Y or N: ").strip().lower()
    if retry == 'y':
        while True:
            digit_count = int(input("Please enter a starting digit length: "))
            if digit_count >= 1: #count must be at least one
                break
            print("Please enter a number lenght of 1 or higher.")

        while True:
            multiplier = int(input("Please enter a multiplier between 3 and 9: "))
            if 3 <= multiplier <= 9: #limiting to single digit multiplier to increase result chance
                break
            print("Please enter a nunber from 3 to 9.")

        while True:
            max_seconds = float(input("Enter maximum seconds to search between 1.0 and 10.0: "))
            if 1.0 <= max_seconds <= 10.0:
                break
            print("Please enter a number between 1.0 and 10.0")

        start_time = time.monotonic()
        all_solutions = []
        dc = digit_count #to reduce clutter in methods
        
        while True:
            answers, timed_out = solution(dc, multiplier, start_time, max_seconds)
            all_solutions.extend(answers)
            if timed_out:
                print("Timeout reached, stopping search.")
                break
            dc += 1 #continue increasing the digit count

        if all_solutions:
            print("Solutions found:")
            for num in all_solutions:
                print(num)
        else:
            print("No solution found")
    else:
        print("Program exited.")
        break