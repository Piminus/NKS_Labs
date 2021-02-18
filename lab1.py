# Лабораторна робота №1 Шульга Є.К. ІО-71, №30 за списком

time_table = [
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
t1 = 433
t2 = 1073
ten_intervals = []
stat_densities = []
P_list = []

sorted_table = sorted(time_table)
int_len = 0

def count_T(gamma):

    global int_len, stat_densities, ten_intervals, P_list
    int_len = (sorted_table[-1] - sorted_table[0]) / 10
    for i in range(0, 10):
        ten_intervals.append([a for a in sorted_table if (i * int_len <= a <= (i + 1) * int_len)])
    stat_densities = [len(interval) / (len(sorted_table) * int_len) for interval in ten_intervals]
    area_sum = 1
    for i in range(10):
        P_list.append(area_sum)
        area_sum -= stat_densities[i] * int_len
    gamma = 0.63
    p_less = max([p for p in P_list if p < gamma])
    p_more = min([p for p in P_list if p > gamma])
    index_less = P_list.index(p_less)
    index_more = P_list.index(p_more)
    d = (p_more - gamma) / (p_more - p_less)
    T = index_more + int_len * d
    return T


def faultlessness_probability(time):
    
    time = 433
    Sum = 1
    whole_intervals = int(time // int_len)
    for i in range(whole_intervals):
        Sum -= stat_densities[i] * int_len
    Sum -= stat_densities[whole_intervals] * (time % int_len)
    return Sum

def count_Tcp():
    
    return sum(time_table) / len(time_table)

def fail_freq(time):
    
    f = stat_densities[int(time // int_len)]
    p = faultlessness_probability(time)
    return f / p



print("Tср:", count_Tcp())

print("Tγ:", count_T(gamma))

print("Вероятность безотказной работы:", faultlessness_probability(t1))

print("Интенсивность отказов:", fail_freq(t2))
