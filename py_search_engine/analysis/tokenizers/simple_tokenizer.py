class SimpleTokenizer:
    def __init__(self, term):
        self.term = term

    def tokenize(self):
        terms_list = self.term.split(' ')

        return [(term, position)
                for position, term
                in enumerate(terms_list)]
