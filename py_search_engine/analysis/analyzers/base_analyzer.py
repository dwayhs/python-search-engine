class BaseAnalyzer:
    PIPELINE = []

    def analyze(self, term):
        terms = [term]
        for pipeline_step in self.PIPELINE:
            terms = pipeline_step(terms).process()

        return terms
