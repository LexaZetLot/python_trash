#include <Python.h>
#include <stdio.h>

main() {
  char *arg1="sir", *arg2="robin", *cstr;
  PyObject *pmod, *pclass, *pargs, *pinst, *pmeth, *pres;

  Py_Initialize();
  pmod   = PyImport_ImportModule("module");
  pclass = PyObject_GetAttrString(pmod, "klass");
  Py_DECREF(pmod);

  pargs  = Py_BuildValue("()");
  pinst  = PyEval_CallObject(pclass, pargs);
  Py_DECREF(pclass);
  Py_DECREF(pargs);

  pmeth  = PyObject_GetAttrString(pinst, "method");
  Py_DECREF(pinst);
  pargs  = Py_BuildValue("(ss)", arg1, arg2);
  pres   = PyEval_CallObject(pmeth, pargs);
  Py_DECREF(pmeth);
  Py_DECREF(pargs);

  PyArg_Parse(pres, "s", &cstr);
  printf("%s\n", cstr);
  Py_DECREF(pres);
}