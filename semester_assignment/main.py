import time
from simulated_annealing import *


def separator():
  print("\n>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n")


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
  random.shuffle(init_order)

  # INITIALIZATION
  start_time = time.time()
  jobs = jobs_input(jobs_num, machines_num)
  order = simulated_annealing(jobs, init_order, object_function, iteration_num, 100, init_temperature, jobs_num,
                              machines_num, cooling_strategy)
  result = object_function(jobs, order, jobs_num, machines_num)
  deadlines = calculate_deadlines(machines_num, result["c_max"], jobs_num, jobs, result["job_end"])

  # PRINTING OUT THE RESULTS
  separator()

  print_flow_shop(machines_num, jobs_num, result["job_begin"], result["job_end"])

  print_deadlines_table(deadlines["end_times"], jobs, deadlines["jobs_l"], deadlines["jobs_t"], deadlines["deadlines"])

  print(f"Initial order: {init_order}")
  print(f"Best order: {order}\n")

  print(f"C-max: {result['c_max']}\n")

  print(f"Runtime with {cooling_stategy_name(cooling_strategy)}: {round(time.time() - start_time, 4)} sec")

  # EXAMPLE DATA FROM THE ASSIGNMENT
  # s = [1, 2, 3, 4, 5]
  # test = object_function(jobs, s, jobs_num, machines_num)
  # print_flow_shop(machines_num, jobs_num, test["job_begin"], test["job_end"])
  # print("c_max: ", test["c_max"])
  # d = calculate_deadlines(machines_num, test["c_max"], jobs_num, jobs, test["job_end"])
  # print_deadlines_table(d["end_times"], jobs, d["jobs_l"], d["jobs_t"], d["deadlines"])


main()
