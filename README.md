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
- The data set was analyzed and the output included in this repository, in the Analysis folder. Supporting files are located in the Resources folder.
### Resources
Data was sourced from the following file and audited with the following software:
- election_results.csv retrieved from UCF Canvas on 10/21/2022
- Software: Python 3.7, Visual Studio Code 1.72.2 

## Election Audit Results
Analysis of the election results shows that:
- There were 369,711 total votes cast. 
- The code that enabled this output begins with setting a variable to track total votes, then creating a **for** loop to iterate through the election_results.csv file and track the amount of votes cast and tallying the votes for the appropriate candidate.
### ![For Loop](https://github.com/scottemac00/Election_Analysis/blob/3999b1b03f407609f25dfc2281638f9f346d2778/Resources/Candidate%20Vote%20Tally%20Loop.png)  
- This was verified by opening the spreadsheet and correlating the last cell used![election_results.csv last cell](https://github.com/scottemac00/Election_Analysis/blob/3999b1b03f407609f25dfc2281638f9f346d2778/Resources/Total%20Cell%20Count.png) then subtracting one. 
### Results by County
- The following image displays the script's output with votes by county:
### ![](https://github.com/scottemac00/Election_Analysis/blob/77e4ba4937e886462a881fb043f5b988f24d13c0/Resources/County%20Tallies.png)

### Results by Candidate
- As noted in **bold** below, Diana DeGette won the election.
  - Charlese Casper Stockham received 23.0% of the vote with 85,213 votes.
  - **Diana DeGette received 73.8% of the vote with 272,892 votes.**
  - Raymon Anthony Doane received 3.1% of the vote with 11,606 votes.  
   
## Election Audit Summary
  The script that enables this analysis may be run at various times during an election to augment current counting mechanisms. With minor modification, we might use this for elections at various levels of government or whenever votes are tallied, regardless of candidate or issue on the ballot. As with any data, the output is only as good as the input. Modifying the scipt to further automate (e.g., iterate) over the data set, even as the set grows, will give the organization near real-time results. Another possible data point to collect would be how much time voters spend on each question (if voting is also digital). This could provide insight into how informed and/or decided voters are prior to entering the poll.
