# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    dictionaries.py                                    :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ckatz <marvin@42.fr>                       +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2017/11/03 12:25:32 by ckatz             #+#    #+#              #
#    Updated: 2017/11/03 16:56:24 by ckatz            ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

#simple dictionary
'''
alien_0 = {'color': 'green', 'points': 5};

print(alien_0['color']);
print(alien_0['points']);
print("\n------------------------------------");
'''
#accessing the values in a dictionary
'''
alien_0 = {'color': 'green', 'points': 5};
print(alien_0['color']);

new_points = alien_0['points'];
print("You just earned " + str(new_points) + " points!");
'''
#adding new key value pairs

alien_0 = {'color': 'green', 'points': 5};
print(alien_0);

alien_0['x_position'] = 0;
alien_0['y_position'] = 25;
print(alien_0);

