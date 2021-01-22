from pypair import pypair

parameters = [ [ "Brand X", "Brand Y","Brand A" ]
             , [ "NT", "2000", "XP"]
             , [ "Internal", "Modem" ]
             , ['This', 'That']
             ]


test = pypair(parameters,2)

for i in test:
    print(i)

