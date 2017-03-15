import random


class InvertedIndex:
    def __init__(self):
        self.inverted_index = {}
        self.document_store = {}

    def index(self, terms, document):
        document_id = self._generate_document_id(document)

        self._store_document(document_id, document)
        self._add_terms_to_index(document_id, terms)

    def search(self, search_terms):
        document_ids = self._query(search_terms)
        documents = self._fetch(document_ids)

        return documents

    def _query(self, search_terms):
        resulting_documents = []

        for search_term, position in search_terms:
            resulting_documents += self.inverted_index[search_term].keys()

        return set(resulting_documents)

    def _fetch(self, document_ids):
        return [self.document_store[document_id] for document_id in document_ids]

    def _generate_document_id(self, document):
        # TODO: better id generation method
        return str(random.random())

    def _store_document(self, document_id, document):
        self.document_store[document_id] = document

    def _add_terms_to_index(self, document_id, terms):
        for term, position in terms:
            self._add_term_to_index(term, position, document_id)

    def _add_term_to_index(self, term, position, document_id):
        if term not in self.inverted_index:
            self.inverted_index[term] = {}

        if document_id not in self.inverted_index[term]:
            self.inverted_index[term][document_id] = []

        self.inverted_index[term][document_id].append(position)
