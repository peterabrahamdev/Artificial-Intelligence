import math

def temp_lin_mult(t0, alpha, t):
  return t0 / (1 + (alpha * t))


def temp_lin_mult2(t0, alpha, t):
  return t0 / (1 + alpha * (t ** 2))


def temp_exp_mult(t0, alpha, t):
  return t0 * (alpha ** t)


def temp_log_mult(t0, alpha, t):
  return t0 / (1 + alpha * math.log(1) + t)


def temp_non_monotonic(f_star, f_si, t0, alpha, t):
  return (1 + ((f_si - f_star) / f_si)) * temp_lin_mult(t0, alpha, t)

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
