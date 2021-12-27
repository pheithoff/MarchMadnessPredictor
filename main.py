import csv
import re
import os
import sys
import stat_extraction
import data_analysis

# Stats keys used in dictionary
statsKeys = ["Seed", "Off Eff", "Avg Scoring Margin", "Eff FG%", "Off Reb%", "FT%", "Def Reb%", "Block%",
             "Steal Per Poss", "Assist TO ratio", "Fouls per poss", "Def Eff", "Opp Eff FG %", "Win %", "KenPom Rank",
             "Avg Height", "Avg Experience", "TO %", "Adj Efficiency Margin",]
headerFields = ["Team-Year"]+statsKeys[:]

statsDict = {key: None for key in statsKeys}

def writeTeamsDictToCSV(teamsDict):
    with open("team_stats_updated.csv", "w", newline='') as f:
        w = csv.DictWriter(f, headerFields)
        w.writeheader()
        for k in teamsDict:
            w.writerow({field: teamsDict[k].get(field) or k for field in headerFields})

def readTeamDictFromCSV():
    teamsDictionary = dict()
    i = 0
    with open("team_stats.csv", mode="r") as fhandle:
        for line in fhandle:
            words = line.rstrip("\n").split(",")
            if i == 0:
                headers = words.copy()
                i += 1
            else:
                teamsDictionary[words[0]] = dict(statsDict)
                for statIndex in range(1, len(words)):
                    try:
                        teamsDictionary[words[0]][headers[statIndex]] = float(words[statIndex])
                    except ValueError:
                        teamsDictionary[words[0]][headers[statIndex]] = words[statIndex]

    return teamsDictionary

def writeResultsToCSV(result):
    with open('results_updated.csv', 'w', newline='') as out:
        csv_out = csv.writer(out)
        csv_out.writerow(['Team1', 'Team2', 'Score'])
        for row in result:
            csv_out.writerow(row)
            
def readResultsFromCSV():
    resultList = []
    with open("results.csv", mode="r") as f:
        for line in f:
            words = line.rstrip("\n").split(",")
            resultList.append(words)
            
    return resultList
            

if __name__ == "__main__":
    # Dictionary containing teams with their specific stats dictionary.
    teamsDict = {}

    # List of results. Results will be formatted as a tuple with format: (Team1, Team2, PointDiff)
    # Point Diff > 0 if team1 won and < 0 if team2 won.
    resultsList = []
    from itertools import islice


    # directory = 'Bracket Results'
    # for filename in os.listdir(directory):
    #     with open(directory + '/' + filename, 'r') as f:
    #         year = f.name[16:20]
    #         while True:
    #             next_6_lines = list(islice(f, 6))
    #             if not next_6_lines:
    #                 break
    #             #sort_lines(next_6_lines)
    #             # Extract data from the 6 lines
    #             line1 = re.sub('=', '= ', next_6_lines[0]).split()
    #             line2 = re.sub('=', '= ', next_6_lines[1]).split()
    #             line3 = re.sub('=', '= ', next_6_lines[2]).split()
    #             line4 = re.sub('=', '= ', next_6_lines[3]).split()
    #             line5 = re.sub('=', '= ', next_6_lines[4]).split()
    #             line6 = re.sub('=', '= ', next_6_lines[5]).split()

    #             team1 = line2[2:]
    #             team1 = ' '.join(team1)
    #             temp = re.search("XX(.+?)]", team1)
    #             if temp is not None:
    #                 team1 = temp.group(1)
    #             team1 = re.sub("'''", '', team1)
    #             team1_year = team1 + '-' + year

    #             team1_score = re.sub("'", '', line3[2])
    #             team1_score = re.sub("\*", '', team1_score)
    #             team1_score = int(team1_score)

    #             if team1_year not in teamsDict:
    #                 seed1 = re.sub("'", '', line1[2])
    #                 # print(seed1)
    #                 # print(team1_year)
    #                 teamsDict[team1_year] = dict(statsDict)
    #                 teamsDict[team1_year]['Seed'] = int(seed1)

    #             team2 = line5[2:]
    #             team2 = ' '.join(team2)
    #             temp = re.search("XX(.+?)]", team2)
    #             if temp is not None:
    #                 team2 = temp.group(1)
    #             team2 = re.sub("'''", '', team2)
    #             team2_year = team2 + '-' + year
    #             team2_score = re.sub("'", '', line6[2])
    #             team2_score = re.sub("\*", '', team2_score)
    #             team2_score = int(team2_score)
    #             if team2_year not in teamsDict:
    #                 seed2 = re.sub("'", '', line4[2])
    #                 # print(seed2)
    #                 # print(team2_year)
    #                 teamsDict[team2_year] = dict(statsDict)
    #                 teamsDict[team2_year]['Seed'] = int(seed2)


    #             resultTuple = (team1_year, team2_year, (team1_score - team2_score))
    #             resultsList.append(resultTuple)

    # writeResultsToCSV(resultsList)


    

    teamsDict = readTeamDictFromCSV()
    resultsList = readResultsFromCSV()
    stat_extraction.BracketResultsExtract_html('2004_html.txt', teamsDict, resultsList, statsDict)
    
    
    print(teamsDict)
    print(resultsList)
    
    # updatedTeamsDict = data_analysis.Normalize_TeamDictionary(teamsDict)
    writeResultsToCSV(resultsList)
    writeTeamsDictToCSV(teamsDict)