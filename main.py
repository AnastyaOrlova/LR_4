import random
import math

def rand():
    y = random.uniform(0, 1)

    return y

def exp(a):
    y = rand()
    rand_t = -1 / a * math.log(y)

    return rand_t

def start (N, case):
    for i in range (N):
        case.append(0)

    return case

def model(time_client, t_z, case, time_work, reject, rand_t):
    for i in range(len(time_work)):
        if time_work[i] <= time_client:
            time_work[i] += rand_t + t_z
            case[i] += 1
            break
        if i == len(time_work) - 1:
            reject[0] += 1



def iteration(time_client, T, time_work, case):
    while time_client < T:
        rand_t = exp(a)
        time_client += rand_t
        # print(time_client)
        model(time_client, t_z, case, time_work, reject, rand_t)
    print("Время работы кассы = ", time_work)
    print("количество обработанных заявок = ", case)
    print("количество потерянных покупателей = ", reject)
    return case, time_work, reject

# def average(work, time_work):
#     for i in range(len(time_work)):
#         work[i] += time_work[i]
#     return work

def div(work, iterate):
    for i in range(len(work)):
        work[i] = work[i] / iterate

    return work

if __name__ == '__main__':
    iterate = 10
    for j in range(iterate):
        N = 10
        a = 1
        T = 720
        t_z = 4
        time_client = 0
        case = []
        count = []
        time_work = []
        work = []
        rej = [0]
        work = start(N, work)
        count = start(N, count)
        reject = [0]
        case = start(N, case)
        time_work = start(N, time_work)
        iteration(time_client, T, time_work, case)
        for i in range(len(time_work)):
            work[i] += time_work[i]
            count[i] += case[i]
        for i in range(len(reject)):
            rej += reject[i]

        print(work)
        print(count)
        print(rej)


    work = div(work, iterate)
    count = div(count, iterate)
    rej = div(rej, iterate)


    print("Cреднее время работы кассы = ", work)
    print("Среднее количество обработанных заявок = ", count)
    print("Среднее количество потерянных покупателей = ", rej)