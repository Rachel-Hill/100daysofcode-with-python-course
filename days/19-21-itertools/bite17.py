from itertools import combinations
#friends, team_size=2, order_does_matter=True

def friends_teams(friends, team_size=2, order_does_matter=False):
    teams=combinations(friends,2)
    return teams

if __name__ == '__main__':
    friends = 'Bob Dante Julian Martin'.split()
    print(list(friends_teams(friends)))
