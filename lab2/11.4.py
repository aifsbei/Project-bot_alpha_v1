n_number_of_strings = int(input())
for i in range(n_number_of_strings):
    string = input()
    number_of_letter = 0
    to_delete = []
    is_beginning = True
    is_text_in_quotes = False
    is_a_comment = False
    first_s = False
    second_s = False
    for char in string:
        number_of_letter += 1
        if is_beginning:
            if char == ' ':
                continue
            else:
                is_beginning = False
        else:
            if not is_text_in_quotes:
                if char == '\'':
                    is_text_in_quotes = True
                if char == ' ':
                    if string[number_of_letter] == ' ':
                        to_delete.append(number_of_letter)
                if char == '#':
                    string = string[:number_of_letter - 1]
                    break
            else:
                if (char == '\'' and first_s and second_s) or (char == '\'' and not first_s):
                    is_text_in_quotes = False
                if char == '\\':
                    if not first_s:
                        first_s = True
                    elif not second_s:
                        second_s = True
                else:
                    first_s = False
                    second_s = False
    count_of_deleted_symbols = 0
    for ix in to_delete:
        string = string[:ix - count_of_deleted_symbols - 1] + string[ix - count_of_deleted_symbols:]
        count_of_deleted_symbols += 1
    print(string)