j = int(input())
results = []

for _ in range(j):
    count = 0
    j, b = list(map(int, input().split()))
    heights = list(map(int, input().split()))
    for h in heights:
        if h > b:
            count += 1
    results.append(count)

# Print the results as integers
for result in results:
    print(result)