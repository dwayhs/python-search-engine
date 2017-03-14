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


class SearchIndex:
    def __init__(self, index_pipeline, terms_store):
        self.index_pipeline = index_pipeline
        self.terms_store = terms_store

    def index(self, document):
        processed_terms = self.index_pipeline.execute_pipeline(document)
        self._store(processed_terms, document)

    def search(self, search_string):
        # TODO: use pipeline to get query terms
        search_terms = search_string.split(' ')

        return self.terms_store.search(search_terms)

    def _store(self, terms, document):
        self.terms_store.index(terms, document)


class SimpleIndexPipeline:
    PIPELINE = [
        SimpleNormalizeFilter,
        SimpleTokenizer
    ]

    def __init__(self, indexed_columns=[]):
        self.indexed_columns = indexed_columns

    def execute_pipeline(self, document):
        terms = self._extract_index_content(document)

        for pipeline_step in self.PIPELINE:
            terms = pipeline_step(terms).process()

        return terms

    def _extract_index_content(self, document):
        return [document[column] for column in self.indexed_columns]



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
