def validUTF8(dataset):
    continuations = 0
    for character in dataset:
        valid_character = False
        if valid_one_byte_pattern(character) and continuations == 0:
            valid_character = True

        elif valid_two_byte_heading(character):
            if continuations != 0:
                valid_character = False
            else:
                continuations = 1

        elif valid_three_byte_heading(character):
            if continuations != 0:
                valid_character = False
            else:
                continuations = 2

        elif valid_four_byte_heading(character):
            if continuations != 0:
                valid_character = False
            else:
                continuations = 3

        elif valid_continuation(character):
            if continuations != 0:
                valid_character = True
                continuations = continuations - 1
            else:
                valid_character = False

        if not valid_character:
            return False
    return True


def shift_check(num, prefix, prefix_length):
    # Shift the number to the right so that only the first n bits remain

    num_length = num.bit_length()
    shift_amount = num_length - prefix_length
    leading_bits = num >> shift_amount

    if leading_bits == prefix:
        return True
    else:
        return False


def valid_one_byte_pattern(character):
    if character < 128 and character >= 0:
        return True
    return False


def valid_two_byte_heading(character):
    num = character
    prefix = 0b110
    prefix_length = 3

    return shift_check(num, prefix, prefix_length)


def valid_three_byte_heading(character):
    num = character
    prefix = 0b1110
    prefix_length = 4

    return shift_check(num, prefix, prefix_length)


def valid_four_byte_heading(character):
    num = character
    prefix = 0b11110
    prefix_length = 5

    return shift_check(num, prefix, prefix_length)


def valid_continuation(character):

    num = character
    prefix = 0b10
    prefix_length = 2

    return shift_check(num, prefix, prefix_length)
