%module environ

extern char * getenv(const char *varname);
extern int    putenv(char *assignment);