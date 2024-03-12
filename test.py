tables = {
    "table_1": [
        {"label_1": "value_1", "label_2": "value_2"},
        {"label_1": "value_3", "label_3": "value_3"},
    ],

    "table_2": [
        {"label_1": "value_1", "label_2": "value_2"},
        {"label_1": "value_3", "label_3": "value_3"},
    ],
}

tabless = {
    "table_1": {
        "label_1": ["value_1", "value_3", "value_1"],
        "label_2": ["value_2", "value_4", "value_6"],
        "label_3": ["value_1", None, None]
    },

     "table_2": {      #1          #2         #3
        "label_1": ["value_1", "value_2", "value_1"],
        "label_2": ["value_4", "value_5", "value_6"],
    },
}


tables = {
    "table_1": [
        ["label_1", "label_2", "label_3"],
        ["value_1", "value_2", "value_3"],
        ["value_4", "value_5", "value_6"],
    ],

    "table_2": [
        ["label_1", "label_2", "label_3"],
        ["value_1", "value_2", "value_3"],
        ["value_4", "value_5", "value_6"],
    ],
}

class DBase:
    def __init__(self):
        self.tables = {}

    def create(self, table, *labels):
        self.tables[table] = [list(labels)]

    def insert(self, table, *values):
        if len(values) <= len(self.tables[table][0]):
            self.tables[table].append(list(values))
        else:
            raise Exception("Erro: tentativa de inserção de registro incompatível com a tabela!")

    def query(self, table, label, value):
        pass

    def fetch(self, table):
        if table in self.tables:
            return self.tables[table]
        raise Exception("Erro: a tabela não existe!")

database = DBase()
database.create("table", "label1", "label2")
database.insert("table", "value1", "value2")
database.insert("table", "value3", "value4")
print(database.fetch("table"))