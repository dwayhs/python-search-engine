#!/usr/bin/env python
import random


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


class SimpleNormalizeFilter(BaseFilter):
    def _process_term(self, term):
        # TODO: replaces special chars...
        # TODO: lowercases...
        return [term]


class SimpleTokenizer(BaseFilter):
    def _process_term(self, term):
        return term.split(' ')


class SimpleAnalyzer:
    PIPELINE = [
        SimpleNormalizeFilter,
        SimpleTokenizer
    ]

    def analyze(self, term):
        terms = [term]
        for pipeline_step in self.PIPELINE:
            terms = pipeline_step(terms).process()

        return terms


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

        for search_term in search_terms:
            resulting_documents += self.inverted_index[search_term]

        return set(resulting_documents)

    def _fetch(self, document_ids):
        return [self.document_store[document_id] for document_id in document_ids]

    def _generate_document_id(self, document):
        # TODO: better id generation method
        return str(random.random())

    def _store_document(self, document_id, document):
        self.document_store[document_id] = document

    def _add_terms_to_index(self, document_id, terms):
        for term in terms:
            self._add_term_to_index(term, document_id)

    def _add_term_to_index(self, term, document_id):
        if term in self.inverted_index:
            self.inverted_index[term].append(document_id)
        else:
            self.inverted_index[term] = [document_id]
