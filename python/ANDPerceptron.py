def evaluate():
    return sum([i*j for i,j in zip(inputs,weights)]) + bias

inputs = [0,1]
weights = [1,1]
bias = -1

yhat = 1 if evaluate() > 0 else 0
print(yhat)