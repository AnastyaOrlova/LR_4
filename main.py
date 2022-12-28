import random
import math

def rand():
    y = random.uniform(0, 1)
    return y

def exp(a):
    y = rand()
    time_client = -1/a*math.log(y)
    return time_client

def case_1(time_step, t_z, time_work, reject):
    time_work += time_step + t_z
    if time_work <= time_step:
        N_1.append(time_step)
    else:
        case_2(time_step, t_z, time_work, reject)

def case_2(time_step, t_z, time_work, reject):
    time_work += time_step + t_z
    if time_work <= time_step:
        N_1.append(time_step)
    else:
        case_3(time_step, t_z, time_work, reject)

def case_3(time_step, t_z, time_work, reject):
    time_work += time_step + t_z
    if time_work <= time_step:
        N_1.append(time_step)
    else:
        case_4(time_step, t_z, time_work, reject)

def case_4(time_step, t_z, time_work, reject):
    time_work += time_step + t_z
    if time_work <= time_step:
        N_1.append(time_step)
    else:
        reject += 1

if __name__ == '__main__':
    N_1 = []
    N_2 = []
    N_3 = []
    N_4 = []
    a = 1
    T = 20
    t_z = 18
    reject = 0
    # time_client = exp(a)
    time_step = 0
    # time_step += time_client
    time_work = 0
    while time_step < T:
        time_client = exp(a)
        print("time_client = ", time_client)
        time_step += time_client
        print("time_step = ", time_step)
        case_1(time_step, t_z, time_work, reject)

    print(N_1)
    print(N_2)
    print(N_3)
    print(N_4)
    print(reject)
