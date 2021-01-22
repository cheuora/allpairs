import itertools

def itemCount2by2(array):
    length = 0
    for i in array:
        length = length + len(i)
    return length

def getCoverage(parameters, way):
    pairCoverage = list(itertools.combinations(parameters,way))
    pairCovArray = []
    for i in pairCoverage:
        pairCovArray.append(list(itertools.product(*i)))
    
    return pairCovArray

def executor(fullcomb, coverageObj):
    remainedCoverage = 1
    selectedCaseIndex = []
    ret_cases = []
    threshold = len(coverageObj.originCoverage)

    for i in range(threshold,0, -1):
        selectedCaseIndex = []
        for selectedIndex, value in enumerate(fullcomb):
            bingo = coverageObj.checkCoverage(value)
            if (len(bingo) == i):
                selectedCaseIndex.append(selectedIndex)
                for items in bingo:
                    if items:
                        remainedCoverage =  coverageObj.updateCoverage(items)


        for case_index in selectedCaseIndex:
            ret_cases.append(fullcomb[case_index])
        
        if (remainedCoverage == 0):
            break

        for ele in sorted(selectedCaseIndex, reverse = True): 
            # fullcomb업데이트 :  
            del fullcomb[ele] 

    return ret_cases


class Coverage:
    originCoverage = ''
    def __init__(self, coverageAll, num_of_way):
        Coverage.originCoverage = coverageAll
        self.num_of_way = num_of_way
        pass

    def updateCoverage(self,coordinate):
        # 인덱스(x,y)에 맞는 커버리지 list배열(2x2)배열을 삭제 및 업데이트
        # 남아 있는 item수를 항상 return
        Coverage.originCoverage[coordinate[0]].pop(coordinate[1])
        return itemCount2by2(Coverage.originCoverage)

    def searchCoverageItem(self, itemVal):
        # 커버리지 list배열(2x2)에서 item을 찾아 인덱스를(x,y) return
        # 못찾으면 null return

        x = 0
        y = 0
        retval = []

        for i,values in enumerate(Coverage.originCoverage):
            if ( itemVal in values):
                y = values.index(itemVal)
                x = i
                retval.append((x,y))

        return retval
    
    def checkCoverage(self,itemCaseFromFull):
        retval = []
        combinations_case = list(itertools.combinations(itemCaseFromFull,self.num_of_way))
        for i in combinations_case:
            searchResult = self.searchCoverageItem(i)
            if (searchResult):
                retval = retval + searchResult
        
        return retval


def pypair(parameters,way):
    # main function
    fullcomb = list(itertools.product(*parameters))
    coverageObj = Coverage(getCoverage(parameters,way), way)
    Test_cases = executor(fullcomb, coverageObj)

    return Test_cases
