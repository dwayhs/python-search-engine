from py_search_engine.analysis.filters import (SimpleNormalizeFilter,
                                               SimpleTokenizer)

from .base_analyzer import BaseAnalyzer


class SimpleAnalyzer(BaseAnalyzer):
    PIPELINE = [
        SimpleNormalizeFilter,
        SimpleTokenizer
    ]
