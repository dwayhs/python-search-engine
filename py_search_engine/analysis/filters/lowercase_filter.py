from .base_filter import BaseFilter


class LowercaseFilter(BaseFilter):
    def process_term(self, term):
        return [term.lower()]
