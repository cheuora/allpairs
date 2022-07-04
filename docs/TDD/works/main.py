import json

FIRST_CASE_RESULT = 2 #ID가 공란
SECOND_CASE_RESULT = 3 #ID는 있으며, PW는 불일치
THIRD_CASE_RESULT = 4 #ID는 미존재 ID이며 PW가 입력되지 않음
FOURTH_CASE_RESULT = 5 #ID는 미존재 PW는 값 있음
FIFTH_CASE_RESULT =6 #ID는 존재, PW는 공란 

with open("User.txt", "r") as f:
    json_data = json.load(f)

def Login(ID, PW):
    # For True Case
    if (len(ID.strip())>0 and len(PW.strip())>0):
        try:            
            if (json_data[ID]['pw'] == PW):
                return True
        except(KeyError):
            pass

    # For First Case
    if (len(ID.strip())==0) :
        return FIRST_CASE_RESULT

    # For Second Case
    if (len(ID.strip())>0 and len(PW.strip())>0):
        try:
            if (json_data[ID]['pw'] != PW):
                return SECOND_CASE_RESULT
        except(KeyError):
            pass

    # For Third Case
    if (len(ID.strip())>0 and len(PW.strip())==0):
        if not (ID in json_data):
            return THIRD_CASE_RESULT

    # For Fourth Case
    if (len(ID.strip())>0 and len(PW.strip())>0):
        if not (ID in json_data):
            return FOURTH_CASE_RESULT

    # For Fifth Case
    if (len(ID.strip())>0 and len(PW.strip()) == 0):
        if (ID in json_data):
            return FIFTH_CASE_RESULT


    return False

    