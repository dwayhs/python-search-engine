#!/usr/bin/env python
#coding: UTF-8

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


test_documents = [
    {
        "text" : "A South Korean court removed the president on Friday, a first in the nation’s history, rattling the delicate balance of relationships across Asia at a particularly tense time. Her removal capped months of turmoil, as hundreds of thousands of South Koreans took to the streets, week after week, to protest a sprawling corruption scandal that shook the top echelons of business and government. Park Geun-hye, the nation’s first female president and the daughter of the Cold War military dictator Park Chung-hee, had been an icon of the conservative establishment that joined Washington in pressing for a hard line against North Korea’s nuclear provocations."
    },
    {
        "abc": 1,
        "text" : "President Trump, after a halting start, is now marshaling the full power of his office to win over holdout conservatives and waffling senators to support the House Republicans’ replacement for the Affordable Care Act. There are East Room meetings, evening dinners and sumptuous lunches — even a White House bowling soiree. Mr. Trump is deploying the salesman tactics he sharpened over several decades in New York real estate. His pitch: He is fully behind the bill to scotch President Barack Obama’s signature domestic achievement, but he is open to negotiations on the details. In so doing, Mr. Trump is plunging personally into his first major legislative fight, getting behind a bill that has been denounced by many health care providers and scorned by his base on the right. If it fails, Mr. Trump will find it difficult not to shoulder some of the blame. And it has momentum. On Thursday, two key House committees approved the legislation, which would undo the Affordable Care Act and replace it with a more modest system of tax credits and a rollback of Mr. Obama’s Medicaid expansion. Party-line votes by the House Energy and Commerce and Ways and Means Committees sent the measure to the House Budget Committee for consideration next week before a final House vote that Speaker Paul D. Ryan plans for later this month."
    },
    {
        "text" : "Now, with Mr. Trump’s administration aggressively pitching the House Republican plan to repeal and replace the Affordable Care Act, Capitol Hill’s official scorekeeper — the Congressional Budget Office — is coming under intense fire. As it prepares to render its judgment on the cost and impact of the bill, the nonpartisan agency of economists and statisticians has become a political piñata — and the latest example of Mr. Trump’s team casting doubt on benchmarks accepted as trustworthy for decades. The reason for their umbrage is clear: The C.B.O.’s official judgment on the American Health Care Act, as the Republican legislation is known, is expected to be released on Monday and it is more than an intellectual exercise. It could make or break the bill. Mr. Flynn, a retired Army lieutenant general, was hired by a prominent Turkish-American with ties to the government of President Recep Tayyip Erdogan, who has engaged in a widespread political crackdown after surviving a military coup attempt. Mr. Flynn was assigned to investigate Fethullah Gulen, a Turkish cleric who lives in Pennsylvania and was blamed by Mr. Erdogan for helping instigate the July putsch. Mr. Flynn signed a contract for the work just three weeks after delivering a fiery speech at the Republican National Convention endorsing Mr. Trump and leading “lock her up” chants advocating the imprisonment of Hillary Clinton for her use of a private email server while secretary of state. Without disclosing his financial interest, Mr. Flynn published an op-ed article on Election Day arguing that Turkey was misunderstood and assailing Mr. Gulen as 'a shady Islamic mullah' and 'radical Islamist.'"
    }
]


search_index = SearchIndex(
    index_pipeline=SimpleIndexPipeline(indexed_columns=['text']),
    terms_store=InvertedIndex()
)

for document in test_documents:
    search_index.index(document)

## Test queries
search_result = search_index.search("President Trump")

for result in search_result:
    print(result['text'] + "\n\n")
