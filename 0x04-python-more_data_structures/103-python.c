#include "Python.h"
#include "stdio.h"

/**
 * print_python_bytes - print byts info
 * @p: ptr tp list
 */
void print_python_bytes(PyObject *p)
{
	Py_ssize_t size, i;
	char *data;

	printf("[.] bytes object info\n");
	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}
	PyBytes_AsStringAndSize(p, &data, &size);
	printf("  size: %ld\n", size);
	printf("  trying string: %s\n", data);
	printf("  first 6 bytes: ");
	for (i = 0; i < size && i < 6; i++)
	{
		printf("%02x ", data[i] & 0xFF);
	}
	printf("\n");
}

/**
 * print_python_list - print list items
 * @p: pointer to list
 */
void print_python_list(PyObject *p)
{
	PyListObject *list = (PyListObject *)p;
	PyObject *item;
	Py_ssize_t size = PyList_GET_SIZE(p), i;
	Py_ssize_t allocated = list->allocated;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", allocated);

	for (i = 0; i < size; i++)
	{
		item = list->ob_item[i];

		printf("Element %ld: %s\n", i, PyBytes_Check(item) ? "bytes" : "unknown");
		if (PyBytes_Check(item))
		{
			print_python_bytes(item);
		}
	}
}
