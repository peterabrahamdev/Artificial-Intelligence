import random
import time
from cooling_strategies import *


def separator():
  print("\n>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n")


def inprint_separator():
  return "\n>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n"


def print_flow_shop(machines_num, jobs_num, job_begin, job_end):
  represent_job = []  # the job's number
  for i in range(jobs_num):
    represent_job.append(i + 1)

  # printing the Gantt chart
  print("FLOW-SHOP GANTT CHART:\n")
  for i in range(machines_num):
    for j in range(0, jobs_num):
      if (j == 0 and job_begin[i][j] != 0):
        print((job_begin[i][j]) * "-|", end="")
      if (j < jobs_num - 1):
        print((job_end[i][j] - job_begin[i][j]) * f"{represent_job[j]}|", end="")
        print((job_begin[i][j + 1] - job_end[i][j]) * "-|", end="")
      if (j == jobs_num - 1):
        print((job_end[i][j] - job_begin[i][j]) * f"{represent_job[j]}|", end="")
    print("\n")


def jobs_input(jobs_num, machines_num):
  jobs = [[0 for i in range(machines_num)] for y in range(
    jobs_num)]  # it's a two-dimensional array where an array stores a random generated number which is the job's length
  for i in range(jobs_num):
    for j in range(machines_num):
      jobs[i][j] = (random.randint(1, 8))
  # jobs = [
  #   [3, 4, 6, 7],
  #   [4, 5, 4, 6],
  #   [8, 7, 2, 2],
  #   [5, 3, 1, 5],
  #   [7, 6, 8, 4]
  # ]
  return jobs


def object_function(jobs, order, jobs_num, machines_num):
  job_begin = [[0 for x in range(jobs_num)] for y in range(machines_num)]  # stores the starting points of the jobs
  job_end = [[0 for x in range(jobs_num)] for y in range(machines_num)]  # stores the end points of the jobs
  cost = [0 for i in range(jobs_num)]  #
  for i in range(0, machines_num):
    for j in range(0, jobs_num):
      c_max = cost[j]
      if j > 0:
        c_max = max(cost[j - 1], cost[j])
      cost[j] = c_max + jobs[order[j] - 1][i]
      job_end[i][j] = cost[j]
      job_begin[i][j] = job_end[i][j] - jobs[order[j] - 1][i]
      c_max = job_end[i][j]

  return {"c_max": c_max, "job_begin": job_begin, "job_end": job_end}


def calculate_deadlines(machines_num, c_max, jobs_num, jobs, job_end):
  deadlines = [
    random.randint(machines_num * 3, c_max) for i in range(jobs_num)  # randomly generating deadlines
    # 25, 30, 30, 45, 30
  ]

  end_times = job_end[len(job_end) - 1]

  jobs_l = []
  for i in range(len(jobs)):
    jobs_l.append(end_times[i] - deadlines[i])

  jobs_t = []
  for i in range(len(jobs)):
    jobs_t.append(max(0, end_times[i] - deadlines[i]))

  return {"end_times": end_times, "jobs_l": jobs_l, "jobs_t": jobs_t, "deadlines": deadlines, "jobs": jobs}


def print_deadlines_table(end_times, jobs, jobs_l, jobs_t, deadlines):
  separator()
  print("DEADLINE TABLE:\n")

  print("{:>}\t\t{:>4}\t\t{:>4}\t\t{:>4}\t\t{:>4}".format("Ji", "Ci", "di", "Li", "Ti"))
  print("------------------------------------------------")
  for i in range(len(jobs)):
    print(
      "{:>}\t\t{:>4}\t\t{:>4}\t\t{:>4}\t\t{:>4}".format(f"J{i + 1}", end_times[i], deadlines[i], jobs_l[i],
                                                        jobs_t[i]))

  print("------------------------------------------------")
  print("{:>}\t\t\t\t\t\t\t\t{:>4}\t\t{:>4}".format("SUM", sum(jobs_l), sum(jobs_t)))
  separator()


def probability(t_star, f_st, temp):
  expon = (t_star - f_st) / temp
  return math.exp(-expon)


def choose_cooling_strategy(cooling_strategy, f_star, f_si, t0, alpha, t):
  if (cooling_strategy == 1):
    temp = temp_lin_mult(t0, alpha, t)
  elif (cooling_strategy == 2):
    temp = temp_lin_mult2(t0, alpha, t)
  elif (cooling_strategy == 3):
    temp = temp_exp_mult(t0, alpha, t)
  elif (cooling_strategy == 4):
    temp = temp_log_mult(t0, alpha, t)
  elif (cooling_strategy == 5):
    temp = temp_non_monotonic(f_star, f_si, t0, alpha, t)
  return temp


def cooling_stategy_name(cooling_strategy):
  if (cooling_strategy == 1):
    name = "Linear Multiplicative Type 1"
  elif (cooling_strategy == 2):
    name = "Linear Multiplicative Type 2"
  elif (cooling_strategy == 3):
    name = "Exponential Multiplicative"
  elif (cooling_strategy == 4):
    name = "Logarithmical Multiplicative"
  elif (cooling_strategy == 5):
    name = "Non-monotonic"
  return name


def simulated_annealing(jobs, s, object_f, iterations, neighbors, t0, jobs_num, machines_num, cooling_strategy):
  s_best = list(s)  # stores the best order of jobs
  f_best = object_f(jobs, s_best, jobs_num, machines_num)['c_max']  # stores the best Cmax
  s_base = list(s_best)
  f_base = f_best
  t = 0  # represents time
  alpha = 0.8  # alpha (should be between 0.8 - 0.9)
  try:
    for i in range(iterations):
      s_best_neighbor = list(s_base)
      f_best_neighbor = f_base
      for j in range(neighbors):
        t += 1
        s_neighbor = list(s_base)
        a = random.randint(0, len(s) - 1)
        b = random.randint(0, len(s) - 1)
        s_neighbor[a], s_neighbor[b] = s_neighbor[b], s_neighbor[a]
        f_neighbor = object_f(jobs, s_neighbor, jobs_num, machines_num)['c_max']

        # -- START SIMULATED ANNEALING --
        if f_neighbor < f_best_neighbor:
          f_best_neighbor = f_neighbor
          s_best_neighbor = s_neighbor
        else:
          temp = choose_cooling_strategy(cooling_strategy, f_best_neighbor, f_neighbor, t0, alpha, t)
          prob = probability(f_best_neighbor, f_neighbor, temp)
          randProb = random.randint(0, 98)
          if randProb < prob * 100:
            f_best_neighbor = f_neighbor
            s_best_neighbor = s_neighbor
        # -- END SIMULATED ANNEALING --
  except(OverflowError):
    print(f"\n!!! Overflow Error - Exited at: {t}/{iterations * neighbors} !!!")
  s_base = s_best_neighbor
  f_base = f_best_neighbor
  if f_base < f_best:
    f_best = f_base
    s_best = s_base
  separator()
  print(f"Best order: {s_best}")
  separator()

  return s_best


def main():
  # INPUTS
  jobs_num = int(input("Number of Jobs: "))
  machines_num = int(input("Number of Machines: "))
  iteration_num = int(input("Number of Iterations: "))
  print("============================",
        "\nCOOLING STRATEGIES\n1 | Linear Multiplicative Type 1\n2 | Linear Multiplicative Type 2 (ERROR)\n3 | Exponential Multiplicative (ERROR)\n4 | Logarithmical Multiplicative\n5 | Non-monotonic",
        "\n============================", )
  cooling_strategy = int(input("Number of the cooling strategy: "))
  init_temperature = int(input("Initial temperature: "))

  # ARRANGING INPUTS
  init_order = list(range(1, jobs_num + 1))
  st = time.time()
  random.shuffle(init_order)

  # INITIALIZATION
  start_time = time.time()
  jobs = jobs_input(jobs_num, machines_num)
  order = simulated_annealing(jobs, init_order, object_function, iteration_num, 100, init_temperature, jobs_num,
                              machines_num, cooling_strategy)
  result = object_function(jobs, order, jobs_num, machines_num)
  deadlines = calculate_deadlines(machines_num, result["c_max"], jobs_num, jobs, result["job_end"])

  # PRINTING OUT THE RESULTS

  print_flow_shop(machines_num, jobs_num, result["job_begin"], result["job_end"])

  print_deadlines_table(deadlines["end_times"], jobs, deadlines["jobs_l"], deadlines["jobs_t"], deadlines["deadlines"])

  print(f"C-max: {result['c_max']}")

  print(f"Runtime with {cooling_stategy_name(cooling_strategy)}: {round(time.time() - start_time, 4)} sec")

  # EXAMPLE DATA FROM THE ASSIGNMENT
  # s = [1, 2, 3, 4, 5]
  # test = object_function(jobs, s, jobs_num, machines_num)
  # print_flow_shop(machines_num, jobs_num, test["job_begin"], test["job_end"])
  # print("c_max: ", test["c_max"])
  # d = calculate_deadlines(machines_num, test["c_max"], jobs_num, jobs, test["job_end"])
  # print_deadlines_table(d["end_times"], jobs, d["jobs_l"], d["jobs_t"], d["deadlines"])


main()
