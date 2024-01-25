# Python_Assignment
Question 1
Write a python code for converting integer values to Indian currency notations, without 
using the currency libraries.
Explanation: Function Definition:
def convert_currency(num):
This line defines a function named convert_currency that takes an integer number as its parameter.
Convert to String:
num_string = str(num)
Converts the input integer number to a string (num_string) using the str() function.
Determine Comma Positions:
length = len(num_string)
comma_positions = [i for i in range(length - 1, 0, -2)]
Calculates the length of the string (num_string) to determine the number of digits.
Creates a list comma_positions containing the positions where commas should be inserted. It starts from the second-to-last digit and goes backward by twos.
Insert Commas:
for position in comma_positions:
    num_string = num_string[:position] + ',' + num_string[position:]
Iterates over the positions in comma_positions.
Inserts a comma at each specified position using string slicing.
Return Result:
return num_string
Returns the final string with commas inserted, representing the Indian currency notation.
Example Usage:
input_number = 504678
currency_notation = convert_currency(input_num)
print("Input:", input_num)
print("Output:", currency_notation)
Sets input_number to 504678.
Calls the convert_to_indian_currency_notation function with input_number and stores the result in output_currency_notation.
Prints the input and the converted output.

Question 2
You won’t get caught if you hide behind someone.”
Sang-Woo advises Gi-Hun to hide behind someone to avoid getting shot.
Gi-Hun follows Sang-Woo's advice and hides behind Ali, who saved his life earlier. Gi-Hun and Ali 
both have the same height, K
. Many players saw this trick and also started hiding behind Ali. 
Now, there are N
players standing between Gi-Hun and Ali in a straight line, with the ith player having height Hi
. Gi-Hun wants to know the minimum number of players who need to get shot so that Ali is visible 
in his line of sight.
Note:
• Line of sight is a straight line drawn between the topmost point of two objects. Ali is visible 
to Gi-Hun if nobody between them crosses this line. 
• Even if there are some players who have the same height as that of Gi-Hun and Ali, Ali will 
be visible in Gi-Hun's line of sight. 
• Gi-Hun and Ali have the same height. 
Input Format
• The first line of input contains a single integer T
, denoting the number of test cases. The description of T
• test cases follows. 
• The first line of each test case contains two space-separated integers N and K
• , denoting the total number of players between Gi-Hun and Ali and the height of both of 
them respectively. 
• The second line of each test case contains N
• space-separated integers, denoting the heights of the players between Gi-Hun and Ali. 
Output Format
For each test case, output in a single line the minimum number of players who need to get shot so 
that Ali is visible in Gi-Hun's line of sight.
Constraints
• 1≤T≤105
• 1≤N≤105
• 1≤K≤106
• 1≤Hi≤106 for every 1≤i≤N
• . 
• The sum of N across all test cases does not exceed 5⋅105
• . 
Sample Input 1 
3
4 10
2 13 4 16
5 8
9 3 8 8 4
4 6
1 2 3 4
Sample Output 1 
2
1
0
Explaination: j = int(input()): Read the number (j).

for _ in range(n):: Loop over each test case.

count = 0: Initialize a counter variable (count) to count the number of players who need to get shot.

j, b = list(map(int, input().split())): Read two space-separated integers, j (number of players between Gi-Hun and Ali) and b (the height of Gi-Hun and Ali).

heights = list(map(int, input().split())): Read the heights of the players between Gi-Hun and Ali.

for h in heights:: Iterate through each player's height.

if h > b:: Check if the height of the current player is greater than the height of Gi-Hun and Ali (b).

count += 1: If the condition is true, increment the counter.

print(result): Print the final count for the current test case, representing the minimum number of players who need to get shot so that Ali is visible in Gi-Hun's line of sight.
