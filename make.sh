#!/bin/sh
gcc -I./ src/auth_pam.c src/xtrlock.c -o xtrlock-pam -lpam -lX11
