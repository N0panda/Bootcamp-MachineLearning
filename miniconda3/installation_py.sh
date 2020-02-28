# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    installation_py.sh                                 :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ythomas <marvin@42.fr>                     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/02/07 15:48:52 by ythomas           #+#    #+#              #
#    Updated: 2020/02/07 16:16:35 by ythomas          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

#!/bin/bash

PATH_INSTALLER="Miniconda3.sh"
FOLDER="/tmp/Miniconda3"

if [ $1 = "remove" ]; then
	if [ -d $FOLDER ]; then
		rm -rf $FOLDER;
		echo "$FOLDER is now deleted";
	else
		echo "Folder does not exist";
	fi
elif [ ! $1 ]; then
	if [ ! -d $FOLDER ]; then
		echo "Installation de Python";
		export PATH=$FOLDERi:$PATH;
		sh $PATH_INSTALLER -p "$FOLDER";
		source ~/.zshrc
	else
		echo "already installed";
	fi
else
	echo "bad command";
fi
