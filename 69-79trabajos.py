country_tuple = ("France", "England", "Spain", "Germany", "Australia")
#trabajo 69
print (country_tuple)
print ()
country = input ("Please
enter one of the countries from above: ")
print (country,
"has index number", country_tuple. index (country) )

#trabajo 70
country tuple = ("France", "England", "Spain", "Germany", "Australia")
print (country tuple)
print ()
country = input ("Please enter one of the countries from above: ")
print (country, print ()
"has index number", country_tuple.index (country))
num = int (input ("Enter a number betwen 0 and 4: "))
print (country_ tuple [num])


#trabajo 71
sports_list - ["tennis", "football"] sports list.append (input ("What is your favourite sport? ")) sports list.sort () print (sports list)


#trabajo 72

subject_ list - ["maths", "english", "computing", "history", "science", "spanish"] print (subject list)
dislike = input ("Which of these subjects do you dislike?
getrid = subject list.index (dislike)
del subject list [getrid]
print (subject list)


#trabajo 73
food dictionary = {]
foodI = input ("Enter a food you like: ")
food dictionary [1] = food
food2 = input ("Enter another food you like: ")
food dictionary [2] = food2
food3 = input ("Enter a third food you like: ")
food dictionary [3] = food3
food = input ("Enter one last food you like: ")
food dictionary [4] = food4
print (food dictionary)
dislike = int (input ("Which of these do you want to get rid of? "))
del food dictionary [dislike]
print (sorted (food dictionary.values () ))


#trabajo 74
colours = ["red", "blue", "green", "black", "white",
, "pink", "grey", "purple", "yellow", "brown"]
start = int (input ("Enter a starting number (0-4) : "))
end = int (input ("Enter an end number (5-9)
print (colours [start:end])

#trabajo 75
nums
= [123, 345,234, 765]
for i in nums:
print (i)
selection = int (input ("Enter a number from the list: "))
if selection in nums:
print (selection, "is in position", nums. index (selection)) else:
print ("That is not in the list")

#trabajo 76
namel = input ("Enter a name of somebody you want to invite to your party: ")
name2 = input ("Enter another name:
name3 = input ("Enter a third name:
party = [namel, name2, name3]
another = input ("Do you want to invite another (y/n): ")
while another == "y":
newname = party. append (input ("Enter another name: "))
another = input ("Do you want to invite another (y/n):
")
print ("You have", len (party), "people coming to your party")

#trabajo 77
namel = input ("Enter a name of somebody you want to invite to your party: ")
name 2 input ("Enter another name:
'* )
name3 = input ("Enter a third name:
party
=
[name 1, name2, name3]
another = input ("Do you want to invite another (y/n) : ")
while another == "y":
newname = party. append (input ("Enter anothername:)
another = input ("Do you want to invite another (y/n): ")
print ("You have", len (party),
"people coming to your party")
print (party)
selection - input ("Enter one of the names: print (selection, "is in position" stillcome
party. index (selection), "on the list")
= input ("Do you still want them to come (y/n) :
'*)
11 stillcome ==
"n":
party. remove (selection)
print (party)

#trabajo 78
tv = ["Task Master", "Top Gear", "The Big Bang Theory", "How I Met Your Mother"]
for i in tv:
print (1)
print ()
newtv = input ("Enter another TV show:
' )
position = int (input ("Enter a number between 0 and 3: "))
tv.insert (position, newtv) for i in tv:
print (1)


#trabajo 79
nums
=
[ ]
count = 0
while count <3:
num = int (input ("Enter a number:
7) )
nums. append (num)
print (nums)
count = count + 1
lastnum = input ("Do you want the last number saved (y/n) : ")
if lastnum ==
"n":
nums. remove (num)
print (nums)