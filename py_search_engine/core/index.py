class Index:
    def __init__(self, terms_store, mapping={}):
        self.terms_store = terms_store
        self.mapping = mapping

    def index(self, document):
        document_terms = self._extract_terms_from_document(document)

        self._store(document_terms, document)

    def search(self, attribute, search_string):
        attribute_analyzer = self.mapping[attribute]

        search_terms = attribute_analyzer.analyze(search_string)

        return self.terms_store.search(search_terms)

    def _extract_terms_from_document(self, document):
        terms = []

        for attribute_name, attribute_analyzer in self.mapping.items():
            document_attribute_value = document[attribute_name]

            terms += attribute_analyzer.analyze(document_attribute_value)

        return terms

    def _store(self, terms, document):
        self.terms_store.index(terms, document)
