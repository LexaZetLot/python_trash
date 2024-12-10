S = 'ni'
print(S.encode('ascii'), S.encode('latin1'), S.encode('utf8'))
print(S.encode('utf16'), len(S.encode('utf16')))
print(S.encode('utf32'), len(S.encode('utf32')))

S = 'eggs'
S.encode()
print(S)
bytes(S, encoding='utf-8')
print(bytes(S, encoding='utf-8'))

B = b'spam'
B.decode()
print(B)