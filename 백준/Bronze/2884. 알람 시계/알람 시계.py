H, M = map(int, input().split())

if M < 45 and H >= 1:
    print(H-1, (M+60)-45)
if M >= 45 :
    print(H,M - 45)
if M < 45 and H < 1 :
    print(24-1,(M+60)-45)