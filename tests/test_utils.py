from collections import defaultdict

from language_detection import utils

class TestUtils:
    def test_merge_dictionaries_summing(self):
        dict_a = {'a': 5, 'b': 0, 'c': 13}
        defaultdict_a = defaultdict(int)

        for k, v in dict_a.items():
            defaultdict_a[k] = v

        dict_b = {'a': 2, 'c': 1, 'd': 4}
        defaultdict_b = defaultdict(int)
        for k, v in dict_b.items():
            defaultdict_b[k] = v

        dict_expected = {'a': 7, 'b': 0, 'c': 14, 'd': 4}
        defaultdict_expected = defaultdict(int)
        for k, v in dict_expected.items():
            defaultdict_expected[k] = v

        assert utils.merge_dictionaries_summing(defaultdict_a, defaultdict_b) == defaultdict_expected
