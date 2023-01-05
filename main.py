import random
import math

def rand():
    y = random.uniform(0, 1)
    return y

def exp(a):
    y = rand()
    rand_t = -1/a*math.log(y)
    return rand_t

def start (N, case):
    for i in range (N):
        case.append(0)
    return case

def model(time_client, t_z, case, time_work, reject):
    # print(time_work)
    # print(case)
    for i in range(len(time_work)):
        if time_work[i] <= time_client:
            time_work[i] += time_client + t_z
            case[i] += 1
            # print(time_work)
            # print(case)
            break
        if i == len(time_work) - 1:
            reject[0] += 1
    # print(reject)

    return case, time_work, reject

if __name__ == '__main__':
    iterate = 10000
    N = 11
    a = 2
    T = 720
    t_z = 4
    reject = [0]
    case = []
    # time_client = exp(a)
    time_client = 0
    # time_step += time_client
    time_work = []
    case = start(N, case)
    time_work = start(N, time_work)
    while time_client < T:
        rand_t = exp(a)
        # print("rand_t = ", rand_t)
        time_client += rand_t
        # print("time_client = ", time_client)
        model(time_client, t_z, case, time_work, reject)

    print("Время работы кассы = ", time_work)
    print("количество обработанных заявок = ", case)
    print("количество потерянных покупателей = ", reject)