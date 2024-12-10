%module hellowrap

%{
#include <hellolib.h>
%}

extern char *message(char*);