#include <Python.h>
#include <stdlib.h>
#include <string.h>

static PyObject *wrap_getenv(PyObject *self, PyObject *args)
{
    char *varName, *varValue;
    PyObject *returnObj = NULL;

    if (PyArg_Parse(args, "(s)", &varName)) {
        varValue = getenv(varName);
        if (varValue != NULL)
            returnObj = Py_BuildValue("s", varValue);
        else
            PyErr_SetString(PyExc_SystemError, "Error calling getenv");
    }
    return returnObj;
}

static PyObject * wrap_putenv(PyObject *self, PyObject *args)
{
    char *varName, *varValue, *varAssign;
    PyObject *returnObj = NULL;

    if (PyArg_Parse(args, "(ss)", &varName, &varValue))
    {
        varAssign = malloc(strlen(varName) + strlen(varValue) + 2);
        sprintf(varAssign, "%s=%s", varName, varValue);
        if (putenv(varAssign) == 0) {
            Py_INCREF(Py_None);
            returnObj = Py_None;
        }
        else
            PyErr_SetString(PyExc_SystemError, "Error calling putenv");
    }
    return returnObj;
}

static PyMethodDef cenviron_methods[] = {
    {"getenv",  wrap_getenv, METH_VARARGS, "getenv doc"},
    {"putenv",  wrap_putenv, METH_VARARGS, "putenv doc"},
    {NULL, NULL, 0, NULL}
};


static struct PyModuleDef cenvironmodule = {
   PyModuleDef_HEAD_INIT,
   "cenviron",
   "cenviron doc",
   -1,
   cenviron_methods
};


PyMODINIT_FUNC
PyInit_cenviron()
{
    return PyModule_Create(&cenvironmodule);
}