#include <Python.h>

/**
 * print_python_string - prints a python strings in a pyobject
 * @p: pointer to python list object
 *
 * Return:
 *  void
 */
void print_python_string(PyObject *p)
{
    long int lenght;

    fflush(stdout);
    printf("[.] string object info\n");
    if (!PyUnicode_CheckExact(p))
    {
        printf("  [ERROR] Invalid String Object\n");
        return;
    }
    if (PyUnicode_IS_ASCII(p))
    {
        printf("  type: compact ascii\n");
    }
    else
    {
        printf("  type: compact unicode object\n");
    }

    lenght = PyUnicode_GET_LENGTH(p);
    
    printf("  length: %ld\n", lenght);
    printf("  value: %S\n", PyUnicode_AsWideCharString(p, NULL));
}
