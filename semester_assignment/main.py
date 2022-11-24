import time
from simulated_annealing import *
from flow_shop import *
from cooling_strategies import *
from deadlines import *


def separator():
  print("\n>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n")


def main():
  # INPUTS
  jobs_num = int(input("Number of Jobs: "))
  machines_num = int(input("Number of Machines: "))
  iteration_num = int(input("Number of Iterations: "))
  print("============================",
        "\nCOOLING STRATEGIES\n1 | Linear Multiplicative Type 1\n2 | Linear Multiplicative Type 2\n3 | Exponential Multiplicative\n4 | Logarithmical Multiplicative\n5 | Non-monotonic",
        "\n============================", )
  cooling_strategy = int(input("Number of the cooling strategy: "))
  init_temperature = int(input("Initial temperature: "))

  # ARRANGING INPUTS
  init_order = list(range(1, jobs_num + 1))
  random.shuffle(init_order)

  # INITIALIZATION
  start_time = time.time()
  jobs = jobs_input(jobs_num, machines_num)
  gen_deadlines = generate_deadlines(machines_num, jobs_num, deadline_length(jobs, init_order, jobs_num, machines_num))
  order = simulated_annealing_cmax(jobs, init_order, object_function, iteration_num, 100, init_temperature, jobs_num,
                                   machines_num, cooling_strategy, gen_deadlines)
  order2 = simulated_annealing_tsum(jobs, init_order, object_function, iteration_num, 100, init_temperature, jobs_num,
                                    machines_num, cooling_strategy, gen_deadlines)
  result = object_function(jobs, order, jobs_num, machines_num, gen_deadlines)
  result2 = object_function(jobs, order2, jobs_num, machines_num, gen_deadlines)
  deadlines = calculate_deadlines(jobs, result["job_end"], gen_deadlines)
  deadlines2 = calculate_deadlines(jobs, result2["job_end"], gen_deadlines)

  # PRINTING OUT THE RESULTS
  separator()
  print("CMAX", end=" ")
  print_flow_shop(machines_num, jobs_num, result["job_begin"], result["job_end"])

  separator()
  print("ΣTi", end=" ")
  print_flow_shop(machines_num, jobs_num, result2["job_begin"], result2["job_end"])

  separator()
  print("CMAX", end=" ")
  print_deadlines_table(deadlines["end_times"], jobs, deadlines["jobs_l"], deadlines["jobs_t"], deadlines["deadlines"])

  separator()
  print("ΣTi", end=" ")
  print_deadlines_table(deadlines2["end_times"], jobs, deadlines2["jobs_l"], deadlines2["jobs_t"],
                        deadlines2["deadlines"])

  separator()
  print("Cmax data:\n")
  print(f"Initial order: {init_order}")
  print(f"Best order: {order}")
  print(f"C-max: {result['c_max']}")
  print(f"T-sum: {deadlines['t_sum']}")

  separator()
  print("ΣTi data:\n")
  print(f"Initial order: {init_order}")
  print(f"Best order: {order2}")
  print(f"C-max: {result2['c_max']}")
  print(f"T-sum: {deadlines2['t_sum']}")

  separator()
  print(f"Runtime with {cooling_stategy_name(cooling_strategy)}: {round(time.time() - start_time, 4)} sec")

  # EXAMPLE DATA FROM THE ASSIGNMENT
  # s = [1, 2, 3, 4, 5]
  # test = object_function(jobs, s, jobs_num, machines_num)
  # print_flow_shop(machines_num, jobs_num, test["job_begin"], test["job_end"])
  # print("c_max: ", test["c_max"])
  # d = calculate_deadlines(machines_num, test["c_max"], jobs_num, jobs, test["job_end"])
  # print_deadlines_table(d["end_times"], jobs, d["jobs_l"], d["jobs_t"], d["deadlines"])


main()
