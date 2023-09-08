A = input()
B = input()
if int(A) > 0 and len(A)==3 and int(B) > 0 and len(B) == 3:
    print(int(A)*int(B[2]))
    print(int(A)*int(B[1]))
    print(int(A)*int(B[0]))
    print(int(A)*int(B[2]) + int(A)*int(B[1])*10 + int(A)*int(B[0])*100)