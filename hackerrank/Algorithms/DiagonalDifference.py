n = int(input().strip())
a = []
for a_i in range(n):
    a_t = [int(a_temp) for a_temp in input().strip().split(' ')]
    a.append(a_t)
print(abs(sum(a[i][n-1-i] for i in range(n)) - sum(a[i][i] for i in range(n))))