# x = int(input("整数を入れてください："))

# if x < 0:
#     x = 0
#     print('負数はゼロとする')
# elif x == 0:
#     print('ゼロ')
# elif x == 1:
#     print('ひとつ')
# else:
#     print('もっと')

# 4.2　for文
words = ['cat', 'window', 'defenstrate']
for w in words:
    print(w, len(w))

for w in words[:]:
    if len(w) > 6:
        words.insert(0, w)

print(words)