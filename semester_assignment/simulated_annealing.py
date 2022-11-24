from cooling_strategies import *
from flow_shop import *


def probability(t_star, f_st, temp):
  expon = (t_star - f_st) / temp
  return math.exp(-expon)


def simulated_annealing_tsum(jobs, s, object_f, iterations, neighbors, t0, jobs_num, machines_num, cooling_strategy,
                             deadlines):
  try:
    s_best = list(s)  # stores the best order of jobs
    f_best = object_f(jobs, s_best, jobs_num, machines_num, deadlines)['t_sum']  # stores the best Tsum
    s_base = list(s_best)
    f_base = f_best
    t = 0  # represents time
    alpha = 0.8  # alpha (should be between 0.8 - 0.9)
    for i in range(iterations):
      s_best_neighbor = list(s_base)
      f_best_neighbor = f_base
      for j in range(neighbors):
        t += 1
        s_neighbor = list(s_base)
        a = random.randint(0, len(s) - 1)
        b = random.randint(0, len(s) - 1)
        s_neighbor[a], s_neighbor[b] = s_neighbor[b], s_neighbor[a]
        f_neighbor = object_f(jobs, s_neighbor, jobs_num, machines_num, deadlines)['t_sum']
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
      s_base = s_best_neighbor
      f_base = f_best_neighbor
      if f_base < f_best:
        f_best = f_base
        s_best = s_base
  except(OverflowError):
    print(f"\n!!! Overflow Error - Exited at: {t}/{iterations * neighbors} !!!")
  return s_best


def simulated_annealing_cmax(jobs, s, object_f, iterations, neighbors, t0, jobs_num, machines_num, cooling_strategy,
                             deadlines):
  try:
    s_best = list(s)  # stores the best order of jobs
    f_best = object_f(jobs, s_best, jobs_num, machines_num, deadlines)['c_max']  # stores the best Cmax
    s_base = list(s_best)
    f_base = f_best
    t = 0  # represents time
    alpha = 0.8  # alpha (should be between 0.8 - 0.9)
    for i in range(iterations):
      s_best_neighbor = list(s_base)
      f_best_neighbor = f_base
      for j in range(neighbors):
        t += 1
        s_neighbor = list(s_base)
        a = random.randint(0, len(s) - 1)
        b = random.randint(0, len(s) - 1)
        s_neighbor[a], s_neighbor[b] = s_neighbor[b], s_neighbor[a]
        f_neighbor = object_f(jobs, s_neighbor, jobs_num, machines_num, deadlines)['c_max']
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
      s_base = s_best_neighbor
      f_base = f_best_neighbor
      if f_base < f_best:
        f_best = f_base
        s_best = s_base
  except(OverflowError):
    print(f"\n!!! Overflow Error - Exited at: {t}/{iterations * neighbors} !!!")
  return s_best
