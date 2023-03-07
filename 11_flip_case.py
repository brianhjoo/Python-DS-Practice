def flip_case(phrase, to_swap):
    """Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'

    """
    results = []

    for letter in phrase:
        if letter.lower() == to_swap.lower():
            results.append(letter.swapcase())
        else:
            results.append(letter)
    return "".join(results)