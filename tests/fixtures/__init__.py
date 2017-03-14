import json


def load_document_fixture(document_name):
    with open('tests/fixtures/{}.json'.format(document_name)) as f:
        document_contents = f.read()

    return json.loads(document_contents)
