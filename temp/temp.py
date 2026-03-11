# logs = ["210", "211", "210", "ERROR", "212", "215", "ERROR", "214"]

# def average_temperature(logs):
#     total = 0
#     count = 0
#     for log in logs:
#         if log.isdigit():  # only consider valid temperature readings
#     #   if log != "ERROR":  # if we want to exclude "ERROR" entries
#             total += int(log)
#             count += 1
            
#     return total / count if count > 0 else 0

# avg_temp = average_temperature(logs)
# print(f"Average Temperature: {avg_temp: .2f}")

import sympy as sp

sorted(sp.functions.__all__)