import random


def scramble(plain_password):
    password_list = random.sample(plain_password, len(plain_password))
    print("".join(password_list))
    return


def character_selector(low_range, high_range, count=2):
    characters = ""
    temp_list = random.sample(range(low_range, high_range+1), k=count)
    for num in temp_list:
        characters += chr(num)
    return characters


if __name__ == "__main__":
    new_password = ""
    new_password += character_selector(97, 122, 9)
    new_password += character_selector(65, 90, 4)
    new_password += character_selector(48, 57, 3)
    new_password += character_selector(35, 38, 2)
    new_password += character_selector(48, 57, 5)
    scramble(new_password)
