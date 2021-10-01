PLACEHOLDER = "[name]"


with open('./Input/Names/invited_names.txt') as names:
    list_of_names = names.readlines()

with open('./Input/Letters/starting_letter.txt') as letter:
    starting_letter = letter.read()
    for name in list_of_names:
        stripped = name.strip()
        new_letter = starting_letter.replace(PLACEHOLDER, stripped)
        with open(f'./Output/ReadyToSend/letter_for_{stripped}.txt', mode='w') as letter_file:
            letter_file.write(new_letter)
