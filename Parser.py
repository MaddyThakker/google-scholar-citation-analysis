from logging import debug
from os import name
from typing import Dict
from scholarly import scholarly, ProxyGenerator
import json
import pandas as pd

class Parser:

    def __init__(self, author_id: str, name: str, debug=False) -> None:
        self.author_id = author_id
        self.name = name
        self.debug = debug
    
    def get_all_citations(self) -> Dict:
        author_cite_times = {}

        search_query = scholarly.search_author_id(self.author_id)
        author = scholarly.fill(search_query)
        for publication in author["publications"]:
            if self.debug:
                print("Publication - ", publication["bib"]["title"])

            detailed_publication = scholarly.fill(publication)
            cited_this = scholarly.citedby(detailed_publication)

            for each_citation in cited_this:
                if self.debug:
                    print("Citation for current paper - ", each_citation['bib'])
                all_authors_this_citations =  each_citation['bib']["author"].split(" and ")
                for each_author in all_authors_this_citations:
                    author_cite_times[each_author] += 1

        return author_cite_times

if __name__ == "__main__":
    psr = Parser(author_id="eZ4WZmIAAAAJ", name="Anish Madan", debug=True)
    print(psr.get_all_citations())