def f(dict):
    return [dict[key] for key in dict.keys()]
print(f(dict(a=1, b=2)))