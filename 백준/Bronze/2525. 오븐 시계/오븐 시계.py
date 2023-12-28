H, M = map(int, input().split())
oven = int(input())

# 현재 시각에 오븐구이 시간을 더합니다.
H += oven // 60
M += oven % 60

# 분이 60 이상이면 시간을 조정합니다.
if M >= 60:
    H += 1
    M -= 60

# 시간이 24 이상이면 0으로 조정합니다.
if H >= 24:
    H -= 24

print(H, M)