class BaseAnalyzer:
    TOKENIZER = None
    FILTERS = []

    def analyze(self, term):
        terms = self.TOKENIZER(term).tokenize()
        for filter_class in self.FILTERS:
            terms = filter_class(terms).process()

        return terms
