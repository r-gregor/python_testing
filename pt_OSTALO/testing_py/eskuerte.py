tolerance = 1.0e-15
lower = 0.0
upper = 2.0
uncertainty = upper - lower
iter=0
while uncertainty > tolerance:
    iter=iter+1
    print("Iteration: " + str(iter))
    middle = (lower + upper)/2
    if middle**2 < 2.0:
        lower = middle
    else:
        upper = middle
    print(lower, upper)
    uncertainty = upper - lower

