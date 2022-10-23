counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}
for voters in counties_dict.values():
    print(voters)
for county in counties_dict:
    print(counties_dict.get(county))

for county, voters in counties_dict.items():
    print(county,voters)

for county, voters in counties_dict.items():
    print(str(county)  + "County has"  +  str(voters)  +  "registered voters.")

voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
                {"county":"Denver", "registered_voters": 463353},
                {"county":"Jefferson", "registered_voters": 432438}]

for counties_dict in voting_data:
    print(counties_dict) 

for counties_dict in voting_data:
    for value in counties_dict.values():
        print(value) 

for counties_dict in voting_data:
    print(counties_dict["county"])                          

candidate_votes = int(input("How many votes did the candidate get in the election? "))
total_votes = int(input("What is the total number of votes in the election? "))
message_to_candidate = (
    f"You received {candidate_votes:,} number of votes. "
    f"The total number of votes in the election was {total_votes:,}. "
    f"You received {candidate_votes / total_votes * 100:.2f}% of the total votes.")

print(message_to_candidate)




