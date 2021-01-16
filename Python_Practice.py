#PRINT HELLO WORLD
print("Hello World")
#list/slicing/logical connections
counties = ["Arapahoe","Denver","Jefferson"]
if counties[1] == 'Denver':
    print(counties[1])

counties = ["Arapahoe","Denver","Jefferson"]
if "El Paso" in counties:
    print("El Paso is in the list of counties.")
else:
    print("El Paso is not in the list of counties.")

if "Arapahoe" in counties and "El Paso" in counties:
    print("Arapahoe and El Paso are in the list of counties.")
else:
    print("Arapahoe or El Paso is not in the list of counties.")

if "Arapahoe" in counties or "El Paso" in counties:
    print("Arapahoe or El Paso is in the list of counties.")
else:
    print("Arapahoe and El Paso are not in the list of counties.")

for county in counties:
    print(county)
# is equivalent to...
for i in range(len(counties)):
    print(counties[i])

    #Iterate Through a Dictionary
counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}
#Retrieve only keys using a for loop
for county in counties_dict:
    print(county)
#Retrieve only keys using keys()
#This will print each key in order
for county in counties_dict.keys():
    print(county)


#Retrieve only values using values()
for voters in counties_dict.values():
    print(voters)
#Retrieve only values using dictionary_nane[key]
for county in counties_dict:
    print(counties_dict[county])
#Retrieve only values using get() 
for county in counties_dict:
    print(counties_dict.get(county))

#Retrieve key-value pairs using items()
for county, voters in counties_dict.items():
    print(county, voters)
for county, voters in counties_dict.items():
    print(county, "county has", str(voters), "registered voters.")


#Retrieve dictionaries from a list of dictionaries
voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
    {"county":"Denver", "registered_voters": 463353},
    {"county":"Jefferson", "registered_voters": 432438}]
for county_dict in voting_data:
    print(county_dict)
for i in range(len(voting_data)):
    print(voting_data[i])


#Retreive values from a list of dictionaries
for county_dict in voting_data:
    for value in county_dict.values():
        print(value)
#Retrieve only the number of registered voters from each dictionary
for county_dict in voting_data:
    print(county_dict['registered_voters'])
#Retrieve only the county name from each dictionary
for county_dict in voting_data:
    print(county_dict['county'])


#Printing Formats
#Concatenate strings with: + str()
#Original:
#   my_votes = int(input("How many votes did you get in the election?"))
#   total_votes = int(input("What is the total votes in the election?"))
#   percentage_votes = (my_votes / total_votes) * 100
#   print("I received " + str(percentage_votes)+ "% of the total votes")
#F-string Format: 
#   my_votes = int(input("How many votes did you get in the election?"))
#   total_votes = int(input("What is the total votes in the election?"))
#   print(f"I received {my_votes/total_votes * 100}% of the total votes")

#Refer to line 55
for county, voters in counties_dict.items():
    print(f"{county} county has {voters} registered voters.")

candidate_votes = int(input("How many votes did the candidate get in the election?"))
total_votes = int(input("What is the total votes in the election?"))
message_to_candidate = (
    f"You received {candidate_votes} number of votes. "
    f"The total number of votes in the election was {total_votes}. "
    f"You received {candidate_votes/total_votes*100}% of the total votes."
)
print(message_to_candidate)

#General number to format in an f-string:
#f'{value"{width}.{precision}}'
#   width = number of characters used to display the value
#   precision = number of decimal places to format the value
#Add a thousands separator with a comma: f'{value"{width},.{precision}}'

message_to_candidate = (
    f"You received {candidate_votes:,} number of votes. "
    f"The total number of votes in the election was {total_votes:,}. "
    f"You received {candidate_votes / total_votes * 100:.2f}% of the total votes."
)
print(message_to_candidate)

#Skill Drill
for county, voters in counties_dict.items():
    print(f"{county} county has {voters:,} registered voters.")