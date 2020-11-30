import math

aa = lambda x: x ** 2
bb = lambda x, y: math.sqrt(x ** 2 + y ** 2)
cc = lambda *args: sum(args) / len(args)
dd = lambda s: "".join(set(s))

print('Bagian a')
print(aa(5))
print('Bagian b')
print(bb(5, 10))
print('Bagian c')
print(cc(15))
print('Bagian d')
print(dd("abcde"))
