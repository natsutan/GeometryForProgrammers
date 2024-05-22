import matplotlib.pyplot as plt


#  x_{i+1} = x_i^2 - x_i
N = 10

def f(x):
    for i in range(N):
        x = x ** 2 - x
        if x > 10:
            return 10
        print(x)

    return x**2 - x

# 初期値を -2.0から2.0まで0.1刻みで変化させていく
xs = []
ys = []
for i in range(-20, 30):
    x = i / 10
    xs.append(x)
    ys.append(f(x))

# グラフにプロットする。




plt.plot(xs, ys)
plt.show()




