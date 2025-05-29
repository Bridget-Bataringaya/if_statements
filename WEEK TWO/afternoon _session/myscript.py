from multipledispatch import dispatch

@dispatch(int, int, int)
def add(a, b, c):
    print(f"Integer sum: {a + b + c}")

@dispatch(float, float, float)
def add(a, b, c):
    print(f"Float sum: {a + b + c}")

add(2, 3, 4)          # ➜ Should print: Integer sum: 9
add(1.1, 2.2, 3.3)    # ➜ Should print: Float sum: 6.6
