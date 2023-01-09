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

def model(time_client, t_z, case, time_work, reject, rand_t):
    for i in range(len(time_work)):
        if time_work[i] <= time_client:
            time_work[i] += time_client - time_work[i] + t_z
            case[i] += 1
            break
        if i == len(time_work) - 1:
            reject[0] += 1

    return case, time_work, reject

def iteration(time_client):
    while time_client < T:
        rand_t = exp(a)
        time_client += rand_t
        model(time_client, t_z, case, time_work, reject, rand_t)

    return case, time_work, reject

def average(work, time_work):
    for i in range(len(time_work)):
        work[i] = work[i] + time_work[i]

    return work

def div(work, iterate):
    for i in range(len(work)):
        work[i] = work[i]/iterate

    return work

if __name__ == '__main__':
    iterate = 1000
    N = 20
    a = 1
    T = 720
    t_z = 4

    count = []
    work = []
    rej = [0]
    work = start(N, work)
    count = start(N, count)
    j = 1
    while j <= iterate:
        j += 1
        time_client = 0
        case = []
        case = start(N, case)
        time_work = []
        reject = [0]
        time_work = start(N, time_work)
        iteration(time_client)
        work = average(work, time_work)
        count = average(count, case)
        rej = average(rej, reject)

    work = div(work, iterate)
    count = div(count, iterate)
    rej = div(rej, iterate)

    print("Cреднее время работы кассы = ", work)
    print("Среднее количество обработанных заявок = ", count)
    print("Среднее количество потерянных покупателей = ", rej)