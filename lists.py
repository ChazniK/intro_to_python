# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    lists.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ckatz <marvin@42.fr>                       +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2017/11/02 13:49:52 by ckatz             #+#    #+#              #
#    Updated: 2017/11/03 11:08:03 by ckatz            ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

# [] brackets indicates a list - (array)
# [-1] - last item in list

'''
bicycles = ['trek', 'cannondale', 'redline', 'specialized'];
print(bicycles[1]);
print(bicycles[3]);
print(bicycles[-1]);
'''

#modifying elements in a list
'''
motorcycles = ['honda', 'yamaha', 'suzuki'];
print(motorcycles);

motorcycles[0] = "ducati";
print(motorcycles);
'''
#adding elements to a list - append()
'''
motorcycles = ['honda', 'yamaha', 'suzuki'];
print(motorcycles);
motorcycles.append("ducati");
print(motorcycles);

motorcycles = []
motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')
print(motorcycles)
'''

#Inserting elements into a list - insert()
'''
motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycles.insert(0, "ducati");
print(motorcycles);
'''
#Removing elements from a list - del(), pop() allows removed val used later
# remove() removes the first instance of the specified value
'''
motorcycles = ['honda', 'yamaha', 'suzuki'];
print(motorcycles);
del motorcycles[1];
print(motorcycles);
'''
'''
motorcycles = ['honda', 'yamaha', 'suzuki'];
print(motorcycles);
last_owned = motorcycles.pop();
print("The last motorcycle I owned was a " + last_owned.title() + ".");
'''
'''
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati'];
print(motorcycles);
motorcycles.remove("ducati");
print(motorcycles);
'''

#Organising a list - sort() to sort a list, reverse as parameter
#sorted() is to temporarily sort the list
# len() used to get the lenght of a list
'''
cars = ['bmw', 'audi', 'toyota', 'subaru'];
cars.sort();
print(cars);
cars.sort(reverse=True);
print(cars);
'''
'''
cars = ['bmw', 'audi', 'toyota', 'subaru'];
print(cars);
print("Here is the sorted list: ");
print(sorted(cars));
print (cars);
'''
'''
cars = ['bmw', 'audi', 'toyota', 'subaru'];
print(len(cars));
'''

#looping through a list
'''
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
	print(magician.title() + ", that was a great trick!");
	print("I can't wait to see your next trick, " + magician.title() + ".\n");
cars = ['bmw', 'audi', 'toyota', 'subaru'];
print("Thank you, everyone. That was a great magic show");
'''

#numerical lists - range(start, end)
'''
for value in range(1, 5):
	print(value);

numbers = list(range(1, 6));
print(numbers);

even_numbers = list(range(2, 11, 2));
print(even_numbers);

squares = [];
for value in range(1, 11):
	square = value **2;
	squares.append(square);
print(squares);
'''

#min and max values in a list
'''
digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0];
print(min(digits));
print(max(digits));
print(sum(digits));
'''

#list comprehension - combines for loop and creation of new elements 1 line
'''
squares = [value **2 for value in range(1, 11)]
print(squares);
'''
#slicing a list
'''
players = ['charles', 'martina', 'michael', 'florence', 'eli'];
print(players[0:3]);

print("Here are the first three players on my team:")
players = ['charles', 'martina', 'michael', 'florence', 'eli'];
for player in players[:3]:
	print(player.title());
'''
#copying a list
'''
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:];

print("My favorite foods are:");
print(my_foods);

print("\nMy friend's favorite foods are:");
print(friend_foods);

my_foods.append("cannoli");
friend_foods.append("ice cream");

print(my_foods);
print(friend_foods);
'''

#Tuples - used to store an immutable list

dimensions = (200, 50, 40, 60);
print(dimensions[0]);
print(dimensions[2]);



















































