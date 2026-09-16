#파이값구하기
import random

total_points = 10000000
inside_circle = 0

for _ in range(total_points):
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)

    if x**2 + y**2 <= 1:
        inside_circle += 1

pi_estimate = (inside_circle / total_points) * 4

print(f"시도 횟수: {total_points:,}회")
print(f"추정된 파이(π) 값: {pi_estimate}")