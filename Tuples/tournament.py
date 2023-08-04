HEADER_FORMAT = 'Team                           | MP |  W |  D |  L |  P'
ROW_FORMAT = '{:<30} | {:>2} | {:>2} | {:>2} | {:>2} | {:>2}'

def tally(rows):

    teams_results = {}

    for match in rows:
        team_one, team_two, result = match.split(";")

        if team_one not in teams_results:
            teams_results[team_one] = [0] * 5
        
        if team_two not in teams_results:
            teams_results[team_two] = [0] * 5
        
        # Number of Match Played(MP)
        teams_results[team_one][0] += 1
        teams_results[team_two][0] += 1 

        # Check results
        if result == "win":

            # Team__one wins
            teams_results[team_one][1] += 1 # Match Win (W)
            teams_results[team_one][4] += 3 # Points (P)
            # Team_two loss
            teams_results[team_two][3] += 1 # Match loss (L)

        elif result == "loss":

            # Team__one loss
            teams_results[team_one][3] += 1 # Match loss (L)
            # Team_two win
            teams_results[team_two][1] += 1 # Match Win (W)
            teams_results[team_two][4] += 3 # Points (P)

        else:
            # Teams drawn
            teams_results[team_one][2] += 1 # Matches Drawn (D)
            teams_results[team_one][4] += 1 # Points (P)
            teams_results[team_two][2] += 1 # Matches Drawn (D)
            teams_results[team_two][4] += 1 # Points (P)

    # Create table with a tuple for every teams and its results sorted by points(P)
    # If teams are the same points, sort by name
    teams_results = sorted(teams_results.items(), key = lambda team: (-team[1][-1], team[0]))

    # return [HEADER_FORMAT] + [ROW_FORMAT.format(team, mp, w, d, l, p) for team, (mp, w, d, l, p) in teams_results]
    print(HEADER_FORMAT)
    for row in teams_results:
        team, (mp, w, d, l, p) = row
        print(ROW_FORMAT.format(team, mp, w, d, l, p))


results = [
            "Courageous Californians;Devastating Donkeys;win",
            "Allegoric Alaskans;Blithering Badgers;win",
            "Devastating Donkeys;Allegoric Alaskans;loss",
            "Courageous Californians;Blithering Badgers;win",
            "Blithering Badgers;Devastating Donkeys;draw",
            "Allegoric Alaskans;Courageous Californians;draw",
        ]
tally(results)