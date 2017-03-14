from py_search_engine.analysis.filters import (LowercaseFilter,
                                               SimpleNormalizeFilter,
                                               SimpleTokenizer)

from .base_analyzer import BaseAnalyzer


class SimpleAnalyzer(BaseAnalyzer):
    PIPELINE = [
        LowercaseFilter,
        SimpleNormalizeFilter,
        SimpleTokenizer
    ]
