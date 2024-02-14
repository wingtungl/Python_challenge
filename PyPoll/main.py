import os
import csv
csvpath = os.path.join('Resources','election_data.csv')

total_vote= 0
candidate_list=[]
candidate_votes={}
candidate_info= []

#Read CSV
with open(csvpath)as csvfile:
    csvreader= csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
#Total vote
    for row in csvreader:
        total_vote= total_vote+1
        candidate=row[2]
        if candidate not in candidate_list:
            candidate_list.append(candidate)
            candidate_votes[candidate]=0
        candidate_votes[candidate]=candidate_votes[candidate]+1
#Each candidate vote and percentage and winner
    winner=["",0]
    for candidate,votes in candidate_votes.items():
        votes=candidate_votes[candidate]
        percentage_vote=votes/total_vote*100
        candidate_info.append([candidate, f"{percentage_vote:.2f}%", (votes)])
        print(f"{candidate} {votes} ({percentage_vote})")
        if winner[1]<votes:
            winner[1]=votes
            winner[0]=candidate
        print(winner)
   
# Analysis in terminal
print("Election Results")
print("---------------------")
print(f"Total Votes:{total_vote}")
print("---------------------")
print(f"{candidate_info}")
print("---------------------")
print(f"Winner:{winner[0]}")
print("---------------------")

# analysis in text file
file2 = open('pyroll2.txt', 'w')
print("Election Results", file = file2)
print("---------------------", file = file2)
print(f"Total Votes:{total_vote}", file = file2)
print("---------------------", file = file2)
print(f"{candidate_info}", file = file2)
print("---------------------", file = file2)
print(f"Winner:{winner[0]}", file = file2)
print("---------------------", file = file2)



