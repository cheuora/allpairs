import itertools

def itemCount2by2(array):
    length = 0
    for i in array:
        length = length + len(i)
    return length


class Coverage:
    originCoverage = ''
    def __init__(self, coverageAll):
        Coverage.originCoverage = coverageAll
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
        combinations_case = list(itertools.combinations(itemCaseFromFull,2))
        for i in combinations_case:
            searchResult = self.searchCoverageItem(i)
            if (searchResult):
                retval = retval + searchResult
        
        return retval





# parameters = [ [ "Brand X", "Brand Y","Brand A" ]
#              , [ "win98", "NT", "2000", "XP"]
#              , [ "Internal", "Modem" ],
#              [56,45,22,34],
#              ]

parameters = [ ["a", "b"], [1,2],['x','y', 'z']]

fullcomb = list(itertools.product(*parameters))


pairCoverage = list(itertools.combinations(parameters,2))

pairCovArray = []

for i in pairCoverage:
    pairCovArray.append(list(itertools.product(*i)))


for kkk in pairCovArray:
    print(kkk)

print('/n/n/n')

for kkkk in fullcomb:
    print(kkkk)

print('\n\n\n')

### 전체 조합을 가지고 커버리지 체크하면서 커버리지는 삭제함. 커버리지에 들어가면 index를 저장. 아니면 skip ###

coverageObj = Coverage(pairCovArray)

selectedCaseIndex = []
remainedCoverage = 1

for selectedIndex, value in enumerate(fullcomb):
    bingo = coverageObj.checkCoverage(value)

    if (any(bingo)):
        selectedCaseIndex.append(selectedIndex)
        for items in bingo:
            if items:
                remainedCoverage =  coverageObj.updateCoverage(items)
    
    if remainedCoverage == 0:
        break

print(selectedCaseIndex)

print("\n\n\n")
print(coverageObj.originCoverage)
print("\n\n\n")

for k in selectedCaseIndex:
    print(fullcomb[k])









#print(len(cv.originCoverage))

# print(fullcomb[1])

temp = list(itertools.combinations(fullcomb[1],2))
# print(temp)

# print(temp[0] in pairCovArray[0])

# print("\n\n\n")
# print(pairCovArray[0])
