
PLACEHOLDER = "[name]"
with open("./Input/Names/invited_names.txt") as names_file:
    names = names_file.readlines()
    print(names)

with open("./Input/Letters/starting_letter.txt") as letter_file:
    letter_content = letter_file.read()
    for i,b in enumerate(names):
        text_replace = letter_content.replace(PLACEHOLDER,names[i].strip())
        with open(f"./Output/ReadyTosend/letter_for_{names[i].strip()}.docx","w") as completed_letter:
            completed_letter.write(text_replace)