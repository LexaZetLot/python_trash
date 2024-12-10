#include <Python.h>
#include <stdio.h>
#define error(msg) do { printf("%s\n", msg); exit(1); } while (1)

main() {
  char *arg1="sir", *arg2="robin", *cstr;
  PyObject *pmod, *pclass, *pargs, *pinst, *pmeth, *pres;

  Py_Initialize();
  pmod = PyImport_ImportModule("module");
  if (pmod == NULL)
      error("Can't load module");

  pclass = PyObject_GetAttrString(pmod, "klass");
  Py_DECREF(pmod);
  if (pclass == NULL)
      error("Can't get module.klass");

  pargs = Py_BuildValue("()");
  if (pargs == NULL) {
      Py_DECREF(pclass);
      error("Can't build arguments list");
  }
  pinst = PyEval_CallObject(pclass, pargs);
  Py_DECREF(pclass);
  Py_DECREF(pargs);
  if (pinst == NULL)
      error("Error calling module.klass()");

  pmeth  = PyObject_GetAttrString(pinst, "method");
  Py_DECREF(pinst);
  if (pmeth == NULL)
      error("Can't fetch klass.method");

  pargs = Py_BuildValue("(ss)", arg1, arg2);
  if (pargs == NULL) {
      Py_DECREF(pmeth);
      error("Can't build arguments list");
  }
  pres = PyEval_CallObject(pmeth, pargs);
  Py_DECREF(pmeth);
  Py_DECREF(pargs);
  if (pres == NULL)
      error("Error calling klass.method");

  if (!PyArg_Parse(pres, "s", &cstr))
     error("Can't convert klass.method result");
  printf("%s\n", cstr);
  Py_DECREF(pres);
}