# NHL SEASON SIMULATOR (based on 2014-2015 statistics)
# By Drew Roberts
# Personal Project

import team
import operator
import time
import sys
from random import randint

null = team.Team
anaheim = team.Team("Anaheim Ducks", 15.7, 81.0, 1.04, 2.78, 2.70, "w", "p")
arizona = team.Team("Arizona Coyotes", 20.0, 76.7, 0.62, 2.01, 3.26, "w", "p")
boston = team.Team("Boston Bruins", 17.8, 82.0, 1.04, 2.55, 2.45, "e", "a")
buffalo = team.Team("Buffalo Sabres", 13.40, 75.1, 0.61, 1.87, 3.28, "e", "a")
calgary = team.Team("Calgary Flames", 18.8, 80.6, 1.04, 2.89, 2.60, "w", "p")
carolina = team.Team("Carolina Hurricanes", 18.8, 84.7, 0.76, 2.23, 2.67, "e", "m")
chicago = team.Team("Chicago Blackhawks", 17.6, 83.4, 1.19, 2.68, 2.27, "w", "c")
colorado = team.Team("Colorado Avalanche", 15.0, 84.6, 0.99, 2.55, 2.72, "w", "c")
columbus = team.Team("Columbus Blue Jackets", 21.7, 80.2, 0.88, 2.77, 3.02, "e", "m")
dallas = team.Team("Dallas Stars", 19.0, 80.7, 0.98, 3.13, 3.13, "w", "c")
detroit = team.Team("Detroit Red Wings", 23.8, 80.9, 1.05, 2.82, 2.57, "e", "a")
edmonton = team.Team("Edmonton Oilers", 17.7, 76.7, 0.68, 2.35, 3.37, "w", "p")
florida = team.Team("Florida Panthers", 16.3, 80.0, 1.03, 2.42, 2.60, "e", "a")
los_angeles = team.Team("Los Angeles Kings", 19.0, 80.9, 1.18, 2.66, 2.40, "w", "p")
minnesota = team.Team("Minnesota Wild", 15.8, 86.3, 1.14, 2.77, 2.42, "w", "c")
montreal = team.Team("Montreal Canadiens", 16.5, 83.7, 1.18, 2.61, 2.24, "e", "a")
nashville = team.Team("Nashville Predators", 16.2, 80.8, 1.26, 2.76, 2.46, "w", "c")
new_jersey = team.Team("New Jersey Devils", 19.3, 80.6, 0.93, 2.15, 2.55, "e", "m")
new_york_i = team.Team("New York Islanders", 18.7, 78.0, 1.08, 2.99, 2.73, "e", "m")
new_york_r = team.Team("New York Rangers", 16.8, 84.3, 1.32, 3.02, 2.28, "e", "m")
ottawa = team.Team("Ottawa Senators", 16.8, 82.9, 1.09, 2.83, 2.54, "e", "a")
philadelphia = team.Team("Philadelphia Flyers", 23.4, 77.1, 1.01, 2.58, 2.72, "e", "m")
pittsburgh = team.Team("Pittsburgh Penguins", 19.3, 84.8, 1.09, 2.65, 2.49, "e", "m")
san_jose = team.Team("San Jose Sharks", 21.6, 78.5, 0.91, 2.73, 2.76, "w", "p")
st_louis = team.Team("St. Louis Blues", 22.3, 83.7, 1.18, 2.92, 2.40, "w", "c")
tampa_bay = team.Team("Tampa Bay Lightning", 18.8, 83.7, 1.28, 3.16, 2.51, "e", "a")
toronto = team.Team("Toronto Maple Leafs", 15.9, 80.4, 0.80, 2.51, 3.13, "e", "a")
vancouver = team.Team("Vancouver Canucks", 19.3, 85.7, 0.96, 2.88, 2.68, "w", "p")
washington = team.Team("Washington Capitals", 25.3, 81.2, 1.08, 2.89, 2.43, "e", "m")
winnipeg = team.Team("Winnipeg Jets", 17.8, 81.8, 1.15, 2.72, 2.49, "w", "c")

teamsList = []
teamsList.append(null)
teamsList.append(anaheim)
teamsList.append(arizona)
teamsList.append(boston)
teamsList.append(buffalo)
teamsList.append(calgary)
teamsList.append(carolina)
teamsList.append(chicago)
teamsList.append(colorado)
teamsList.append(columbus)
teamsList.append(dallas)
teamsList.append(detroit)
teamsList.append(edmonton)
teamsList.append(florida)
teamsList.append(los_angeles)
teamsList.append(minnesota)
teamsList.append(montreal)
teamsList.append(nashville)
teamsList.append(new_jersey)
teamsList.append(new_york_i)
teamsList.append(new_york_r)
teamsList.append(ottawa)
teamsList.append(philadelphia)
teamsList.append(pittsburgh)
teamsList.append(san_jose)
teamsList.append(st_louis)
teamsList.append(tampa_bay)
teamsList.append(toronto)
teamsList.append(vancouver)
teamsList.append(washington)
teamsList.append(winnipeg)


# REGULAR SEASON
game = 1
check = 0

while game <= 82:
    i = 1
    check = 0
    while i < 31:
        if teamsList[i].wins + teamsList[i].losses < game:
            check += 1
        i += 1

    if check != 0:
            home_team = randint(1, 30)
            away_team = randint(1, 30)

            if home_team != away_team and teamsList[home_team].wins + teamsList[home_team].losses < game and teamsList[away_team].wins + teamsList[away_team].losses < game:
                h = randint(0, 10)
                h2 = randint(0, teamsList[home_team].total)
                home_score = h * h2
                a = randint(0, 10)
                a2 = randint(0, teamsList[away_team].total)
                away_score = a * a2

                if home_score > away_score:
                    teamsList[home_team].wins += 1
                    teamsList[away_team].losses += 1
                else:
                    teamsList[home_team].losses += 1
                    teamsList[away_team].wins += 1
    else:
            game += 1

teamsList.sort(key=operator.attrgetter("wins"), reverse=True)
t = 0
while t < 31:
    if teamsList[t].name != "null":
        print(teamsList[t].name, ": ", teamsList[t].wins)
    t += 1

s = 0
atlantic = []
metropolitan = []
central = []
pacific = []

while s < 31:
    if teamsList[s].division == "a":
        atlantic.append(teamsList[s])
    elif teamsList[s].division == "m":
        metropolitan.append(teamsList[s])
    elif teamsList[s].division == "c":
        central.append(teamsList[s])
    elif teamsList[s].division == "p":
        pacific.append(teamsList[s])

    s += 1

atlantic.sort(key=operator.attrgetter("wins"), reverse=True)
metropolitan.sort(key=operator.attrgetter("wins"), reverse=True)
central.sort(key=operator.attrgetter("wins"), reverse=True)
pacific.sort(key=operator.attrgetter("wins"), reverse=True)

y = 0
while y < 3:
    atlantic[y].playoffs = True
    metropolitan[y].playoffs = True
    central[y].playoffs = True
    pacific[y].playoffs = True
    y += 1

eastern = []
western = []

h = 0
while h < 31:
    if teamsList[h].conference == "e":
        eastern.append(teamsList[h])
    elif teamsList[h].conference == "w":
        western.append(teamsList[h])

    h += 1

eastern.sort(key=operator.attrgetter("wins"), reverse=True)
western.sort(key=operator.attrgetter("wins"), reverse=True)

u = 0
break_e = 0
while u < 16 and break_e < 2:
    if eastern[u].playoffs == False:
        eastern[u].playoffs = True
        break_e += 1
    u += 1

x = 0
break_w = 0

while x < 14 and break_w < 2:
    if western[x].playoffs == False:
        western[x].playoffs = True
        break_w += 1
    x += 1

playoffTeams = []
b = 0
while b < 31:
    if teamsList[b].playoffs == True:
        playoffTeams.append(teamsList[b])
    b += 1

print("\n\n\nThe teams that made the Stanley Cup playoffs are the...\n")

x = 0
while x < 16:
    print(playoffTeams[x].name, ": ", playoffTeams[x].conference)
    x += 1

#input("Press Enter to start the Stanley Cup playoffs!")
eastern_playoffs_teams = []
western_playoffs_teams = []

x = 0
while x < 16:
    if playoffTeams[x].conference == "e":
        eastern_playoffs_teams.append(playoffTeams[x])
    elif playoffTeams[x].conference == "w":
        western_playoffs_teams.append(playoffTeams[x])
    x += 1

eastern_playoffs_teams.sort(key=operator.attrgetter("wins"), reverse=True)
western_playoffs_teams.sort(key=operator.attrgetter("wins"), reverse=True)

x = 0
y = 7

while x <= 3 and y >= 4:
    e1 = 0
    e2 = 0
    w1 = 0
    w2 = 0

    while e1 < 4 and e2 < 4:
                h = randint(0, 10)
                h2 = randint(0, eastern_playoffs_teams[x].total)
                e_first_score = h * h2
                a = randint(0, 10)
                a2 = randint(0, eastern_playoffs_teams[y].total)
                e_second_score = a * a2

                if e_first_score > e_second_score:
                    e1 += 1
                    print("The ", eastern_playoffs_teams[x].name, " beat the ", eastern_playoffs_teams[y].name)
                else:
                    e2 += 1
                    print("The ", eastern_playoffs_teams[y].name, " beat the ", eastern_playoffs_teams[x].name)

                if e1 == 4:
                    eastern_playoffs_teams[x].second_round = True
                elif e2 == 4:
                    eastern_playoffs_teams[y].second_round = True

    while w1 < 4 and w2 < 4:
                f = randint(0, 10)
                f2 = randint(0, western_playoffs_teams[x].total)
                w_first_score = f * f2
                z = randint(0, 10)
                z2 = randint(0, western_playoffs_teams[y].total)
                w_second_score = z * z2
                if w_first_score > w_second_score:
                    w1 += 1
                    print("The ", western_playoffs_teams[x].name, " beat the ", western_playoffs_teams[y].name)
                else:
                    w2 += 1
                    print("The ", western_playoffs_teams[y].name, " beat the ", western_playoffs_teams[x].name)

                if w1 == 4:
                    western_playoffs_teams[x].second_round = True
                elif w2 == 4:
                    western_playoffs_teams[y].second_round = True
    x += 1
    y -= 1

# SECOND ROUND
print("\n\nSECOND ROUND OF THE STANLEY CUP PLAYOFFS\n\n")
g = 0
e_second_round_teams = []
w_second_round_teams = []
while g < 31:
    if teamsList[g].second_round:
        print(teamsList[g].name)
        if teamsList[g].conference == "e":
            e_second_round_teams.append(teamsList[g])
        elif teamsList[g].conference == "w":
            w_second_round_teams.append(teamsList[g])
    g += 1

e_second_round_teams.sort(key=operator.attrgetter("wins"), reverse=True)
w_second_round_teams.sort(key=operator.attrgetter("wins"), reverse=True)

x = 0
y = 3

while x <= 1 and y >= 2:
    e1 = 0
    e2 = 0
    w1 = 0
    w2 = 0

    while e1 < 4 and e2 < 4:
                h = randint(0, 10)
                h2 = randint(0, e_second_round_teams[x].total)
                e_first_score = h * h2
                a = randint(0, 10)
                a2 = randint(0, e_second_round_teams[y].total)
                e_second_score = a * a2

                if e_first_score > e_second_score:
                    e1 += 1
                    print("The ", e_second_round_teams[x].name, " beat the ", e_second_round_teams[y].name)
                else:
                    e2 += 1
                    print("The ", e_second_round_teams[y].name, " beat the ", e_second_round_teams[x].name)

                if e1 == 4:
                    e_second_round_teams[x].semifinals = True
                elif e2 == 4:
                    e_second_round_teams[y].semifinals = True

    while w1 < 4 and w2 < 4:
                f = randint(0, 10)
                f2 = randint(0, w_second_round_teams[x].total)
                w_first_score = f * f2
                z = randint(0, 10)
                z2 = randint(0, w_second_round_teams[y].total)
                w_second_score = z * z2
                if w_first_score > w_second_score:
                    w1 += 1
                    print("The ", w_second_round_teams[x].name, " beat the ", w_second_round_teams[y].name)
                else:
                    w2 += 1
                    print("The ", w_second_round_teams[y].name, " beat the ", w_second_round_teams[x].name)

                if w1 == 4:
                    w_second_round_teams[x].semifinals = True
                elif w2 == 4:
                    w_second_round_teams[y].semifinals = True
    x += 1
    y -= 1


# SEMIFINALS
print("\n\nSEMIFINALS OF THE STANLEY CUP PLAYOFFS\n\n")
g = 0
e_semifinals_teams = []
w_semifinals_teams = []
while g < 31:
    if teamsList[g].semifinals:
        print(teamsList[g].name)
        if teamsList[g].conference == "e":
            e_semifinals_teams.append(teamsList[g])
        elif teamsList[g].conference == "w":
            w_semifinals_teams.append(teamsList[g])
    g += 1

e_semifinals_teams.sort(key=operator.attrgetter("wins"), reverse=True)
w_semifinals_teams.sort(key=operator.attrgetter("wins"), reverse=True)

e1 = 0
e2 = 0
w1 = 0
w2 = 0

while e1 < 4 and e2 < 4:
                h = randint(0, 10)
                h2 = randint(0, e_semifinals_teams[0].total)
                e_first_score = h * h2
                a = randint(0, 10)
                a2 = randint(0, e_semifinals_teams[1].total)
                e_second_score = a * a2

                if e_first_score > e_second_score:
                    e1 += 1
                    print("The ", e_semifinals_teams[0].name, " beat the ", e_semifinals_teams[1].name)
                else:
                    e2 += 1
                    print("The ", e_semifinals_teams[1].name, " beat the ", e_semifinals_teams[0].name)

                if e1 == 4:
                    e_semifinals_teams[0].finals = True
                elif e2 == 4:
                    e_semifinals_teams[1].finals = True

while w1 < 4 and w2 < 4:
                f = randint(0, 10)
                f2 = randint(0, w_semifinals_teams[0].total)
                w_first_score = f * f2
                z = randint(0, 10)
                z2 = randint(0, w_semifinals_teams[1].total)
                w_second_score = z * z2
                if w_first_score > w_second_score:
                    w1 += 1
                    print("The ", w_semifinals_teams[0].name, " beat the ", w_semifinals_teams[1].name)
                else:
                    w2 += 1
                    print("The ", w_semifinals_teams[1].name, " beat the ", w_semifinals_teams[0].name)

                if w1 == 4:
                    w_semifinals_teams[0].finals = True
                elif w2 == 4:
                    w_semifinals_teams[1].finals = True

# STANLEY CUP FINALS
print("\n\nTHE STANLEY CUP FINALS\n\n")
final_two = []
g = 0
while g < 31:
    if teamsList[g].finals:
        print(teamsList[g].name)
        final_two.append(teamsList[g])
    g += 1

e = 0
w = 0
champions_list = open("stanleycupchampions.txt", 'a')

while e < 4 and w < 4:
                f = randint(0, 10)
                f2 = randint(0, final_two[0].total)
                first_score = f * f2
                z = randint(0, 10)
                z2 = randint(0, final_two[1].total)
                second_score = z * z2
                if first_score > second_score:
                    e += 1
                    print("The ", final_two[0].name, "(", final_two[0].wins, ",", final_two[0].losses, ") beat the ", final_two[1].name,  "(", final_two[1].wins, ",", final_two[1].losses, ")   |   ", final_two[0].name, " : ", e, " - ", final_two[1].name, " : ", w)
                    # time.sleep(2)
                else:
                    w += 1
                    print("The ", final_two[1].name,  "(", final_two[1].wins, ",", final_two[1].losses, ") beat the ", final_two[0].name,  "(", final_two[0].wins, ",", final_two[0].losses, ")   |   ", final_two[1].name, " : ", w, " - ", final_two[0].name, " : ", e)
                    # time.sleep(2)

                if e == 4:
                    print("\nThe ", final_two[0].name, " have won the Stanley Cup!!!\n")
                    champion = [final_two[0].name, " beat the ", final_two[1].name, e, " games to ", w, "to win the Stanley Cup\n"]
                    champions_list.write(final_two[0].name + "\n")
                elif w == 4:
                    print("\nThe ", final_two[1].name, " have won the Stanley Cup!!!\n")
                    champion = [final_two[1].name, " beat the ", final_two[0].name, w, " games to ", e, "to win the Stanley Cup\n"]
                    champions_list.write(final_two[1].name + "\n")

champions_list.close()

with open("stanleycupchampions.txt") as f:
    seasons = sum(1 for line in f)
f.close()

i = 0
searchfile = open("stanleycupchampions.txt", "r")
while i < 31:
    for line in searchfile:
        if teamsList[i].name in line:
            teamsList[i].numOfCups += 1
    searchfile.seek(0)
    i += 1
searchfile.close()

teamsList.sort(key=operator.attrgetter("numOfCups"), reverse=True)

i = 0

while i < 1:
    user_team = input("To find out a team's Stanley Cup statistics, please enter a team name or enter 0 to exit.\n Enter \"Top Ten\" to see the top ten teams in the Stanley Cup Finals of all-time: ")

    if user_team == "Top Ten":
        p = 0
        while p < 10:
            print("#", p+1, ": ", teamsList[p].name, "-", teamsList[p].numOfCups, "in" , seasons, "seasons - ", "Percentage:", round(teamsList[p].numOfCups/seasons * 100, 2), "%")
            p += 1
        print("\n")

    elif user_team == "All":
        p = 0
        while p < 30:
            print("#", p+1, ": ", teamsList[p].name, "-", teamsList[p].numOfCups, "in" , seasons, "seasons - ", "Percentage:", round(teamsList[p].numOfCups/seasons * 100, 2), "%")
            p += 1
        print("\n")

    else:
        team_check = 0
        j = 0
        while j < 31:
            if user_team == teamsList[j].name:
                team_check += 1
                teamPercentage = round(teamsList[j].numOfCups/seasons * 100, 2)
                print("The", teamsList[j].name, "have won the Stanley Cup", teamsList[j].numOfCups, "time(s) in", seasons, "season(s).")
                print("Percentage:", teamPercentage, "%\n")
            j += 1

        if team_check == 0:
            print("You either entered 0 or an invalid team name. Exiting program...")
            break
