import unittest
import pytest
from helpers import *


class MyTestCase(unittest.TestCase):
    def test_get_names_from_url(self):
        url = "https://finance.yahoo.com/?guccounter=1&guce_referrer=aHR0cHM6Ly93d3cuZ29vZ2xlLmNvbS8&guce" \
              "_referrer_sig=AQAAAFtqSeNfJLpJ916YN0alaOJvdbwRK8ws1y5EAUiLmYVu71uIU66KuPoVhn_prCSjUdpU7_KKi" \
              "Rxc5VHfLfrSe4pkxT7Mfv7zn7Pvv-b8v7HqGEnWFRqb_ewJ0zSFBji-cuHwlIPHHxp6coxHrX11o9PJHq5_JIOd8JZYiHv-0-w2"
        parts = get_names_from_url(url)
        self.assertEqual(parts, [['yahoo', 'finance'], ['guccounter1guce']])
        self.assertEqual(len(parts), 2)
        self.assertEqual(len(parts[0]), 2)
        self.assertEqual(len(parts[1]), 1)

        for list_ in parts:
            for part in list_:
                self.assertEqual(len(part) < 16, True)

        url = "https://secure.dc7.pageuppeople.com/apply/671/cw/applicationForm/default.asp?lStatusID=2&sLanguage="
        wanted = [['pageuppeople', 'dc7', 'secure'], ['apply', "671", "cw", "applicationForm", "defaultasplStat"]]
        parts = get_names_from_url(url)
        self.assertEqual(parts, wanted)
        self.assertEqual(len(parts), 2)
        self.assertEqual(len(parts[0]), 3)
        self.assertEqual(len(parts[1]), 5)

        for list_ in parts:
            for part in list_:
                self.assertEqual(len(part) < 16, True)

        url = "app\\build\\generated\\source\\navigation-args\\debug\\navgraphdirections.kt: (7, 33):" \
              " unresolved reference: r"
        with pytest.raises(ValueError):
            parts = get_names_from_url(url)


def test_string_is_url():
    # valid URLs with different schemes and netlocs
    assert string_is_url("http://www.example.com")
    assert string_is_url("https://example.org")
    assert string_is_url("https://example.com/path/with?query=parameters")

    # valid URLs with different ports and paths
    assert string_is_url("http://example.com:8080")
    assert string_is_url("https://example.com/path/to/resource.html")

    # URLs with invalid characters or special characters
    assert not string_is_url("http://example.com/path/with spaces")
    assert not string_is_url("ftp://example.com/path#fragment")
    assert not string_is_url("http://example.com/path/<script>alert('xss'){}</script>")
    assert not string_is_url("ftp://ftp.example.net")
    assert not string_is_url("mailto:user@example.com")

    # invalid URLs
    assert not string_is_url("example.com")
    assert not string_is_url("http://")
    assert not string_is_url("not a url")

    # URLs with unicode characters
    assert string_is_url("https://ja.wikipedia.org/wiki/メインページ")
    assert string_is_url("https://fr.wikipedia.org/wiki/Électricité")


def test_find_changed_parts():
    assert find_changed_parts("hello", "hillo") == "i"
    assert find_changed_parts("abc", "def") == "def"
    assert find_changed_parts("same", "same") == ""
    assert find_changed_parts("", "") == ""
    assert find_changed_parts("longerstring", "short") == "short"


if __name__ == '__main__':
    unittest.main()
