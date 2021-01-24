import itertools
import copy
from pypair import pypair

parameters = [ [ "Brand X", "Brand Y","Brand A" ]
             , [ "NT", "2000", "XP"]
             , [ "Internal", "Modem" ]
             , ['This', 'That']
             ]


cond1 = {"Brand X" : ["XP"], "Brand Y" : ["NT","Modem"]}
cond3 = {"Brand Y" : ["NT","Modem"]}
cond0 = {}



def execude_condition(parameters, cond):
    retVal = copy.deepcopy(parameters)
    for i in cond:
        for j in retVal:
            bingo = j.count(i)
            if bingo > 0 :
               j.pop(j.index(i))

    
    return retVal


def include_condition(parameters, cond):
    retVal = copy.deepcopy(parameters)
    temp_index_value = {}
    for key, value in cond.items():
        exchange_item = key

        for param_item in retVal:
            should_del_item = value

            for del_item in should_del_item:
                bingo = param_item.count(del_item)
                if bingo > 0:
                    param_item.pop(param_item.index(del_item))
        

            if param_item.count(exchange_item) > 0:
                del_index = retVal.index(param_item)
                try:
                    temp_index_value[del_index].append(exchange_item)
                except KeyError:
                    temp_index_value[del_index] =[]
                    temp_index_value[del_index].append(exchange_item)
          
    for key, value in temp_index_value.items():
        retVal[key] = value
    
    return retVal
        
    # exchange_item = list(cond.keys())[0]
    # for param_item in retVal:
    #     should_del_item = list(cond.values())[0]
        
    #     for del_item in should_del_item:
    #         bingo = param_item.count(del_item)
    #         if bingo > 0:
    #             param_item.pop(param_item.index(del_item))

    #     if param_item.count(exchange_item) > 0 :
    #         del_index = retVal.index(param_item)
    #         retVal[del_index] = []
    #         retVal[del_index].append(exchange_item)
    
    # return retVal



# include_condition(parameters,cond3)
# print(parameters)

def make_one_accepted_condition(parameters, conditions, num_of_way):
    main_results = execude_condition(parameters,conditions)
    additional_results = include_condition(parameters,conditions)

    main_combination = pypair(main_results,2)
    additional_combination = pypair(additional_results,1)

    return(main_combination + additional_combination)   

temp = make_one_accepted_condition(parameters, cond1, 2)


for i in temp:
    print(i)


    
