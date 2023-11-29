# author: cheyenne（8神）
def rotate_left_as_WinHex(b: bytes):
    return bytes((n << (i + 1)) % 0xFF for i, n in enumerate(b))

print(rotate_left_as_WinHex(bytes(range(1, 9))))

a = bytes(range(1, 9))
for i in range(8):
    a = rotate_left_as_WinHex(a)
print(a == bytes(range(1, 9)))
