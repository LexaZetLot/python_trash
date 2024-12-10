#include <Python.h>
#include <stdlib.h>

static PyObject *Handler = NULL;

void Route_Event(char *label, int count)
{
    char *cres;
    PyObject *args, *pres;

    args = Py_BuildValue("(si)", label, count);
    pres = PyEval_CallObject(Handler, args);
    Py_DECREF(args);

    if (pres != NULL) {
        PyArg_Parse(pres, "s", &cres);
        printf("%s\n", cres);
        Py_DECREF(pres);
    }
}


static PyObject *
Register_Handler(PyObject *self, PyObject *args)
{
    Py_XDECREF(Handler);
    PyArg_Parse(args, "(O)", &Handler);
    Py_XINCREF(Handler);
    Py_INCREF(Py_None);
    return Py_None;
}

static PyObject *
Trigger_Event(PyObject *self, PyObject *args)
{
    static count = 0;
    Route_Event("spam", count++);
    Py_INCREF(Py_None);
    return Py_None;
}

static PyMethodDef cregister_methods[] = {
    {"setHandler",    Register_Handler, METH_VARARGS, ""},
    {"triggerEvent",  Trigger_Event,    METH_VARARGS, ""},
    {NULL, NULL, 0, NULL}
};

static struct PyModuleDef cregistermodule = {
   PyModuleDef_HEAD_INIT,
   "cregister",
   "cregister mod",
   -1,
   cregister_methods
};

PyMODINIT_FUNC
PyInit_cregister()
{
    return PyModule_Create(&cregistermodule);
}