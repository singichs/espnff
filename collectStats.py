import operator
import sys

from espnff import League

week_number = sys.argv[1]

league_id = 1811748
year = 2018

league = League(league_id, year)

#League Name
print league.settings.name + "\n\n"

standings = {}
for team in league.teams:
	standings[str(team.team_name)] = team.wins
standings = sorted(standings.items(), key=operator.itemgetter(1), reverse=True)

for x in range(0,13):
	print str(standings[x][0]) + " " + str(standings[x][1])

#Power Rankings
print "Week " + week_number + " power rankings:"
for x in range(0,13):
	test =  league.power_rankings(int(week_number))[x][1]
	print str(x+1) + ". " + str(test)[5:-1]
print "\n"


#prints a list of the scores each team put up
print "Team scores list:"
names = {}
for team in league.teams:
	names[str(team.team_name)] = team.scores
for team in names:
	print team + " : " + str(names[team])
print "\n"


expected_wins = {}
for team in league.teams:
	expected_wins[str(team.team_name)] = 0


#prints the scores each team put up and orders highest score to lowest score
for x in range(0,13):
	week_score = {}
	print "Week " + str(x+1) + ":"
	for team in league.teams:
		week_score[team.team_name] = team.scores[x]

	sorted_scores = sorted(week_score.items(), key=operator.itemgetter(1), reverse=True)
	
	#print sorted_scores
	counter = 0
	for key, value in sorted_scores:
		print str(counter+1) + ". " + str(key) + " : " +  str(value)
		if x < (int(week_number)-1):
			expected_wins[str(key)] += ((13-counter)/13.0)
		counter += 1
	print "\n"


ordered_expected_wins = sorted(expected_wins.items(), key=operator.itemgetter(1), reverse=True)

print "\nExpected Number of Wins:"
counter = 0
for key, value in ordered_expected_wins:
	print str(counter+1) + ". " + str(key) + " : " + '{0:.20f}'.format(value)
	counter += 1



# team0 = league.teams[0]
# team1 = league.teams[1]
# team2 = league.teams[2]
# team3 = league.teams[3]
# team4 = league.teams[4]
# team5 = league.teams[5]
# team6 = league.teams[6]
# team7 = league.teams[7]
# team8 = league.teams[8]
# team9 = league.teams[9]
# team10 = league.teams[10]
# team11 = league.teams[11]
# team12 = league.teams[12]
# team13 = league.teams[13]

# print team0.team_name + " : " + str(team0.scores) + "\n"
# print team1.team_name + " : " + str(team1.scores) + "\n"
# print team2.team_name + " : " + str(team2.scores) + "\n"
# print team3.team_name + " : " + str(team3.scores) + "\n"
# print team4.team_name + " : " + str(team4.scores) + "\n"
# print team5.team_name + " : " + str(team5.scores) + "\n"
# print team6.team_name + " : " + str(team6.scores) + "\n"
# print team7.team_name + " : " + str(team7.scores) + "\n"
# print team8.team_name + " : " + str(team8.scores) + "\n"
# print team9.team_name + " : " + str(team9.scores) + "\n"
# print team10.team_name + " : " + str(team10.scores) + "\n"
# print team11.team_name + " : " + str(team11.scores) + "\n"
# print team12.team_name + " : " + str(team12.scores) + "\n"
# print team13.team_name + " : " + str(team13.scores) + "\n"