import networkx as nx
from pyvis.network import Network
import pandas as pd
import sqlite3
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
        
        conn = sqlite3.connect('farsnet3.0.db3')  # Replace with your actual database
        cursor = conn.cursor()
        
        query = f"""
            SELECT id, pos, semanticCategory, example, gloss, nofather, noMapping FROM synset
            WHERE synset.id IN (
                SELECT synset.id as synset_id
                FROM word
                INNER JOIN sense ON sense.word = word.id
                INNER JOIN synset ON sense.synset = synset.id
                LEFT OUTER JOIN value ON value.word = word.id
                WHERE word.search_value {style} '{searchKeyword}'
                OR value.search_value {style} '{searchKeyword}'
            )
            OR synset.id IN (
                SELECT sense.synset AS synset_id
                FROM sense
                INNER JOIN sense_relation ON sense.id = sense_relation.sense
                INNER JOIN sense AS sense_2 ON sense_2.id = sense_relation.sense2
                INNER JOIN word ON sense_2.word = word.id
                WHERE sense_relation.type = 'Refer-to'
                AND word.search_value {style} '{searchKeyword}'
            )
            OR synset.id IN (
                SELECT sense_2.synset AS synset_id
                FROM sense
                INNER JOIN sense_relation ON sense.id = sense_relation.sense
                INNER JOIN sense AS sense_2 ON sense_2.id = sense_relation.sense2
                INNER JOIN word ON sense.word = word.id
                WHERE sense_relation.type = 'Refer-to'
                AND word.search_value {style} '{searchKeyword}'
            )
        """
        
        cursor.execute(query)
        results = cursor.fetchall()
        conn.close()
        return results

    @staticmethod
    def get_synset_relation_by_id(synset_id):
        conn = sqlite3.connect('farsnet3.0.db3')  # Replace with your actual database
        query = f"""
            SELECT id, type, synsetWords1, synsetWords2, synset, synset2, reverse_type 
            FROM synset_relation 
            WHERE synset={synset_id} OR
            synset2={synset_id}
        """
        df = pd.read_sql_query(query, conn)
        conn.close()
        return df

    @staticmethod
    def get_all_synsets():
        conn = sqlite3.connect('farsnet3.0.db3')  # Replace with your actual database
        query = "SELECT id, pos, semanticCategory, example, gloss, nofather, noMapping FROM synset"
        df = pd.read_sql_query(query, conn)
        conn.close()
        return df
            
# # Instantiate the class
# fars_graph = FarsGraph()

# # Visualize the graph
# fars_graph.visualize()

# # Find predecessors of a node
# print(fars_graph.find_pred('سگ'))

# # Find relations between two nodes
# print(fars_graph.find_relations('سگ', 'گربه'))

# # Get synsets by word
# print(fars_graph.get_synsets_by_word('سگ', 'LIKE'))

# # Get synset relations by id
# print(fars_graph.get_synset_relation_by_id(1))

# # Get all synsets
# print(fars_graph.get_all_synsets())

# # Denormalize a token
# print(fars_graph.denormalize('سگ'))


#######################################################
# predecessors = list(fars_graph.find_pred('some_node'))
# print(predecessors)

# # Find relations between two nodes
# relations = fars_graph.find_relations('node1', 'node2')
# print(relations)

# # Get synsets by word
# synsets = FarsGraph.get_synsets_by_word('word', 'LIKE')
# print(synsets)

# # Get synset relation by ID
# synset_relations = FarsGraph.get_synset_relation_by_id(12345)
# print(synset_relations)

# # Get all synsets
# all_synsets = FarsGraph.get_all_synsets()
# print(all_synsets)
