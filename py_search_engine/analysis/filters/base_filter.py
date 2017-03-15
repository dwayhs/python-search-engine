class BaseFilter:
    def __init__(self, tokens_list):
        self.tokens_list = tokens_list

    def process(self):
        processed_terms = []

        for term, position in self.tokens_list:
            processed_term_list = self.process_term(term)

            processed_term_list = [(processed_term, position)
                                   for processed_term in processed_term_list]

            processed_terms += processed_term_list

        return processed_terms

    def process_term(self, term):
        raise NotImplementedError
