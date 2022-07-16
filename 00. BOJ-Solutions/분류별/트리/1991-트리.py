def dfs(x):
    if(x > 7):
        return
    else:
        print(x)
        dfs(2*x)
        dfs(2*x+1)

dfs(1)