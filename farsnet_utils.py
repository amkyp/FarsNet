import networkx as nx
from pyvis.network import Network
import pandas as pd
import sqlite_connection
from farsnet import *


class FarsGraph:
    def __init__(self):
        df = pd.read_csv('farsnet/synset_relation.csv', delimiter=',')
        self.G = nx.from_pandas_edgelist(df, source='synsetWords1', target='synsetWords2', edge_attr='type',
                                         create_using=nx.MultiDiGraph())

    def visualize(self):
        net = Network(notebook=True, width=1124, height=700)
        net.from_nx(self.G)
        net.show_buttons(filter_=['physics'])
        net.show('farsnet.html')

    def find_pred(self, node):
        return self.G.predecessors(',' + node)

    def find_relations(self, src, des):
        return self.G.get_edge_data(src, des)

    @staticmethod
    def denormalize(token):
        """ Unfortunately, some of FarsNet entries are not normalized so the input should be denormalized to have
        a better chance of string matching! """
        return token.replace("ی", "ي")

    @classmethod
    def get_synsets_by_word(cls, searchKeyword, style):
        searchKeyword = cls.denormalize(searchKeyword)
        if style == "LIKE":
            searchKeyword = "%" + searchKeyword + "%"
        elif style == 'START':
            searchKeyword = "" + searchKeyword + "%"
            style = "LIKE"
        elif style == 'END':
            searchKeyword = "%" + searchKeyword + ""
            style = "LIKE"
        else:
            style = '='
        String_sql = f"SELECT id, pos, semanticCategory, example, gloss, nofather, noMapping FROM synset \
                     WHERE synset.id IN (SELECT \
                    synset.id as synset_id\
                    FROM\
                    word INNER JOIN sense ON sense.word = word.id \
                    INNER JOIN synset ON sense.synset = synset.id \
                    LEFT OUTER JOIN value ON value.word = word.id \
                    WHERE word.search_value {style} '{searchKeyword}' OR (value.search_value) {style} '{searchKeyword}')\
                    OR synset.id IN (SELECT sense.synset AS synset_id FROM sense INNER JOIN sense_relation ON sense.id = \
                    sense_relation.sense INNER JOIN sense AS sense_2 ON sense_2.id = sense_relation.sense2 INNER JOIN word\
                     ON sense_2.word = word.id WHERE sense_relation.type =  'Refer-to' AND word.search_value {style} '{searchKeyword}')\
                    OR synset.id IN (SELECT sense_2.synset AS synset_id FROM sense INNER JOIN sense_relation ON sense.id = \
                    sense_relation.sense INNER JOIN sense AS sense_2 ON sense_2.id = sense_relation.sense2 INNER JOIN word ON\
                     sense.word = word.id WHERE sense_relation.type =  'Refer-to' AND word.search_value {style} '{searchKeyword}')"
        return sqlite_connection.select(String_sql)

    @staticmethod
    def get_synset_relation_by_id(synset_id):
        df = pd.read_sql_query(
            f"SELECT id, type, synsetWords1, synsetWords2, synset, synset2, reverse_type FROM synset_relation WHERE synset={synset_id} OR synset2={synset_id}",
            sqlite_connection.con)
        return df

    @staticmethod
    def get_all_synsets():
        df = pd.read_sql_query("SELECT id, pos, semanticCategory, example, gloss, nofather, noMapping FROM synset",
                               sqlite_connection.con)
        return df
