#include <Python.h>

main() {
    int cval;
    PyObject *pdict, *pval;
    printf("embed-dict\n");
    Py_Initialize();

    pdict = PyDict_New();
    PyDict_SetItemString(pdict, "__builtins__", PyEval_GetBuiltins());

    PyDict_SetItemString(pdict, "Y", PyLong_FromLong(2));
    PyRun_String("X = 99",  Py_file_input, pdict, pdict);
    PyRun_String("X = X+Y", Py_file_input, pdict, pdict);
    pval = PyDict_GetItemString(pdict, "X");

    PyArg_Parse(pval, "i", &cval);
    printf("%d\n", cval);
    Py_DECREF(pdict);
    Py_Finalize();
}