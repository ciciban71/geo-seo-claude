"""
Translation loader for multi-language PDF report generation.
Supports: English (en), Arabic (ar), Serbian Latin (sr).
"""

from translations import en, ar, sr

LANGUAGES = {'en': en.STRINGS, 'ar': ar.STRINGS, 'sr': sr.STRINGS}

LANG_CONFIG = {
    'en': {'font': 'NotoSans', 'direction': 'ltr', 'alignment': 'left', 'date_fmt': '%B %d, %Y'},
    'ar': {'font': 'Amiri', 'direction': 'rtl', 'alignment': 'right', 'date_fmt': '%d/%m/%Y'},
    'sr': {'font': 'NotoSans', 'direction': 'ltr', 'alignment': 'left', 'date_fmt': '%d.%m.%Y.'},
}


def t(key, lang='en'):
    """Get translated string. Falls back to English."""
    return LANGUAGES.get(lang, LANGUAGES['en']).get(key, LANGUAGES['en'].get(key, key))
