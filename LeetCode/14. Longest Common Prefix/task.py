'''
Ссылка: https://leetcode.com/problems/longest-common-prefix/

Напишите функцию для поиска самой длинной строки общего префикса среди массива строк.
Если общего префикса нет, верните пустую строку "".

Пример 1:
Ввод: strs = ["flower","flow","flight"]
 Вывод: "fl"

Пример 2:
Ввод: strs = ["dog","racecar","car"]
 Выход: ""
 Объяснение: Bo входных строках нет общего префикса.

Ограничения:

1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i]состоит только из строчных английских букв.
'''




# Решение 
strs = ["flower","flow","flight"]
# strs = ["cir","car"]
# strs = ["dog","racecar","car"]
# strs = ["aac","a","ccc"]


len_short_word = len(strs[0])

for i in strs:
    if len(i) <= len_short_word:
        len_short_word = len(i)
        short_word = i


res = ""
flag = True

for i in strs:
    while i not in short_word:
        i = i[0:-1]
        if not(i):
            flag = False
    else:
        if flag:
            
            res = i
            short_word = res
        else:
            res = ""

print(res)




# Вставка в leetcode

# class Solution:
#     def longestCommonPrefix(self, strs: List[str]) -> str:
#         len_short_word = len(strs[0])

#         for i in strs:
#             if len(i) <= len_short_word:
#                 len_short_word = len(i)
#                 short_word = i

#         res = ""
#         flag = True

#         for i in strs:
#             while i not in short_word:
#                 i = i[0:-1]
#                 if not(i):
#                     flag = False
#             else:
#                 if flag:
#                     res = i
#                     short_word = res
#                 else:
#                     res = ""

#         return res
        