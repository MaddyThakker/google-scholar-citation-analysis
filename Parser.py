from scholarly import scholarly, ProxyGenerator
import json
import pandas as pd

class Parser:

    def __init__(self, author_id: str, name: str) -> None:
        self.author_id = author_id
        self.name = name

    def get_all_papers(self):
        search_query = scholarly.search_author_id(self.author_id)
        author = scholarly.fill(search_query)
        for publication in author["publications"]:
            print(publication["bib"]["title"])

# p = Parser(author_id="-DAxp-cAAAAJ", name="Mayank Vatsa")
p = Parser(author_id="eZ4WZmIAAAAJ", name="Anish Madan")

p.get_all_papers()