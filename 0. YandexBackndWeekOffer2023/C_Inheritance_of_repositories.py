'''
В системе контроля версий SEHR GUT можно наследовать репозиторий и вносить изменения кода 
в какую либо версию кода. При этом изменение, внесенное в версию кода, автоматически вносится 
во все репозитории, из которых был наследован код.Исходно в системе есть только репозиторий 
0. Если от него были пронаследованы репозитории 1 и 2, а от репозитория 1 был наследован 
репозиторий 3 и изменения были внесены в репозиторий 3, то они также внесутся в репозитории 
1 и 0 (но не в репозиторий 2). Вася хочет внести изменение в один репозиторий таким образом, 
чтобы они оказались в как можно большем количестве репозиториев.

Ограничение времени - 2 секунды
Ограничение памяти - 256mb

Формат ввода (по порядку):
Во входном файле записано число N — общее количество наследованных репозиториев 
(1 ≤ N ≤ 100000). Затем следует описание наследования репозиториев: в i-ой строке 
записано число Ri — номер репозитория, наследником которого является i-ый репозиторий 
(0 ≤ Ri < i). Начальный репозиторий имеет номер 0.

Формат вывода:
Выведите номер репозитория, в который нужно внести изменения 
Васе. Если правильных ответов несколько — выведите любой из них.

Примеры:
3,0,0,1 -> 3
8,0,1,2,0,4,5,6,4 -> 7

Первый пример соответствует ситуации, описанной в условии. 
Репозитории номер 1 и 2 пронаследованы от репоизитория с номером 0. 
Репозиторий номер 3 пронаследован от репозитория номер 1. Если внести 
изменение в репозиторий номер 3, то это изменение окажется в репозиториях 
с номерами 3, 1 и 0.

'''