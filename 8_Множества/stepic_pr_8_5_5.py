import decimal
from decimal import Decimal
n = int(input())
lines = [ input().split(": ") for _ in range(n)]
attempts = len(lines)
right_attempts = 0
students_with_right_answer = set()
for i in lines:
    if i[1] == "Correct":
        right_attempts += 1
        students_with_right_answer.add(i[0])
if attempts != 0:
    procent = right_attempts / attempts * 100
if right_attempts == 0:
    print("Вы можете стать первым, кто решит эту задачу")
else:
    print(f"Верно решили {len(students_with_right_answer)} учащихся")
    print(f"Из всех попыток {Decimal(f"{procent}").quantize(Decimal("1"), decimal.ROUND_HALF_UP)}% верных")

