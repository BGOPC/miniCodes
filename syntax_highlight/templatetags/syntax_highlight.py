from django import template
from pygments import highlight
from pygments.lexers import get_lexer_by_name
from pygments.formatters import HtmlFormatter

register = template.Library()


@register.filter
def syntax_highlight(code, language):
    language_mapping = {
        "TXT": "text",
        "PY": "python",
        "JS": "javascript",
        "C": "c",
        "CPP": "cpp",
        "CS": "csharp",
        "JV": "java",
    }
    lexer = get_lexer_by_name(language_mapping.get(language, "text"))
    formatter = HtmlFormatter(style='colorful')
    highlighted_code = highlight(code, lexer, formatter)
    return highlighted_code
