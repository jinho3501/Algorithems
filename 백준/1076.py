resistor_values = {
    "black": (0, 1),
    "brown": (1, 10),
    "red": (2, 100),
    "orange": (3, 1_000),
    "yellow": (4, 10_000),
    "green": (5, 100_000),
    "blue": (6, 1_000_000),
    "violet": (7, 10_000_000),
    "grey": (8, 100_000_000),
    "white": (9, 1_000_000_000)
}

def calculate_resistance():
    colors = []
    for i in range(3):
        color = input().strip().lower()
        colors.append(color)
    if any(color not in resistor_values for color in colors):
        print("❌ 잘못된 색상이 포함되어 있습니다. 다시 입력해주세요.")
        return

    first_digit = resistor_values[colors[0]][0]
    second_digit = resistor_values[colors[1]][0]
    multiplier = resistor_values[colors[2]][1]
    resistance_value = (first_digit * 10 + second_digit) * multiplier
    print(f"{resistance_value}")

calculate_resistance()