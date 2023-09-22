'''
В городе М есть два любимых занятия: укладывать плитку и проводить непонятные раскопки тротуара. 
До начала очередного сезона ремонтов на всех тротуарах была уложена плитка. После проведения 
раскопок тротуар непригоден для использования, пока на нем не уложат плитку. Всего в городе М k 
тротуаров.От каждого тротуара без плитки жители города М ежедневно получают одну единицу печали. 
Если тротуар был раскопан в день a, а плитка на нём была уложена в день b, то жители города получат 
b−a единиц печали. Плитку можно уложить и в день раскопок, тогда жители получат 0 единиц печали. 
Тротуар, на котором проводились раскопки может быть снова раскопан и, если на нем была плитка, 
то она будет сломана.Все раскопки и укладки плитки должны завершиться до выборов мэра города 
М, при этом на всех раскопанных тротуарах перед выборами должна быть уложена плитка. Всего 
работ по раскопкам тротуаров планируется n.Руководителю компании-подрядчика по укладке плитки 
попал в руке план раскопок тротуаров с указанием номера тротуара и номера дня, когда тротуар 
будет раскопан. К сожалению, в бюджете выделены средства только для m укладок плитки на 
тротуарах. Зато в компании достаточно трудолюбивых работников чтобы уложить любое количество 
плитки в любой из дней.Определите, какое наименьшее суммарное количество единиц печали получат 
жители города М до выборов мэра.

Формат ввода:

В первой строке вводятся числа k,n и m (1≤k≤1000, 1≤n,m≤100000) — количество тротуаров, 
количество раскопок и количество укладок плитки, на которые выделены средства в бюджете.
В следующих n строках заданы пары чисел di,wi (1≤di≤109, 1≤wi≤K) — день, в который будут 
проведены раскопки и номер тротуара, на которых они будут проводиться. Эти пары заданы в порядке неубывания di.

Формат вывода:

Выведите одно число — минимальное суммарное количество единиц печали. Если до 
выборов останутся раскопанные тротуары — выведите −1, как признак бесконечной печали жителей

Примеры:
5 4 3
1 2
2 3
2 1
6 2
-> 5

2 4 2
1 1
1 2
3 1
4 2
-> 5

В первом примере на тротуарах 1 и 3 нужно уложить плитку в день раскопок, 
а тротуар 2 ремонтируется на шестой день, сразу после проведения раскопок.

'''