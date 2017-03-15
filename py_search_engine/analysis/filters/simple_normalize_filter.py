import re

from unidecode import unidecode

from .base_filter import BaseFilter


class SimpleNormalizeFilter(BaseFilter):
    def process_term(self, term):
        return [re.sub('[^A-Za-z0-9]+', '', unidecode(term))]
