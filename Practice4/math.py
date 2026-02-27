import math


deg = 15
rad = deg * math.pi / 180
print(f"1. {deg} degrees = {rad} radians")


h, a, b = 5, 5, 6
area_trap = (a + b) * h / 2
print(f"2. Area of trapezoid: {area_trap}")


n, s = 4, 25
area_poly = (n * s**2) / (4 * math.tan(math.pi / n))
print(f"3. Area of regular polygon: {area_poly}")


base, height = 5, 6
area_par = base * height
print(f"4. Area of parallelogram: {area_par}")