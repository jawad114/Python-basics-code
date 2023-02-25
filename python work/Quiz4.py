#
# for item in range(1, 4):
#     for i in range(1, 4):
#         print("\n*")
f=open("jawad.txt")
# content=f.readline()
f.tell()
content=f.readline()
print(content)

print(f.tell())
content=f.readline()
print(f.readline())
print(f.seek(0))

print(f.tell())
