from datetime import datetime

import ast


# WE need to think of a way in which we can call a single function and let it perform the task by calling the datatype of the field
# def assignValues(value):
#     value["type"] = eval(value["type"])
#     if value["type"] == list:
#         value["element"] = assignValues(value["element"])
#     if value["type"] == object:
#         for subKey, subValue in value['element'].items():
#             value["element"][subKey] = assignValues(subValue)
#     return value

def convertStringToString(cell,structure):
    return cell,None

def convertStringToFloat(cell,structure):
    try:
        cell = float(cell)
        return cell,None
    except:
        return None,'Cant convert string to float'


def convertStringToList(cell,structure):

    try:
        cell = ast.literal_eval(str(cell))

    except Exception as e:
        # print(e.__str__())
        errorcell = 'Cant convert to List'
        cell = None
        return cell,errorcell

    elemList = []
    elemErrorList = []
    for elem in cell:
        elem, errorElem = convertCells[structure['element']['type']](elem, structure['element'])
        elemList.append(elem)
        elemErrorList.append(errorElem)

    return elemList, elemErrorList

    # for val in range(len(cell)):
    #     for format in ['%d-%m-%Y','%d/%m/%y','%d-%b %y']:
    #         try:
    #             cellValue = datetime.strptime(cell[val],format)
    #             break
    #         except:
    #             cellValue = 'date format not compatible'
    #             continue
    #     cell[val] = cellValue
    # return cell

def convertStringToDatetime(cell,structure):
    for format in ['%d-%m-%Y', '%d/%m/%y', '%d %b %y','%d/%m/%Y',"%Y-%m-%d","%Y.0"]:
        try:
            value = datetime.strptime(str(cell), format)
            errorValue=None
            break
        except:
            value=None
            errorValue = 'Datetime format Not acceptable'
            continue

    cell=value
    errorCell = errorValue

    return cell,errorCell

def convertStringToObject(cell,structure):
    try:
        cell=ast.literal_eval(str(cell))
    except Exception as e:
        # print(e.__str__())
        errorcell = 'Cant convert to object'
        cell = None
        return cell,errorcell

    outputcell={}
    errorCell={}

    for key,value in structure['element'].items():
        try:
            subcell=cell[key]
            outputcell[key], errorCell[key] = convertCells[value['type']](subcell, value)
        except:
            outputcell[key]=None
            errorCell[key]='This key does not exist'
            pass

    return outputcell,errorCell

convertCells = {
    'string':convertStringToString,
    'float':convertStringToFloat,
    'list':convertStringToList,
    'datetime':convertStringToDatetime,
    'object':convertStringToObject
}
#
# def assignStrValue():
#     pass
# def assignFloatValue():
#     pass
# def assignDateValue():
#     pass
#
# reArrangeCells = {
#     'str':assignStrValue,
#     'float':assignFloatValue,
#     'datetime':assignDateValue,
#     'datetime':assignDateValue,
# }

def reArrangeRow(structure,row):
    modifiedRow = {}  # Initialize the dictionary


    for key, value in structure.items():
        if type(value) is not dict and type(value) is not list:
            modifiedRow[key] = row[value]
        elif type(value) is dict:
            modifiedRow[key]=reArrangeRow(value,row)
        elif type(value) is list:
            modifiedValueList=[]
            substructure=value[0]
            for element in row[key]:
                modifiedRowElement = reArrangeRow(substructure,element)
                modifiedValueList.append(modifiedRowElement)
            modifiedRow[key]=modifiedValueList
    return modifiedRow