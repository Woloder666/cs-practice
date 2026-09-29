threshold = float(input())
n = int(input())

errors = 0
exceedings = 0
total = 0.0
correct = 0

has_max = False
max_temp = 0.0

for i in range(n):
    s = input()

    if s == "error":
        errors += 1
    else:
        temp = float(s)

        total += temp
        correct += 1

        if temp > threshold:
            exceedings += 1

        if not has_max:
            max_temp = temp
            has_max = True
        elif temp > max_temp:
            max_temp = temp

average = total / correct

print(n)
print(errors)
print(exceedings)
print(f"{max_temp:.1f}")
print(f"{average:.1f}")
