class BaseFilter:
    def __init__(self, input_list):
        self.input_list = input_list

    def process(self):
        # TODO: optimize
        processed_terms = []

        for term in self.input_list:
            processed_terms += self._process_term(term)

        return processed_terms

    def _process_term(self, item):
        raise NotImplementedError

    def _flatten(self, token_list):
        return [token for token_sublist in token_list for token in token_sublist]