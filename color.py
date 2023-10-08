import colorama

try:
    print(type(colorama))
    attrs = dir(colorama)
    for i in attrs:
        print(i)

except TypeError:
    print(colorama.__name__)

    print(hasattr(colorama.__name__,))