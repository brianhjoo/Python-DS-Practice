def multiple_letter_count(phrase):
    """Return dict of {ltr: frequency} from phrase.

        >>> multiple_letter_count('yay')
        {'y': 2, 'a': 1}

        >>> multiple_letter_count('Yay')
        {'Y': 1, 'a': 1, 'y': 1}
    """

    frequency_count = {}

    for letter in phrase:
        if letter in frequency_count:
            frequency_count[letter] += 1
        else:
            frequency_count[letter] = 1

        # frequency = frequency_count[letter] or 0
        # frequency_count[letter] = frequency + 1

    return frequency_count
