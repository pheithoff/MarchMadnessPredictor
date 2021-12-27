# -*- coding: utf-8 -*-
"""
Created on Fri Dec 24 08:56:26 2021

@author: patrickh
"""
import urllib.request
import os
import numpy as np

# Gets url string for the teamrankings website. If the specific stat does 
# not exist then return "NaN"
def getTeamRankingsUrl(stat, year):
    #The following is the relationship between the stat in the dictionary
    # to the url stat string.
    urlStringDict = {
                    "Off Eff": "offensive-efficiency",
                    "Avg Scoring Margin": "average-scoring-margin",
                    "Eff FG%": "effective-field-goal-pct",
                    "Off Reb%": "offensive-rebounding-pct",
                    "FT%": "free-throw-pct",
                    "Def Reb%": "defensive-rebounding-pct",
                    "Block%": "block-pct",
                    "Steal Per Poss": "steals-perpossession",
                    "Assist TO ratio": "assist--per--turnover-ratio",
                    "Fouls per poss": "personal-fouls-per-possession",
                    "Def Eff": "defensive-efficiency",
                    "Opp Eff FG %": "opponent-effective-field-goal-pct",
                    "Win %": "win-pct-all-games",
                    "TO %": "turnovers-per-possession",                    
        }
    
    # The url format for getting a specific stat is the following:
    # https://www.teamrankings.com/ncaa-basketball/stat/{NAME_OF_STAT}?date={YEAR}-{MONTH}-{DAY}
    # March 10th is the month and day extracted because that is before the first
    # march madness game
    if stat in urlStringDict:
        urlstring = "https://www.teamrankings.com/ncaa-basketball/stat/"+urlStringDict[stat]+"?data="+year+"-03-10"+"&date="+year+"-03-10"
    else:
        urlstring = "NaN"
        
    return urlstring

def index_containing_substring(the_list, substring):
    for i, s in enumerate(the_list):
        if substring in s:
              return i
    return -1

def convertNameforTeamRankings(searchTeamString):
    resultString = searchTeamString

    teamRankingsDict = { 
                        "Ole Miss": "Mississippi",
                        "North Carolina State": "NC State",
                        "Central Connecticut State": "Central Conn",
                        "Southern California": "USC",
                        "Florida Atlantic": "Fla Atlantic",
                        "Pennsylvania": "U Penn",
                        "Penn": "U Penn",
                        "UNC-Wilmington": "NC-Wilmgton",
                        "UNC Wilmington": "NC-Wilmgton", 
                        "Michigan State": "Michigan St",
                        "Western Kentucky": "W Kentucky",
                        "San Diego State": "San Diego St",
                        "Boston College": "Boston Col",
                        "McNeese State": "McNeese St",
                        "Boston University": "Boston U",
                        "UC-Santa Barbara": "UCSB",
                        "Illinois-Chicago": "IL-Chicago",
                        "UW–Milwaukee": "WI-Milwkee",
                        "Milwaukee": "WI-Milwkee",
                        "Central Michigan": "Central Mich",
                        "Colorado State": "Colorado St",
                        "Arizona State": "Arizona St",
                        "Utah St": "Utah State",
                        "UNC-Asheville": "NC-Asheville",
                        "Troy St": "Troy",
                        "Sam Houston St": "Sam Hous St",
                        "South Carolina St": "S Car State",
                        "Saint Joseph's": "St Josephs",
                        "East Tennessee State": "E Tenn St",
                        "Morehead State": "Morehead St",
                        "Alabama State": "Alabama St",
                        "Cleveland State": "Cleveland St",
                        "West Virginia": "W Virginia",
                        "North Dakota State": "N Dakota St",
                        "Robert Morris": "Rob Morris",
                        "Texas A&M": "Texas A&amp;M",
                        "Northern Iowa": "N Iowa",
                        "Cal State Northridge": "Cal St Nrdge",
                        "Oklahoma State": "Oklahoma St",
                        "Florida St.": "Florida St",
                        "Portland St.": "Portland St",
                        "North Carolina": "N Carolina",
                        "Stephen F. Austin": "Ste F Austin",
                        "Morgan State": "Morgan St",
                        "UTSA": "TX-San Ant",
                        "Arkansas-Little Rock": "AR Lit Rock",
                        "Little Rock": "AR Lit Rock",
                        "Indiana State": "Indiana St",
                        "George Mason": "Geo Mason",
                        "Northern Colorado": "N Colorado",
                        "Mississippi State": "Miss State",
                        "Mississippi St": "Miss State",
                        "Saint Peter's": "St Peters",
                        "Florida State": "Florida St",
                        "UNC Asheville": "NC-Asheville",
                        "Kansas State": "Kansas St",
                        "UC Santa Barbara": "UCSB",
                        "Mississippi Valley State": "Miss Val St",
                        "South Florida": "S Florida",
                        "Wichita State": "Wichita St",
                        "South Dakota State": "S Dakota St",
                        "Norfolk State": "Norfolk St",
                        "Long Beach State": "Lg Beach St",
                        "Southern Miss": "S Mississippi",
                        "St. Bonaventure": "St Bonavent",
                        "Loyola (MD)": "Loyola-MD",
                        "Loyola–Chicago": "Loyola-Chi",
                        "Ohio St": "Ohio State",
                        "Middle Tennessee": "Middle Tenn",
                        "Saint Mary's": "St Marys",
                        "James Madison": "James Mad",
                        "New Mexico State": "N Mex State",
                        "North Carolina A&T": "NC A&amp;T",
                        "Long Island": "LIU",
                        "Northwestern State": "NW State",
                        "Florida Gulf Coast": "Fla Gulf Cst",
                        "Mount St. Mary's": "Mt St Marys",
                        "Texas Southern": "TX Southern",
                        "Western Michigan": "W Michigan",
                        "Eastern Kentucky": "E Kentucky",
                        "Coastal Carolina": "Coastal Car",
                        "George Washington": "Geo Wshgtn",
                        "UConn": "Connecticut",
                        "North Florida": "N Florida",
                        "Louisiana–Lafayette": "LA Lafayette",
                        "Massachusetts": "U Mass",
                        "Georgia State": "Georgia St",
                        "Northeastern": "Northeastrn",
                        "Virginia Commonwealth": "VCU",
                        "California-Irvine": "UC Irvine",
                        "Eastern Washington": "E Washingtn",
                        "Southern Methodist": "S Methodist",
                        "SMU": "S Methodist",
                        "Fairleigh Dickinson": "F Dickinson",
                        "Green Bay": "WI-Grn Bay",
                        "Oregon State": "Oregon St",
                        "Cal State Bakersfield": "CS Bakersfld",
                        "Fresno State": "Fresno St",
                        "Virginia Tech": "VA Tech",
                        "South Carolina": "S Carolina",
                        "Jacksonville State": "Jksnville St",
                        "Northern Kentucky": "N Kentucky",
                        "UMBC": "Maryland BC",
                        "UNC Greensboro": "NC-Grnsboro",                  
                        "Cal State Fullerton": "CS Fullerton",
                        "College of Charleston": "Col Charlestn",
                        "TCU": "TX Christian",
                        "UCF": "Central FL",
                        "Gardner–Webb": "Gard-Webb",
                        "Abilene Christian": "Abl Christian",
                        "Grand Canyon": "Grd Canyon",
                        "Georgia Tech": "GA Tech",
        }
    
    if searchTeamString in teamRankingsDict:
        resultString = teamRankingsDict[searchTeamString]
    
    return resultString

# The purpose of this function is to parse through all the teams given as 
# defined in the dictionary given and add to that dictionary from stats
# located in teamrankings.com.
def ExtractStatsFromTeamRankings(teamsDict):
    statsKeys = list(list(teamsDict.values())[0].keys())
    print(statsKeys)
        
    urlstring = ""
    prevurlstring = ""
    i = 0
    
    notFoundList = []
    # Loop through all the stats in the teamsDict per team
    for stat in statsKeys:
        print(stat)
        # Loop through all the teams in the teamsDict
        for team in teamsDict:
            print(team)
            
            # Check if team and stat is N/A or not, indicating that stat
            # has not been looked up yet
            if(teamsDict[team][stat] == "N/A"):
                 # Get the last 4 characters to get year
                year = team[-4:]
                teamName = team[:-5]

                #
                prevurlstring = urlstring
                urlstring = getTeamRankingsUrl(stat, year)
                
                # If this is a new url then open the url and get the list of strings
                # for the data.
                if urlstring != "NaN" and prevurlstring != urlstring:
                    i = i+1
                    fp = urllib.request.urlopen(urlstring)
                    mybytes = fp.read()

                    mystr = mybytes.decode("utf8")
                    lineList = mystr.split('\n')
                    #find the index of where the table starts denoted by the
                    # following string: '\t<table class="tr-table datatable scrollable">'
                    startOfTableIndex = lineList.index('\t<table class="tr-table datatable scrollable">')
                    dataList = lineList[startOfTableIndex:]
                    endOfTableIndex = dataList.index('</table>')
                    dataList = dataList[:endOfTableIndex]
                    #print(dataList)
                    fp.close()
                
                if urlstring != "NaN":
                    searchTeamString = teamName

                    teamIndex = index_containing_substring(dataList, searchTeamString)
                    
                    if teamIndex == -1:
                        notFoundList.append(searchTeamString)
                        print("NOT FOUND:")
                        print(searchTeamString)
                    else:
                        string = dataList[teamIndex+1]
                        indexStart = string.find('sort="')+len('sort="')
                        indexEnd = string.find('">')
                        teamsDict[team][stat] = string[indexStart:indexEnd]
        
                    
    textfile = open("notfound.txt", "w")
    for element in notFoundList:
        textfile.write(element + "\n")
    textfile.close()
                
                    
    return teamsDict    
                
    #urlstring = getTeamRankingsUrl()
    
  
# Results taken from https://www.ncaa.com/news/basketball-men/article/2020-05-07/2004-ncaa-tournament-brackets-scores-stats-records
def BracketResultsExtract_html(textfile, teamDict, resultList, statsDict):
    
    directory = 'Bracket Results'
    year = textfile[0:4]
    print(year)
    
    searchString = 'No. '
    with open(directory + '/' + textfile, 'r') as f:
        for line in f:
            substring_index = line.find(searchString)
            if(substring_index  != -1):
                seedIndex = substring_index + len(searchString)
                line = line[seedIndex:]
                line = line.replace('<', ' <')
                words = line.split()
                print(words)
                curr_index = 0
                seed1 = int(words[curr_index])
                curr_index = curr_index + 1
                team1 = words[curr_index]
                curr_index = curr_index + 1
                integerFound = False
                while(integerFound == False):
                    print(words[curr_index])
                    if words[curr_index].isdigit():
                        team1_score = int(words[curr_index])
                        curr_index += 3 # Add 3 to get to next seed
                        integerFound = True
                    else:
                        team1 = team1 + ' ' + words[curr_index]
                        curr_index += 1
                        
                seed2 = int(words[curr_index])
                curr_index += 1
                team2 = words[curr_index]
                curr_index = curr_index + 1
                integerFound = False
                while(integerFound == False):
                    print(words[curr_index])
                    if words[curr_index].isdigit():
                        team2_score = int(words[curr_index])
                        integerFound = True
                    else:
                        team2 = team2 + ' ' + words[curr_index]
                        curr_index += 1
                
                team1 = convertNameforTeamRankings(team1)
                team2 = convertNameforTeamRankings(team2)
                
                team1_year = team1+'_'+str(year)
                team2_year = team2+'_'+str(year)
                
                teamDict[team1_year] = dict(statsDict)
                teamDict[team1_year]['Seed'] = seed1
                teamDict[team2_year] = dict(statsDict)
                teamDict[team2_year]['Seed'] = seed2
                
                # print(team1_year)
                # print(team2_year)
                # print(seed1)
                # print(seed2)
                # print(team1_score)
                # print(team2_score)
                
                resultTuple = (team1_year, team2_year, (team1_score - team2_score))
                resultList.append(resultTuple)
                
                
                
              
