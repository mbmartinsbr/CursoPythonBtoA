"""
add (adiciona), update (autaliza), clear, discard
union | une
intersection & (todos os elementos presentes nos dois sets)
difference - (elementos apenas no set da esquerda)
symmetric_difference ^ (Elementos que estao nos dois sets, mas não em ambos)
"""
# s1 = set()
# # s1 = {1, 2, 3, 4, 5, 6}
# # s1.add(1)
# # s1.add(2)
# # s1.add((1,2,3,'Luiz'))
#
# # s1.update('Python')
#
# s1.update([1,2,3,4,5], {5,6,7,8})
#
# # s1.discard(2)
#
# print(s1)
# for v in s1:
#     print(v)

# l1 = [1, 2, 1, 1, 3, 4, 5, 6, 3, 6, 6, 6, 6, 6, 7, 8, 9, 'Luiz', 'Luiz']
# l1 = set(l1)
# l1 = list(l1)
# print(l1)

# s1 = {1, 2, 3, 4, 5, 7}
# s2 = {1, 2, 3, 4, 5, 6}
#
# # s3 = s1 | s2   # union
# # s3 = s1 & s2  # intersection
# # s3 = s1 - s2  # difference
# s3 = s1 ^ s2  # symmetric_difference
#
# print(s3)

l1 = ['Luiz', 'Joao', 'Maria']
l2 = ['Joao', 'Maria', 'Luiz', 'Luiz', 'Luiz', 'Luiz', 'Luiz', 'Maria']

# l1 = list(set(l1))
# l2 = list(set(l2))
#
# print(l1)
# print(l2)
if set(l1) == set(l2):
    print('L1 igual l2')
else:
    print('l1 é diferente de l2')
