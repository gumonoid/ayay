result = []

def divider(a, b):
    try:
        a = float(a)
        if b == 0:
            raise ZeroDivisionError("Ділення на 0 неможливе")
        if a < b:
            raise ValueError("a повинно бути більше або дорівнює b")
        if b > 100:
            raise IndexError("b повинно бути менше або дорівнює 100")
        return a / b
    except (ZeroDivisionError, ValueError, IndexError, TypeError) as e:
        print(f"Error: {e}")
        return None

data = {10: 2, 2: 5, "123": 4, 18: 0, "invalid_key": 15, 8: 4}

for key in data:
    res = divider(key, data[key])
    if res is not None:
        result.append(res)

print(result)
