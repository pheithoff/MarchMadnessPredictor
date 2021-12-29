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

def Normalize_Results(resultsList):
    minScore = 9999
    maxScore = -9999
    resultsList = resultsList[1:]
    for result in resultsList:
        # print(result)
        temp = float(result[2])
        # print(temp)
        if temp < minScore:
            minScore = temp
        if temp > maxScore:
            maxScore = temp
    
    
    for result in resultsList:
        # print(result)
        temp = float(result[2])
        # Scale values between 0 and 1 with the max score being 1
        # the min score being 0 and 0 being -0.5
        if temp > 0:
            temp = (0.5)*(temp)/(maxScore)+0.5
        else:
            temp = (0.5)*(temp-minScore)/(-minScore)
        
        result[2] = temp
    
    return resultsList