def maxScore(cardPoints, k):
    n = len(cardPoints)
    total = sum(cardPoints)
    window_size = n - k
    window_sum = sum(cardPoints[:window_size])
    min_window_sum = window_sum

    for i in range(window_size, n):
        window_sum += cardPoints[i] - cardPoints[i - window_size]
        min_window_sum = min(min_window_sum, window_sum)
    return total - min_window_sum

cardPoints = list(map(int, input("Enter card points separated by spaces: ").split()))
k = int(input("Enter the number of cards to take: "))

print("Maximum score:", maxScore(cardPoints, k))