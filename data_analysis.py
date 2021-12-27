# -*- coding: utf-8 -*-
"""
Created on Sun Dec 26 11:01:58 2021

@author: patrickh
"""

# The purpose of this Function is to normalize all of the features found in
# the given team dictionary and normalize them between 0 and 1 using 
# min-max normalization
def Normalize_TeamDictionary(teamDict):
    # Get stats keys
    statsKeys = list(list(teamDict.values())[0].keys())
    

    # loop through each stat
    for stat in statsKeys:
        statMin = 99999
        statMax = -9999
        
        # Find min and max of each statistic by looping through the teams
        for team in teamDict:
            try:
                currStat = float(teamDict[team][stat])
                if currStat < statMin:
                    statMin = currStat
                if currStat > statMax:
                    statMax = currStat
            except ValueError:
                print("Value Error")
            
            
        # Scale each stat by max and min using min-max normalization
        for team in teamDict:
            try:
                teamDict[team][stat] = str((float(teamDict[team][stat]) - statMin) / (statMax - statMin))
            except ValueError:
                print("")
        
    
    
    return teamDict