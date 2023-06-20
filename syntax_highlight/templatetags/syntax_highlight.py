from django import template
from pygments import highlight
from pygments.lexers import get_lexer_by_name
from pygments.formatters import HtmlFormatter

register = template.Library()


@register.filter
def syntax_highlight(code, language):
    lexer = get_lexer_by_name(language)
    formatter = HtmlFormatter(style='colorful')
    highlighted_code = highlight(code, lexer, formatter)
    return highlighted_code
