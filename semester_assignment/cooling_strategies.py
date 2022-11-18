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
