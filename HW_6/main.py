import chess_module

successful_arrangements = chess_module.generate_random_queens()

if len(successful_arrangements) > 0:
    print("Успешные расстановки:")
    for arrangement in successful_arrangements:
        print(arrangement)
else:
    print("Нет удачных расстановок.")
