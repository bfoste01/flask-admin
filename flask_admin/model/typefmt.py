from jinja2 import Markup
from flask.ext.admin._compat import text_type


def null_formatter(view, value):
    """
        Return `NULL` as the string for `None` value

        :param value:
            Value to check
    """
    return Markup('<i>NULL</i>')


def empty_formatter(view, value):
    """
        Return empty string for `None` value

        :param value:
            Value to check
    """
    return ''


def bool_formatter(view, value):
    """
        Return check icon if value is `True` or empty string otherwise.

        :param value:
            Value to check
    """
    glyph = 'ok-circle' if value else 'minus-sign'
    return Markup('<span class="glyphicon glyphicon-%s"></span>' % glyph)


def list_formatter(view, values):
    """
        Return string with comma separated values

        :param values:
            Value to check
    """
    return u', '.join(text_type(v) for v in values)


BASE_FORMATTERS = {
    type(None): empty_formatter,
    bool: bool_formatter,
    list: list_formatter,
}
