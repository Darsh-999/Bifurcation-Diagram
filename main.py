from map import logistic_map as l_map, bifurcation

_set =  []
r = 0
r_offset = 0.001
while r<4:
    _set.append(l_map(x_n = 0.4, r=r, upper_limit = 10000, lower_limit=9900))
    r = r + r_offset

bifurcation(_set)

# l_map(0.4, 3.3, 200, 0)

