#!/usr/bin/python

import re, sys

repl_dict = {
    'build' : 'None',
    'host' : 'None',
    'prefix' : '/usr',
    'eprefix' : '/usr',
    'bindir' : '/usr/bin',
    'sbindir' : '/usr/sbin',
    'libexecdir' : '/usr/libexec',
    'libdir' : '/usr/lib',
    'sysconfdir' : '/usr/etc',
    'datadir' : '/usr/share',
    'localedir' : '/usr/share/locale',
    'includedir' : '/usr/include',
    'mandir' : '/usr/man',
    'infodir' : '/usr/info',
    'localstatedir' : '/usr/var',
    'project_name' : 'xtrlock-pam',
    'project_version' : '3.5',
    'x11_libs' : '-lX11',
    'x11_cflags' : '',
    'x11_version' : '1.8.1',

}

def repl_func(matchobj):
    key = matchobj.group(0)[1:-1]
    if key in repl_dict:
        return repl_dict[key]
    else:
        return matchobj.group(0)


print re.sub('@\w+@', repl_func, sys.stdin.read())

