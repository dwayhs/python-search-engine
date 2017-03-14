from .base_filter import BaseFilter


class SimpleTokenizer(BaseFilter):
    def _process_term(self, term):
        return term.split(' ')
