#   S * *
#   * I *
#   * * D

name = str(input(" whats up , pls write name: "))

print("------------------------------------")
for i in range(0, len(name) ):
    for j in range(0, len(name) ):
        if i == j:
            print(name[j] , sep=" " , end=" ")
        else:
            print("*"  , sep=" " , end=" ")

    print()




















