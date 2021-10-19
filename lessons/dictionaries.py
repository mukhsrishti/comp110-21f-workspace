"demonstrations of dictionary capabilities"

#declaring the type of a dictionary
schools: dict[str, int]

#initialize to an empty dictionary
schools = dict()

#set a key-value pairing in the dictionary
schools["UNC"] = 19_400
schools["Duke"] = 6_717
schools["NCSU"] = 26_150

#print a dictionary literal representation
print(schools)

#access a value by its key -- "lookup"

#remove a key-value pair from a dictionary
#by its key
schools.pop("Duke")

#test for the existence of a key
is_duke_present: bool = "Duke" in schools
print(f"Duke is present: {is_duke_present}")

#update/ Reassign a key-value pair
schools["UNC"] = 20000
schools["NCSU"] = schools["NCSU"] + 200


