import random


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
