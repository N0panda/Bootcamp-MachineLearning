# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    installer.sh                                       :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ythomas <marvin@42.fr>                     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2019/11/04 10:03:37 by ythomas           #+#    #+#              #
#    Updated: 2020/02/27 12:01:00 by ythomas          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

#!/bin/bash

PATH_INSTALLER="Miniconda3.sh"
FOLDER="~/tmp/Miniconda3/"

if [ $1 = "install" ]; then
	if [ ! -d $FOLDER ]; then
		echo "***   Creation du dossier   ***";
		sh $PATH_INSTALLER -p "$FOLDER";
		source ~/.zshrc
		echo "installation packages"
		pip install numpy matplotlib pandas sklearn

	else
		echo "already installed";
	fi
elif [ $1 = "remove" ]; then
	if [ -d $FOLDER ]; then
		rm -rf $FOLDER;
		echo "$FOLDER is now deleted";
		source ~/.zshrc
	else
		echo "Folder does not exist";
	fi
elif [ $1 = "pkg" ]; then
		echo "installation packages"
		pip install numpy matplotlib pandas sklearn
else
	echo "Unknow command";
fi
