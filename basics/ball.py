from itertools import combinations

BLOCKER = 1000


def place_random_obstacle(act_line, obstacles):
    c = []
    for comb in combinations(act_line, obstacles):
        line = act_line.copy()
        if 0 in comb:
            print(comb , "skpiing")
            continue
        for pos in comb:
            line[pos] = BLOCKER
        c.append(line)
    return c


def walk_from_origin(distance, road, num_line_org):
    status = False

    walk_dir = 1
    curr_index = 0
    no_of_flips = 0
    calories_burned = 0
    mid = len(road) // 2
    for i in range(distance):
        if road[mid + curr_index + 1] == BLOCKER:
            walk_dir *= -1
            no_of_flips += 1

        curr_index = curr_index + walk_dir
        calories_burned += 1

    if curr_index == 0 and no_of_flips <= 2:
        print("Got solution in right walk")
        status = True
        return status

    # for left walk
    walk_dir = -1
    curr_index = 0
    calories_burned = 0
    mid = len(road) // 2
    no_of_flips = 0
    for i in range(distance):
        if road[mid - curr_index + 1] == BLOCKER:
            walk_dir *= -1
            no_of_flips += 1

        curr_index = curr_index + walk_dir
        calories_burned += 1

    if curr_index == 0 and no_of_flips <= 2:
        print("Got solution in left walk")
        status = True
        return status

    return status


def solve(distance, obstacles, number_line_bound):
    num_line_org = list(range(-number_line_bound, number_line_bound+1))
    print(num_line_org)
    num_line_with_obs = place_random_obstacle(num_line_org, obstacles)
    pass_cnt = 0
    for sample in num_line_with_obs:
        if walk_from_origin(distance, sample, num_line_org):
            print(sample)
            pass_cnt += 1
    print(pass_cnt)


if __name__ == '__main__':
    distance = 6
    obstacles = 4
    number_line_bound = 3

    solve(distance, obstacles, number_line_bound)
