package:
	gcc -I./ src/auth_pam.c src/xtrlock.c -o xtrlock-pam -lpam -lX11
	dpkg-buildpackage -us -uc
