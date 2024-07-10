def daily_temperatures(temperatures: list[int]) -> list[int]:
    """
    739. Daily Temperatures
    https://leetcode.com/problems/daily-temperatures/description/

    """
    T = temperatures
    n = len(T)
    answer = [0] * n  # Initialize the answer array with all zeros
    stack = []  # Stack to store indices
    for i in range(n):
        # While the stack is not empty and the current temperature is greater than the temperature at the index stored at the top of the stack
        # print(f"T[i] = {T[i]}")
        while stack and T[i] > T[stack[-1]]:
            # print(f"Inside while loop\nstack[-1] = {stack[-1]}, T[i] = {T[i]}, T[stack[-1]] = {T[stack[-1]]}")
            idx = stack.pop()
            answer[idx] = i - idx  # Calculate the number of days
        stack.append(i)  # Push the current index onto the stack
        # print(f"post {i}th Iteration, stack : {stack}, answer : {answer}")
    
    return answer

if __name__ == "__main__":
    assert daily_temperatures([73,74,75,71,69,72,76,73]) == [1, 1, 4, 2, 1, 1, 0, 0], "Test case 1 failed"
    assert daily_temperatures([30,40,50,60]) == [1,1,1,0], "Test case 2 failed"
    assert daily_temperatures([30,60,90]) == [1,1,0], "Test case 3 failed"
    print("All test cases passed!")
