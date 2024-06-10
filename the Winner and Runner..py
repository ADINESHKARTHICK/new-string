import random
Voter_list = list(range(1, 11))
candidates = ['A', 'B', 'C']
votes = {candidate: 0 for candidate in candidates}
for voter in Voter_list:
    vote = random.choice(candidates)
    votes[vote] += 1
    print(f"Voter {voter} casted vote for candidate {vote}")
sorted_votes = sorted(votes.items(), key=lambda x: x[1], reverse=True)
winner, winner_votes = sorted_votes[0]
runner_up, runner_up_votes = sorted_votes[1]
winner_voters = [voter for voter in Voter_list if votes[winner] > votes[runner_up]]
runner_up_voters = [voter for voter in Voter_list if votes[runner_up] > votes[winner]]
print("\nElection Results:")
print("Winner:", winner, "with", winner_votes, "votes")
print("Runner-up:", runner_up, "with", runner_up_votes, "votes")
print("\nMembers who voted for the winner:", winner_voters)
print("Members who voted for the runner-up:", runner_up_voters)
