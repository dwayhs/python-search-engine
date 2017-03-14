from .base_filter import BaseFilter


class LowercaseFilter(BaseFilter):
    def _process_term(self, term):
        return [term.lower()]
