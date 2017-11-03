# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    conditionals.py                                    :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ckatz <marvin@42.fr>                       +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2017/11/03 11:08:21 by ckatz             #+#    #+#              #
#    Updated: 2017/11/03 12:25:06 by ckatz            ###   ########.fr        #
#                                                                              #
# **************************************************************************** #
'''
cars = ['audi', 'bmw', 'subaru', 'toyota'];

for car in cars:
	if (car == "bmw"):
		print(car.upper());
	else:
		print(car.title());

answer = 17;

if (answer != 42):
	print("That is not the correct answer. Please try again!");
'''

#checking if a value is in a list
'''
requested_toppings = ['mushrooms', 'onions', 'pineapple'];

if ("mushrooms" in requested_toppings):
	print("Yes");
else:
	print("No");

#checking if value absent from list

banned_users = ['andrew', 'carolina', 'david'];
user = "marie";

if (user not in banned_users):
	print(user.title() + ", you can post a response if you wish.");
'''
#using multiple elif blocks
'''
age = 12

if (age < 4):
	price = 0;
elif (age < 18):
	price = 5;
elif (age < 65):
	price = 10;
else:
	price = 5;
print("Your admission cost is $" + str(price) + ".");
'''
'''
requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']

for requested_topping in requested_toppings:
	if requested_topping == "mushrooms":
		print("There are no " + requested_topping + " left.");
	else:
		print("Adding " + requested_topping + ".");

print("\nFinished making your pizza!");
'''

#checking for an empty list
'''
requested_toppings = [];

if requested_toppings:
	for requested_topping in requested_toppings:
		print("Adding " + requested_topping + ".")
	print("\nFinished making your pizza!")
else:
	print("Are you sure you want a plain pizza?");
'''

num_list = range(1, 10);

for num in num_list:
	if num == 1:
		print(str(num) + "st");
	elif num == 2:
		print(str(num) + "nd");
	elif num == 3:
		print(str(num) + "rd");
	else:
		print(str(num) + "th");
