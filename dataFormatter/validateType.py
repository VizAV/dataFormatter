import json
from dataFormatter.utils import convertCells

class Validator():
    def __init__(self):
        pass
        # self.validator=validatorFile

    # def convertStringToDataTypes(self):
    #     for key in list(self.validator.keys()):
    #         try:
    #             self.validator[key] = assignValues(self.validator[key])
    #         except NameError as e:
    #             print(e.__str__(), ' in key: ', key, '. Proceeding with other keys')
    #             del self.validator[key]
    #     return

    def setValidator(self,filePath):
        self.validator=read(filePath)



    def transform(self,row):
        errorRow={}
        for key in list(row.keys()):
            if key not in list(self.validator.keys()):
                # Write out saying that this value is not present in the validator
                errorRow[key] = 'Not in validator'
                del row[key]

        # For each element mentioned in the validator column

        for key, value in self.validator.items():

            # Do we need this?
            if key not in list(row.keys()):
                errorRow[key] = 'Not in input File'
            else:

                # Transform each type into another
                row[key], errorRow[key] = convertCells[value['type']](row[key],value)

                # # Get each element of the list and do the previous step
                # if value['type'] == 'list':
                #     errorRow[key] = []
                #     try:
                #         for cellElem in range(len(row[key])):
                #             row[key][cellElem], error = convertCells[value['element']['type']](row[key][cellElem])
                #             errorRow[key].append(error)
                #     except Exception as e:
                #         row[key] = None
                #         errorRow[key] = 'List Length Zero'



        return row, errorRow


def read(filePath):

    try:  # Read the input file and the validator file
        validatorFile = json.load(open(filePath))

        return validatorFile
    except FileNotFoundError as e:
        print(e.__str__())
        exit()