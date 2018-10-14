def check_squre(L):
    for i in range(len(L)):
        for j in range(len(L[i])):
            if L[i][j] == L[i+1][j] and L[i][j+1] == L[i+1][j+1]:
                return True
            else:
                return False


if __name__ == "__main__":
    L = [[2,2,2],[2,2,2],[2,2,2]]
    print(check_squre(L))
    print("work")