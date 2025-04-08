lives = 7
hangword = input("Word to guess: ")
testnum = 0
alpha = "abcdefghijklmnopqrstuvwxyz"
for i in range(20):
    print("ㅤ")
for i in range(len(alpha)):
    censoredword = hangword.replace("a", "=")
    testnum = testnum + 1
print(censoredword)
