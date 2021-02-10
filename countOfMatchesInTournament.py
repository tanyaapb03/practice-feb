#psudocode#
# Input: n = 7
# Output: 6
# Explanation: Details of the tournament: 
# - 1st Round: Teams = 7, Matches = 3, and 4 teams advance.
# - 2nd Round: Teams = 4, Matches = 2, and 2 teams advance.
# - 3rd Round: Teams = 2, Matches = 1, and 1 team is declared the winner.
# Total number of matches = 3 + 2 + 1 = 6.
# If teams even(2,6,.....),matches played=n/2 and n / 2 teams advance to the next round.
# odd,  A total of (n - 1) / 2 matches are played, and (n - 1) / 2 + 1 teams advance to the next round.


def tournamet(n):
   
   
    matches=0
    
    while n>1:
        if n%2==0:
            matches =matches+(n/2)
            n=int(n/2)
        if n%2!=0:
            matches = matches + (n-1)/2
            n=int((n - 1) / 2 )+ 1 

    return matches
print(tournamet(14))

