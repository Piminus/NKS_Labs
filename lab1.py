# Лабораторна робота №1 Шульга Є.К. ІО-71, №30 за списком

input_data = [
                1566, 984, 502, 6, 802, 823, 68, 2671, 1468,
                2162, 615, 1405, 1146, 79, 192, 1005, 777,
                756, 4531, 1554, 698, 279, 75, 484, 745,
                563, 81, 525, 567, 1340, 846, 1410, 26, 370,
                763, 82, 34, 635, 658, 812, 1627, 4908, 981,
                1334, 139, 271, 195, 520, 1841, 526, 203,
                1705, 697, 985, 258, 73, 168, 809, 334, 727,
                342, 1429, 744, 1415, 2513, 444, 488, 2367,
                368, 587, 1953, 124, 231, 3087, 561, 3066,
                1609, 962, 1811, 294, 4187, 157, 76, 1420,
                1926, 493, 1763, 977, 897, 2497, 841, 1143,
                345, 236, 233, 448, 1429, 900, 1751, 566]

gamma = 0.63
workWithoutFailsTimeParam = 433
intensivityTimeParam = 1073

sorted_table = sorted(input_data)

print("Средняя наработка до отказа Tср:", sum(sorted_table) / len(sorted_table))

k = 10
intervals_length = (sorted_table[-1] - sorted_table[0]) / k

intervals = []
for i in range(k):
    intervals.append([a for a in sorted_table if (a >= i * intervals_length and a < (i + 1) * intervals_length)])

f = [len(interval) / (len(sorted_table) * intervals_length) for interval in intervals]

p_list = []
area = 1
for i in range(k):
    p_list.append(area)
    area -= f[i] * intervals_length

p_min = max([p for p in p_list if p < gamma])
p_max = min([p for p in p_list if p > gamma])

print("γ-процентная наработка на отках Tγ при γ = 0.63:", intervals_length - intervals_length * (p_min - gamma) / (p_min - p_max))

probability_of_unfail = 1
whole = int(workWithoutFailsTimeParam // intervals_length)
for i in range(whole):
    probability_of_unfail -= f[i] * intervals_length
probability_of_unfail -= f[whole] * (workWithoutFailsTimeParam % intervals_length)

print("Вероятность безотказной работи на время 433 часов:", probability_of_unfail)

probability_of_unfail = 1
whole = int(workWithoutFailsTimeParam // intervals_length)
for i in range(whole):
    probability_of_unfail -= f[i] * intervals_length
probability_of_unfail -= f[whole] * (workWithoutFailsTimeParam % intervals_length)

print("Интенсивность отказoв на время 1073 часов:", f[int(intensivityTimeParam // intervals_length)] / probability_of_unfail)
