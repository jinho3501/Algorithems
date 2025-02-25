def calculate_gpa():
    total_points =0
    total_credits=0

    for i in range(20):
        score = input()
        parts = score.split()
        if parts[2] == "P":
            continue
        grade = parts[2]
        credits = float(parts[1])
        if grade == "A+":
            total_points += credits * 4.5
        elif grade == "A0":
            total_points += credits * 4.0
        elif grade == "B+":
            total_points += credits * 3.5
        elif grade == "B0":
            total_points += credits * 3.0
        elif grade == "C+":
            total_points += credits * 2.5
        elif grade == "C0":
            total_points += credits * 2.0
        elif grade == "D+":
            total_points += credits * 1.5
        elif grade == "D0":
            total_points += credits * 1.0
        elif grade == "F":
            total_points += credits * 0.0

        total_credits += credits
    if total_credits ==0:
        return 0
    return total_points / total_credits
gpa = calculate_gpa()
print(f"{gpa:.6f}")