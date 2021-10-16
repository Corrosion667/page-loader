"""This is a main testing module of the project."""


from page_loader.naming import get_name


def test_get_name():
    """Test for checking naming parsing of web page URL."""
    assert get_name(
        'https://ru.hexlet.io/courses',
    ) == 'ru-hexlet-io-courses.html'
