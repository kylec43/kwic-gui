from time import time
from time import sleep


class offset:
	def __init__(self, id, value):
		self.id = id
		self.value = value

def getOffsetShifts(line):


	offsets = []

	if len(line) != 0 and line[0] != ' ':
		offsets.append(0)


	for i in range(1, len(line), 1):

		if line[i] != ' ' and line[i-1] == ' ':
			offsets.append(i)
		

	return offsets







def getCircularShifts(line):

	lis = line.split()

	if len(lis) <= 1:
		return lis

	circularShifts = []
	i = 0
	while i < len(lis):
		word = lis[0]
		lis.pop(0)
		lis.append(word)
		shiftedLine = " ".join(lis)
		circularShifts.append(shiftedLine)
		i+=1

	return circularShifts





line = '''How old is Keith 
He How old is James 
He is a year older than Keith but he looks younger 
How your father 
He fine He retired last week It a turning point in his life Now he can relax and enjoy his retirement 
He can spend more time with his grandchildren 
Oh I dont think he wants to He wants to travel to several different countries around the world 
So he wants to have a more active retirement Good idea 
How do you want to spend your old age 
In the same way probably 
What the life expectancy in your country 
I am not sure but probably about years How about in your country 
About I think This newspaper article talks about the problems of an aging population It a problem that will soon affect most of the world 
I heard that the government might need to increase the retirement age because otherwise there will not be enough workers to support the young and the elderly 
Perhaps we need to have more babies Tina gave birth to a baby boy yesterday 
Did she That great However if we have too many children that will have a bad effect on the environment 
How your son these days 
Oh he fine Kids seem to grow up very quickly nowadays 
He be a teenager before you know it Teenagers are often rebellious When do you think it is a good age to have a child 
I had mine when I was That a little young I suggest you wait until you are in your late twenties or even in your early thirties if you have a good career 
Yes I think you are right Im thinking about having a child but not just yet 
Is there a big generation gap between parents and their children in your country 
A Yes there is Teenagers do not want to live traditional lives They want to go out have fun and explore the world They want to develop their own view of life Parents usually try to discourage them but they dont often succeed 
Parents usually give their children more freedom in my country Sometimes they give them too much freedom 
It almost impossible to get the right balance If you are too strict kids might ignore you If you are too lenient they might go wild 
Do you like Barry
No not very much He too ambitious and dishonest
I agree I like his brother Paul They are not alike
Yes They are completely different Paul is very sociable and much more honest than his brother
What kind of person do you consider yourself to be
I think I am polite careful relaxed and shy
Oh I dont think you are shy You are always chatting with new people when we go to a party
Well yes but those people always start talking to me I never talk to them first Perhaps Im not as shy as I think Anyway you are certainly not shy
You are right I love going out and making new friends
So you be at my birthday party on Friday
Of course
How do you think people get their personalities
I think it mainly from the environment a person lives in
Dont you think people get their personalities from their parents
No but parents control a lot of the environment that kids grow up in so they certainly influence their kid personalities a lot
So why do you think many kids have personalities that are so different from their parents
Maybe when they become teenagers they want to be completely different to their parents
You might be right I guess most parents want their kids to be like them but kids today grow up in a different environment You know they know much more about the world from the internet newspapers and TV
Do you think that teenagers get a lot of their bad behaviors from TV and movies
Maybe some of it I think a lot of people blame TV and movies when the real problem is that the parents arent bringing their child up correctly
Parents have a difficult job They have to bring up their children and usually have to work too
Yes that true Your son is doing well at school is not he
Yes he is He very hard working when he at school Then he comes home from school and does his homework before dinner After dinner he goes out with his friends
So he not a bookworm It good that he has an outgoing personality Some kids are very quiet and introverted You wonder how they survive in the real world without their parents to support them
How old is Keith 
He How old is James 
He is a year older than Keith but he looks younger 
How your father 
He fine He retired last week It a turning point in his life Now he can relax and enjoy his retirement 
He can spend more time with his grandchildren 
Oh I dont think he wants to He wants to travel to several different countries around the world 
So he wants to have a more active retirement Good idea 
How do you want to spend your old age 
In the same way probably 
What the life expectancy in your country 
I am not sure but probably about years How about in your country 
About I think This newspaper article talks about the problems of an aging population It a problem that will soon affect most of the world 
I heard that the government might need to increase the retirement age because otherwise there will not be enough workers to support the young and the elderly 
Perhaps we need to have more babies Tina gave birth to a baby boy yesterday 
Did she That great However if we have too many children that will have a bad effect on the environment 
How your son these days 
Oh he fine Kids seem to grow up very quickly nowadays 
He be a teenager before you know it Teenagers are often rebellious When do you think it is a good age to have a child 
I had mine when I was That a little young I suggest you wait until you are in your late twenties or even in your early thirties if you have a good career 
Yes I think you are right Im thinking about having a child but not just yet 
Is there a big generation gap between parents and their children in your country 
A Yes there is Teenagers do not want to live traditional lives They want to go out have fun and explore the world They want to develop their own view of life Parents usually try to discourage them but they dont often succeed 
Parents usually give their children more freedom in my country Sometimes they give them too much freedom 
It almost impossible to get the right balance If you are too strict kids might ignore you If you are too lenient they might go wild 
Do you like Barry
No not very much He too ambitious and dishonest
I agree I like his brother Paul They are not alike
Yes They are completely different Paul is very sociable and much more honest than his brother
What kind of person do you consider yourself to be
I think I am polite careful relaxed and shy
Oh I dont think you are shy You are always chatting with new people when we go to a party
Well yes but those people always start talking to me I never talk to them first Perhaps Im not as shy as I think Anyway you are certainly not shy
You are right I love going out and making new friends
So you be at my birthday party on Friday
Of course
How do you think people get their personalities
I think it mainly from the environment a person lives in
Dont you think people get their personalities from their parents
No but parents control a lot of the environment that kids grow up in so they certainly influence their kid personalities a lot
So why do you think many kids have personalities that are so different from their parents
Maybe when they become teenagers they want to be completely different to their parents
You might be right I guess most parents want their kids to be like them but kids today grow up in a different environment You know they know much more about the world from the internet newspapers and TV
Do you think that teenagers get a lot of their bad behaviors from TV and movies
Maybe some of it I think a lot of people blame TV and movies when the real problem is that the parents arent bringing their child up correctly
Parents have a difficult job They have to bring up their children and usually have to work too
Yes that true Your son is doing well at school is not he
Yes he is He very hard working when he at school Then he comes home from school and does his homework before dinner After dinner he goes out with his friends
So he not a bookworm It good that he has an outgoing personality Some kids are very quiet and introverted You wonder how they survive in the real world without their parents to support them
How old is Keith 
He How old is James 
He is a year older than Keith but he looks younger 
How your father 
He fine He retired last week It a turning point in his life Now he can relax and enjoy his retirement 
He can spend more time with his grandchildren 
Oh I dont think he wants to He wants to travel to several different countries around the world 
So he wants to have a more active retirement Good idea 
How do you want to spend your old age 
In the same way probably 
What the life expectancy in your country 
I am not sure but probably about years How about in your country 
About I think This newspaper article talks about the problems of an aging population It a problem that will soon affect most of the world 
I heard that the government might need to increase the retirement age because otherwise there will not be enough workers to support the young and the elderly 
Perhaps we need to have more babies Tina gave birth to a baby boy yesterday 
Did she That great However if we have too many children that will have a bad effect on the environment 
How your son these days 
Oh he fine Kids seem to grow up very quickly nowadays 
He be a teenager before you know it Teenagers are often rebellious When do you think it is a good age to have a child 
I had mine when I was That a little young I suggest you wait until you are in your late twenties or even in your early thirties if you have a good career 
Yes I think you are right Im thinking about having a child but not just yet 
Is there a big generation gap between parents and their children in your country 
A Yes there is Teenagers do not want to live traditional lives They want to go out have fun and explore the world They want to develop their own view of life Parents usually try to discourage them but they dont often succeed 
Parents usually give their children more freedom in my country Sometimes they give them too much freedom 
It almost impossible to get the right balance If you are too strict kids might ignore you If you are too lenient they might go wild 
Do you like Barry
No not very much He too ambitious and dishonest
I agree I like his brother Paul They are not alike
Yes They are completely different Paul is very sociable and much more honest than his brother
What kind of person do you consider yourself to be
I think I am polite careful relaxed and shy
Oh I dont think you are shy You are always chatting with new people when we go to a party
Well yes but those people always start talking to me I never talk to them first Perhaps Im not as shy as I think Anyway you are certainly not shy
You are right I love going out and making new friends
So you be at my birthday party on Friday
Of course
How do you think people get their personalities
I think it mainly from the environment a person lives in
Dont you think people get their personalities from their parents
No but parents control a lot of the environment that kids grow up in so they certainly influence their kid personalities a lot
So why do you think many kids have personalities that are so different from their parents
Maybe when they become teenagers they want to be completely different to their parents
You might be right I guess most parents want their kids to be like them but kids today grow up in a different environment You know they know much more about the world from the internet newspapers and TV
Do you think that teenagers get a lot of their bad behaviors from TV and movies
Maybe some of it I think a lot of people blame TV and movies when the real problem is that the parents arent bringing their child up correctly
Parents have a difficult job They have to bring up their children and usually have to work too
Yes that true Your son is doing well at school is not he
Yes he is He very hard working when he at school Then he comes home from school and does his homework before dinner After dinner he goes out with his friends
So he not a bookworm It good that he has an outgoing personality Some kids are very quiet and introverted You wonder how they survive in the real world without their parents to support them'''

lis = line.split('\n')

start = time()
for i in range(100):

	physical_shifted_lines = []
	for i in range(len(lis)):
		physical_shifted_lines.append(getCircularShifts(lis[i]))
finish = time()
total = finish - start
print('physical shift time: ', total)


start = time()
for i in range(100):

	offsets = []
	for i in range(len(lis)):
		offsets.append([i,getOffsetShifts(lis[i])])


finish = time()
total = finish - start
print('offset indices time:', total)


start = time()
for k in range(10000):
	for i in range(len(line)):
		w = line[i]
finish = time()
total = finish - start
print('string:',total)

lis = list(line)

start = time()
for k in range(10000):
	for i in range(len(lis)):
		w = line[i]

finish = time()
total = finish - start
print('list:',total)




