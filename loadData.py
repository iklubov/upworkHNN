import math
from openpyxl import load_workbook

def loadData():
    wb = load_workbook('input.xlsx')
    ws = wb['input']
    result = []
    for row in ws.rows:
        if all([type(cell.value)==str for cell in row]):
            continue
        result.append(Node([cell.value for cell in row]))
    print('DATA LOADED \n', result)
    return result

class Node:
    @staticmethod
    def distance(node1, node2):
        return math.fabs(node1.x - node2.x) + math.fabs(node1.y - node2.y)

    def __init__(self, data):
        self.type = data[0]
        self.x = data[1]
        self.y = data[2]

    def __repr__(self):
        return 'Node x=%s y=%s type=%s' % (str(self.x), str(self.y), str(self.type))
