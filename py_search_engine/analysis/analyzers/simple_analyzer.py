from py_search_engine.analysis.filters import (LowercaseFilter,
                                               SimpleNormalizeFilter)
from py_search_engine.analysis.tokenizers import SimpleTokenizer

from .base_analyzer import BaseAnalyzer


class SimpleAnalyzer(BaseAnalyzer):
    TOKENIZER = SimpleTokenizer
    FILTERS = [
        LowercaseFilter,
        SimpleNormalizeFilter
    ]
