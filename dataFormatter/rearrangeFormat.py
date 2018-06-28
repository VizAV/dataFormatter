import json
from dataFormatter.utils import reArrangeRow

class ReArranger():
    def __init__(self):
        pass

    def setRearranger(self,filePath):
        self.reArranger=read(filePath)
    #Get the keys in the same format we wanted
    def transform(self, row):

        collectionDict = {}
        for collectionKeys, collectionValues in self.reArranger.items():



            # #Put the entire contents in a valirable name if it s not a dict
            # if type(collectionValues) is not dict:
            #     reArrangedRow = row[collectionValues]
            # else:

            # Check collection values if it is dict or list. Separate conditions
            if type(collectionValues) is dict:

                reArrangedRow=reArrangeRow(collectionValues,row)

                collectionDict[collectionKeys] = reArrangedRow
            elif type(collectionValues) is list:
                collectionList=[]
                structure=collectionValues[0]
                for keys,values in structure.items():
                    for element in row[keys]:
                        reArrangedRow = reArrangeRow(values,element)
                # for element in row[structure]:
                        collectionList.append(reArrangedRow)
                collectionDict[collectionKeys] = collectionList
            # collectionDict[collectionKeys] = reArrangedRow
                    # # If neither dict not list, assign directly
                    # if type(mainValue) is not dict and type(mainValue) is not list:
                    #     reArrangedRow[mainKey] = row[mainValue]
                    #
                    # #put the values in a recursive function
                    # elif type(mainValue) is dict:
                    #     reArrangedRow[mainKey] = {}
                    #     for subKey, subValues in mainValue.items():
                    #         reArrangedRow[mainKey][subKey] = row[subValues]
                    # elif type(mainValue) is list:
                    #     reArrangedRow[mainKey] = []
                    #     for cellValue in row[mainValue]:
                    #         fundingInfo = {}
                    #         for subKey, subValue in cellValue.items():
                    #             fundingInfo[subKey] = row[mainValue][subValue]
                    #         reArrangedRow[mainKey].append(fundingInfo)

        return collectionDict


def read(filepath):

    try:  # Read the input file and the validator file
        reArrangeFile = json.load(open(filepath))
        return reArrangeFile
    except FileNotFoundError as e:
        print(e.__str__())
        exit()
