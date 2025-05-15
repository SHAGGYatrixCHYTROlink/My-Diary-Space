
# zakladni one vstup funkce
def get_input_from_user(text="input"):
    user_intup = input(f"{text}\n")
    return user_intup
# Vymenit za funkci z testspace
def get_user_inputs(loops_number):
    user_inputs = []
    for loop in range(loops_number):
        user_input = get_input_from_user()
        user_inputs.append(user_input)
    return user_inputs
