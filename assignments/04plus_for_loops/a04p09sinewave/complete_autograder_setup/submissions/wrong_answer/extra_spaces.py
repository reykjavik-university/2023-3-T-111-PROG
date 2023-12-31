import math

number_of_waves = int(input())
number_of_lines = int(input())

radians_per_line = number_of_waves * 2 * math.pi / number_of_lines
semi_amplitude = 20

for line in range(number_of_lines):
    radians = line * radians_per_line
    number_of_xs = round(semi_amplitude + math.sin(radians) * semi_amplitude)
    text = "X" * number_of_xs + " " * (2 * semi_amplitude - number_of_xs)
    print(text)
