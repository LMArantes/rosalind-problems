def recurrence(n, k):
    if n == 1 or n == 2:
        return 1

    # Creates list of size n
    dp = [0] * (n + 1)

    # Base cases
    dp[1] = 1
    dp[2] = 1

    for i in range(3, n + 1):
        dp[i] = dp[i - 1] + k * dp[i - 2]

    return dp[n]
