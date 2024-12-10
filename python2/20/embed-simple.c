#include <Python.h>

main() {
    printf("embed-simple\n");
    Py_Initialize();
    PyRun_SimpleString("import usermod");
    PyRun_SimpleString("print(usermod.message)");
    PyRun_SimpleString("x = usermod.message");
    PyRun_SimpleString("print(usermod.transform(x))");
    Py_Finalize();
}