import time
from simulated_annealing import *
from flow_shop import *
from cooling_strategies import *

def separator():
  print("\n>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n")


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
  print("DEADLINE TABLE:\n")

  print("{:>}\t\t{:>4}\t\t{:>4}\t\t{:>4}\t\t{:>4}".format("Ji", "Ci", "di", "Li", "Ti"))
  print("------------------------------------------------")
  for i in range(len(jobs)):
    print(
      "{:>}\t\t{:>4}\t\t{:>4}\t\t{:>4}\t\t{:>4}".format(f"J{i + 1}", end_times[i], deadlines[i], jobs_l[i],
                                                        jobs_t[i]))

  print("------------------------------------------------")
  print("{:>}\t\t\t\t\t\t\t\t{:>4}\t\t{:>4}".format("SUM", sum(jobs_l), sum(jobs_t)))


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

  separator()

  print_deadlines_table(deadlines["end_times"], jobs, deadlines["jobs_l"], deadlines["jobs_t"], deadlines["deadlines"])

  separator()

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
