import unittest
from HW3 import *

class HW3SampleTests(unittest.TestCase):
    def setUp(self):
        # sprintLog inputs
        self.log1 = {'John': {'task1': 5}, 'Rae': {'task1': 10, 'task2': 4}, 'Kelly': {'task1': 8, 'task3': 5}, 'Alex': {'task1': 11, 'task2': 2, 'task3': 1}, 'Aaron': {'task2': 15}, 'Ethan':{'task3': 12}, 'Helen': {'task3': 10}}
        self.log2 = {'Mark': {'task1': 5, 'task2': 2}, 'Kelly': {'task1': 10}, 'Alex': {'task1': 15, 'task2': 2}, 'Rae': {'task2': 10}, 'Aaron': {'task2': 10}, 'Helen': {'task4': 16}}
        self.log3 = {'Aaron': {'task5': 15, 'task6': 8}, 'Rae': {'task5': 20}, 'Helen': {'task6': 16}}
        self.log4 = {'Alex': {'task6': 15}, 'Kelly': {'task5': 20}, 'Helen': {'task6': 10}}
        # addSprints inputs/outputs
        self.sprint1 = {'task1': {'John': 5, 'Rae': 10, 'Kelly': 8, 'Alex': 11}, 'task2': {'Rae': 4, 'Alex': 2, 'Aaron': 15}, 'task3': {'Kelly': 5, 'Alex': 1, 'Ethan': 12, 'Helen': 10}}
        self.sprint2 = {'task1': {'Mark': 5, 'Kelly': 10, 'Alex': 15}, 'task2': {'Mark': 2, 'Alex': 2, 'Rae': 10, 'Aaron': 10}, 'task4': {'Helen': 16}}
        self.sprint3 = {'task5': {'Aaron': 15, 'Rae': 20}, 'task6': {'Aaron': 8, 'Helen': 16}}
        self.sprint4 = {'task6': {'Alex': 15, 'Helen': 10}, 'task5': {'Kelly': 20}}
        self.addedSprints1 = {'task1': {'John': 5, 'Rae': 10, 'Kelly': 18, 'Alex': 26, 'Mark': 5}, 'task2': {'Rae': 14, 'Alex': 4, 'Aaron': 25, 'Mark': 2}, 'task3': {'Kelly': 5, 'Alex': 1, 'Ethan': 12, 'Helen': 10}, 'task4': {'Helen': 16}}
        self.addedSprints2 = {'task1': {'John': 5, 'Rae': 10, 'Kelly': 8, 'Alex': 11}, 'task2': {'Rae': 4, 'Alex': 2, 'Aaron': 15}, 'task3': {'Kelly': 5, 'Alex': 1, 'Ethan': 12, 'Helen': 10}, 'task5': {'Aaron': 15, 'Rae': 20}, 'task6': {'Aaron': 8, 'Helen': 16}}
        self.addedSprints3 = {'task1': {'Mark': 5, 'Kelly': 10, 'Alex': 15}, 'task2': {'Mark': 2, 'Alex': 2, 'Rae': 10, 'Aaron': 10}, 'task4': {'Helen': 16}, 'task5': {'Aaron': 15, 'Rae': 20}, 'task6': {'Aaron': 8, 'Helen': 16}}
        # addNLogs input/output
        self.logList1 = [self.log1,self.log2]
        self.logList2 = [self.log1,self.log3]
        self.logList3 = [self.log2,self.log3]
        self.sprintSummary1 = {'task1': {'Mark': 10, 'Kelly': 28, 'Alex': 41, 'John': 5, 'Rae': 10}, 'task2': {'Mark': 4, 'Alex': 6, 'Rae': 24, 'Aaron': 35}, 'task3': {'Kelly': 5, 'Alex': 1, 'Ethan': 12, 'Helen': 10}, 'task4': {'Helen': 16}}
        self.sprintSummary2 = {'task1': {'John': 5, 'Rae': 10, 'Kelly': 8, 'Alex': 11}, 'task2': {'Rae': 4, 'Alex': 2, 'Aaron': 15}, 'task3': {'Kelly': 5, 'Alex': 1, 'Ethan': 12, 'Helen': 10}, 'task5': {'Aaron': 15, 'Rae': 20}, 'task6': {'Aaron': 8, 'Helen': 16}}
        self.sprintSummary3 = {'task1': {'Mark': 5, 'Kelly': 10, 'Alex': 15}, 'task2': {'Mark': 2, 'Alex': 2, 'Rae': 10, 'Aaron': 10}, 'task4': {'Helen': 16}, 'task5': {'Aaron': 15, 'Rae': 20}, 'task6': {'Aaron': 8, 'Helen': 16}}
        #lookupVal inputs
        self.lookupList = [{"x":1,"y":True,"z":"found"},{"x":2},{"y":False}]
        self.lookup2List = [(0,{"x":0,"y":True,"z":"zero"}), (0,{"x":1}), (1,{"y":False}), (1,{"x":3, "z":"three"}), (2,{})]
        # iterFile output
        self.filetokens = ["CptS","355","Assignment","3","-","Python","Warmup","This","is","a","text","test","file","for","CptS","355","-","Assignment","3","-","Python","Warmup","With","some","repeated","text","for","CptS","355","-","Assignment","3","-","Python","Warmup","."]
        self.histogram = [('-', 5), ('3', 3), ('355', 3), ('Assignment', 3), ('CptS', 3), ('Python', 3), ('Warmup', 3), ('for', 2), ('text', 2), ('.', 1), ('This', 1), ('With', 1), ('a', 1), ('file', 1), ('is', 1), ('repeated', 1), ('some', 1), ('test', 1)]
        
    def test_sprintLog(self):
        self.assertDictEqual(sprintLog(self.log1),self.sprint1)
        self.assertDictEqual(sprintLog(self.log2),self.sprint2)
        self.assertDictEqual(sprintLog(self.log3),self.sprint3)
        self.assertDictEqual(sprintLog(self.log4),self.sprint4)

    def test_addSprints(self):
        self.assertDictEqual(addSprints(self.sprint1,self.sprint2),self.addedSprints1)
        self.assertDictEqual(addSprints(self.sprint1,self.sprint3),self.addedSprints2)
        self.assertDictEqual(addSprints(self.sprint2,self.sprint3),self.addedSprints3)

    def test_addNLogs(self):
        self.assertDictEqual(addNLogs(self.logList1),self.sprintSummary1)
        self.assertDictEqual(addNLogs(self.logList2),self.sprintSummary2)
        self.assertDictEqual(addNLogs(self.logList3),self.sprintSummary3)

    def test_lookupVal(self):
        self.assertEqual(lookupVal(self.lookupList,"x"),2)
        self.assertEqual(lookupVal(self.lookupList,"y"),False)
        self.assertEqual(lookupVal(self.lookupList,"z"),"found")
        self.assertEqual(lookupVal(self.lookupList,"t"),None)

    def test_lookupVal2(self):
        pass

    def test_unzip(self):
        pass
    
    def test_numPaths(self):
        pass 

    def test_iterFile(self):
        mywords = iterFile("testfile.txt")
        self.assertEqual(mywords.__next__(),"CptS")  
        self.assertEqual(mywords.__next__(),"355")
        self.assertEqual(mywords.__next__(),"Assignment")
        restofFile = []
        for word in mywords:  
            restofFile.append(word)
        self.assertEqual(restofFile,self.filetokens[3:])

    def test_wordHistogram(self):
        pass

if __name__ == '__main__':
    unittest.main()