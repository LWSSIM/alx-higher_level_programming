#include <Python.h>
#include <stdio.h>

/**
 * print_python_list_info - prints basics info about Python lists
 * @p: ptr->Python_lists
 */
void print_python_list_info(PyObject *p)
{
	int size, allocated, i;
	PyObject *item;

	size = PyList_Size(p);
	allocated = ((PyListObject *)p)->allocated;

	printf("[*] Size of the Python List = %d\n", size);
	printf("[*] Allocated = %d\n", allocated);

	for (i = 0; i < size; i++)
	{
		item = PyList_GetItem(p, i);
		printf("Element %d: %s\n", i, Py_TYPE(item)->tp_name);
	}
}
