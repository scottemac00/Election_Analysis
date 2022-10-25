# Election_Analysis

## Overview of Election Audit
A Colorado Board of Elections employee gave me the following tasks to complete the election audit of a recent local congressional election:

    1. Calculate the total number of votes cast.
    2. Get a complete list of candidates who received votes.
    3. Calculate the total number of votes each candidate received.
    4. Calculate the percentage of votes won by each candidate.
    5. Determine the winner of the election based on popular vote.
    6. Tabulate the voter turnout for each county.
    7. Determine the percentage of votes from each county out of the total count.
    8. Identify the county with the highest voter turnout.

### Resources
Data was sourced from the following file and with the following software:
- election_results.csv retrieved from UCF Canvas on 10/21/2022
- Software: Python 3.7, Visual Studio Code 1.72.2 

## Election Audit Results
Analysis of the election results shows that:
- There were 369,711 total votes cast. <INSERT CODE THAT SHOWED HOW TOTAL VOTES WERE TALLIED>
### Results by County
- Provide a breakdown of the number of votes and the percentage of total votes for each county in the precinct. <INSERT IMAGE OF COUNTY OUTPUT>
- Which county had the largest number of votes?
- Provide a breakdown of the number of votes and the percentage of the total votes each candidate received.<INSERT IMAGE OF CANDIDATE OUTPUT>
- Which candidate won the election, what was their vote count, and what was their percentage of the total votes?

### Results by Candidate
- As noted in **bold** below, Diana DeGette won the election.
  - Charlese Casper Stockham received 23.0% of the vote with 85,213 votes.
  - **Diana DeGette received 73.8% of the vote with 272,892 votes.**
  - Raymon Anthony Doane received 3.1% of the vote with 11,606 votes.  
  
  
  ## Election Audit Summary
  The script that enables this analysis may be run at various times during an election to augment current counting mechanisms. With minor modification, we might use this for elections at various levels of government or whenever votes are tallied, regardless of candidate or issue on the ballot. As with any data, the output is only as good as the input. Modifying the scipt to further automate (e.g., iterate) over the data set, even as the set grows, will give the organization near real-time results. Another possible data point to collect would be how much time voters spend on each question (if voting is also digital). This could provide insight into how informed and/or decided voters are prior to entering the poll.
