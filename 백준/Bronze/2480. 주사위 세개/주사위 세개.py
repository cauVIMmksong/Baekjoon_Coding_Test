D1, D2, D3 = map(int, input().split())

if D1 == D2 == D3:  # Three dice have the same value
    print(10000 + (D1 * 1000))
elif D1 == D2 or D1 == D3 or D2 == D3:  # Two dice have the same value
    if D1 == D2 == D3:  # Special case for three of a kind
        print(10000 + (D1 * 1000))
    else:
        if D1 == D2:
            print(1000 + (D1 * 100))
        elif D1 == D3:
            print(1000 + (D1 * 100))
        else:
            print(1000 + (D2 * 100))
else:  # All dice have different values
    max_value = max(D1, D2, D3)  # Find the maximum value among the three dice
    print(max_value * 100)