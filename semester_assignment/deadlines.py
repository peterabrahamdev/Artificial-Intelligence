import random


def generate_deadlines(machines_num, jobs_num, deadline_length):
  deadlines = [
    random.randint(round(deadline_length / 5), deadline_length) for i in range(jobs_num)
    # randomly generating deadlines
    # 25, 30, 30, 45, 30
  ]

  return deadlines


def calculate_deadlines(jobs, job_end, deadlines):
  end_times = job_end[len(job_end) - 1]

  jobs_l = []
  for i in range(len(jobs)):
    jobs_l.append(end_times[i] - deadlines[i])

  jobs_t = []
  for i in range(len(jobs)):
    jobs_t.append(max(0, end_times[i] - deadlines[i]))

  return {"end_times": end_times, "jobs_l": jobs_l, "jobs_t": jobs_t, "deadlines": deadlines, "jobs": jobs,
          "t_sum": sum(jobs_t)}


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
