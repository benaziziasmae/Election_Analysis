# Election_Analysis

## Project Overview

Seth, a Colorad Board of Election employee has given the following tasks to complete the election audit a recent local congressional election.

1. Calulate te total number of votes cast.
2. Get a complete list of candidates who received votes 
3. Calculate the total number of votes each candidate received.
4. Calculate the percentage of votes each candidates won.
5. Determine the winner of the election based on popular vote.

## Resources
- Data Source : Election_results.csv
- Software : Python 3.7 (64 bit) .Visual Studio Code.
- PyPoll_Challenge.py has the code for the challenge requirements.
- PyPoll.py contain the code for the practice in Canvas.
- Election_analysis.txt has an output of the results of Pypoll.py.
- Election_results.txt has the output of the results of PyPoll_challenge.py.

## Summary 

In this Section, we will be analysing the results after running the code of PyPoll_challenge.py. 
The data presented includes three columns: ballot ID, county, and candidate name.

The analysis of the election show that :
- There were "369 711" votes cast in the election 
- The candidates were : 
    - Candidate 1 : Charles Casper Stockham
    - Candidate 2 : Diana DeGette
    - Candidate 3 : Raymon Anthony Doane
- County Names
  - County 1: Jefferson
  - County 2: Denver
  - County 3: Arapahoe
    
 - The candidates results were:
    - Candidate "Charles Casper Stockham" received *23.0 %* of the vote and *85,213* number of votes.
    - Candidate "Diana DeGette" received *73.8 %* of the vote and *272,892* number of votes.
    - Candidate "Raymon Anthony Doane" received *3.1 %* of the vote and *11,606* number of votes.
 - The**winner** of the election was:
    - Candidate **"Diana DeGette"** who received **73.8 %** of the vote and **272,892** number of votes.
 
## Challenge overview/Challenge Summary 

**1- Overview of Election Audit**

- In this section, we will help to find out which county is the largest based off of votes. We previously learned how to read csv files in python and begin to run the data with our coding skills. 
- Breanking down our data: The data file has 3 columns, we had to search through the one that had all of the candidates and figure out how many votes each candidate recieved. Once we figure out the total votes and percentage of the total that they had we wrote the results to a text file with a winner. In this part  we are slightly doing something similar but different. This time we will search through the counties column to figure out the total votes and percentage of each county to find which county is the largest.

- After sharing the election audit the election commission asked to confirm each county turnout.

   - Get a complete list of the counties.
   - Calculate the total number of votes for each county.
   - Calculate the percentage of votes for eachcounty.
   - Determine the county with the largest turnout.

**2- Election-Audit Results** 

   2.1- Number of votes cast in this congressional election
   
   The total amount of votes that were cased in the congressional election was 369,711.
 
   2.2- The breakdown of the number of votes and the percentage of total votes for each county in the precinct.
   
   *County Votes:*

   - Jefferson county has 10.5% total percentage with a total votes of 38,855
   - Denver county has the 82.8% total percentage with a total votes of 306,055
   - Arapahoe county has 6.7% total percentage with a total votes of 24,801
    
   2.3- County with Largest Number of Votes:

   - Denver county has the largest number total of 306,055. In addition, Denver county has the total votes percentage of 82.8%. **Denver county is the Largest County Turnout.**
   
     2.4- Breakdown of the number of votes and the percentage of the total votes each candidate received.
     
   - Charles Casper Stockham candidate has 23.0% total percentage with a total votes of 85,213.
   - Diana DeGette candidate has the 73.8 total percentage with a total votes of 272,892.
   - Raymon Anthony Doane candidate has 3.1% total percentage with a total votes of 11,606.

   - Denver received the most votes within this election, winning 82/8% of the total votes.
   - Jefferson won 10.5% of the total votes, whereas Arapahoe only won 6.7% of the total votes.
   
     2.5- Tha candidate that won the election 
   
   As for the candidates, **Diana DeGette** received the most votes, which was *73.8%* of all votes or *272,892* votes. The second place candidate, Charles Casper Stockham, received 23% of the total votes. Finally, the third candidate, Raymon Anthony Doane, only received 3.1% of the overall votes.
