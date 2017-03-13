#!/usr/bin/env python
#coding: UTF-8

import re

# --- INDEXING ---

# 1. store documents (base documents for tests)
document_01 = {
    "document_id" : "doc01",
    "text" : "A South Korean court removed the president on Friday, a first in the nation’s history, rattling the delicate balance of relationships across Asia at a particularly tense time. Her removal capped months of turmoil, as hundreds of thousands of South Koreans took to the streets, week after week, to protest a sprawling corruption scandal that shook the top echelons of business and government. Park Geun-hye, the nation’s first female president and the daughter of the Cold War military dictator Park Chung-hee, had been an icon of the conservative establishment that joined Washington in pressing for a hard line against North Korea’s nuclear provocations."
}
document_02 = {
    "document_id" : "doc02",
    "text" : "President Trump, after a halting start, is now marshaling the full power of his office to win over holdout conservatives and waffling senators to support the House Republicans’ replacement for the Affordable Care Act. There are East Room meetings, evening dinners and sumptuous lunches — even a White House bowling soiree. Mr. Trump is deploying the salesman tactics he sharpened over several decades in New York real estate. His pitch: He is fully behind the bill to scotch President Barack Obama’s signature domestic achievement, but he is open to negotiations on the details. In so doing, Mr. Trump is plunging personally into his first major legislative fight, getting behind a bill that has been denounced by many health care providers and scorned by his base on the right. If it fails, Mr. Trump will find it difficult not to shoulder some of the blame. And it has momentum. On Thursday, two key House committees approved the legislation, which would undo the Affordable Care Act and replace it with a more modest system of tax credits and a rollback of Mr. Obama’s Medicaid expansion. Party-line votes by the House Energy and Commerce and Ways and Means Committees sent the measure to the House Budget Committee for consideration next week before a final House vote that Speaker Paul D. Ryan plans for later this month."
}
document_03 = {
    "document_id" : "doc03",
    "text" : "Now, with Mr. Trump’s administration aggressively pitching the House Republican plan to repeal and replace the Affordable Care Act, Capitol Hill’s official scorekeeper — the Congressional Budget Office — is coming under intense fire. As it prepares to render its judgment on the cost and impact of the bill, the nonpartisan agency of economists and statisticians has become a political piñata — and the latest example of Mr. Trump’s team casting doubt on benchmarks accepted as trustworthy for decades. The reason for their umbrage is clear: The C.B.O.’s official judgment on the American Health Care Act, as the Republican legislation is known, is expected to be released on Monday and it is more than an intellectual exercise. It could make or break the bill. Mr. Flynn, a retired Army lieutenant general, was hired by a prominent Turkish-American with ties to the government of President Recep Tayyip Erdogan, who has engaged in a widespread political crackdown after surviving a military coup attempt. Mr. Flynn was assigned to investigate Fethullah Gulen, a Turkish cleric who lives in Pennsylvania and was blamed by Mr. Erdogan for helping instigate the July putsch. Mr. Flynn signed a contract for the work just three weeks after delivering a fiery speech at the Republican National Convention endorsing Mr. Trump and leading “lock her up” chants advocating the imprisonment of Hillary Clinton for her use of a private email server while secretary of state. Without disclosing his financial interest, Mr. Flynn published an op-ed article on Election Day arguing that Turkey was misunderstood and assailing Mr. Gulen as 'a shady Islamic mullah' and 'radical Islamist.'"
}
# All documents
documents = [document_01, document_02, document_03]

# Stop Words
stop_words = [
    "a", "about", "above", "after", "again", "against", "all", "am", "an", "and", "any",
    "are", "aren't", "as", "at", "be", "because", "been", "before", "being", "below",
    "between", "both", "but", "by", "can't", "cannot", "could", "couldn't", "did",
    "didn't", "do", "does", "doesn't", "doing", "don't", "down", "during", "each", "few",
    "for", "from", "further", "had", "hadn't", "has", "hasn't", "have", "haven't", "having",
    "he", "he'd", "he'll", "he's", "her", "here", "here's", "hers", "herself", "him",
    "himself", "his", "how", "how's", "i", "i'd", "i'll", "i'm", "i've", "if", "in",
    "into", "is", "isn't", "it", "it's", "its", "itself", "let's", "me", "more", "most",
    "mustn't", "my", "myself", "no", "nor", "not", "of", "off", "on", "once", "only",
    "or", "other", "ought", "our", "ours", "ourselves", "out", "over", "own", "same",
    "shan't", "she", "she'd", "she'll", "she's", "should", "shouldn't", "so", "some",
    "such", "than", "that", "that's", "the", "their", "theirs", "them", "themselves",
    "then", "there", "there's", "these", "they", "they'd", "they'll", "they're", "they've",
    "this", "those", "through", "to", "too", "under", "until", "up", "very", "was", "wasn't",
    "we", "we'd", "we'll", "we're", "we've", "were", "weren't", "what", "what's", "when",
    "when's", "where", "where's", "which", "while", "who", "who's", "whom", "why", "why's",
    "with", "won't", "would", "wouldn't", "you", "you'd", "you'll", "you're", "you've",
    "your", "yours", "yourself", "yourselves"
]

# dumb terms
dumb_terms = [
    '—', '%', '$', ' '
]

# Aux Functions
def print_elements(given_list):
    for element in given_list:
        print element

def flatten(given_list):
    return [item for sublist in given_list for item in sublist]

# MAIN OPERATIONS

# 2. Tokenization
tokens = []

for document in documents:
        # split on space
        terms = document["text"].split(" ")
        #lowercase the terms
        terms = [term.lower() for term in terms]
        #removing punctuation and clean spaces
        terms = [re.sub('[!;.,?\s“”’\']', '', term) for term in terms]

        #check if is a stop Word or is a dumb term
        terms = filter(lambda term: term not in stop_words and term not in dumb_terms, terms)
        print_elements(terms)
        #remove empty strings
        # terms = filter(Null, terms)
        terms = [{'document_id': document['document_id'], 'term': term} for term in terms]

        tokens.append(terms)

#final list of tokens
tokens = flatten(tokens)

# 3. Edge N-grams to generate terms


# TEST AREA
#print_elements(tokens)
