##
## EPITECH PROJECT, 2018
## Makefile
## File description:
## make files
##

NAME	=	205IQ

SRC		=	IQ.py

all:
	cp $(SRC) $(NAME)
	chmod 755 $(NAME)

tests_run:
		python3 test_iq.py

clean:
	echo "Nothing to clean"

fclean:	clean
	rm $(NAME)	\
	rm -f *~	\
	rm -f *#	\
	rm -f *.pyc

re:	fclean clean all

.PHONY:	all re clean fclean
