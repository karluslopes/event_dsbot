class DBase:
    def __init__(self):
        self.tables = {}

    def create(self, table, *labels):
        self.tables[table] = {label: [] for label in labels}

    def insert(self, table, *values):
        if len(values) == len(self.tables[table]):
            i=0
            for label in self.tables[table].keys():
                self.tables[table][label].append(values[i])
                i += 1
        else:
            raise Exception("Erro: Quantidade de dados inseridos incompatível com a tabela.")
               
    def query(self, table, value):
        found = []
        foundedRegisters = []
        matrix = list(self.tables[table].values())

        for row in range(len(matrix)):
            array = []
            found = False

            for collumn in range(len(matrix[row])):
                item = matrix[row][collumn]
                array.append(item)

                if item == value:
                    found = True

            if found:
                foundedRegisters.append(array)
        return matrix, foundedRegisters

database = DBase()
database.create("table", "label1", "label2", "label3")
database.insert("table", "value1", "value2", "value3")
database.insert("table", "value4", "value1", "value5")
database.insert("table", "value1", "value5", "value6")
print(database.query("table", "value1"))
