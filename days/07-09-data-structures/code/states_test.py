from states import (get_every_nth_state,
                    get_state_abbrev,
                    get_longest_state,
                    combine_state_names_and_abbreviations,
                    states,
                    us_state_abbrev,
                    NOT_FOUND)


def test_get_every_nth_state():
    expected = ['Massachusetts', 'Missouri', 'Hawaii',
                'Vermont', 'Delaware']
    assert list(get_every_nth_state()) == expected

    expected = ['Missouri', 'Vermont']
    assert list(get_every_nth_state(n=20)) == expected

def test_get_state_abbrev():
    expected = 'WI'
    assert get_state_abbrev('Wisconsin')

def test_get_longest_state():
    correct_answers = ('North Carolina','South Carolina')
    assert get_longest_state(states) in correct_answers
    assert get_longest_state(us_state_abbrev) in correct_answers

def test_combine_state_names_and_abbreviations():
    expected = ['AK', 'AL', 'AR', 'AZ', 'CA', 'CO', 'CT', 'DE', 'FL', 'GA',
                'South Dakota', 'Tennessee', 'Texas', 'Utah',
                'Vermont', 'Virginia', 'Washington', 'West Virginia',
                'Wisconsin', 'Wyoming']
    assert combine_state_names_and_abbreviations() == expected