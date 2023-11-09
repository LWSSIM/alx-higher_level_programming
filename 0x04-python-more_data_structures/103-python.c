#include <Python.h>
#include <stdio.h>

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
	if (size >= 10)
		printf("  first 10 bytes:");
	else
		printf("  first %ld bytes:", ++size);
	for (i = 0; i < size && i < 10; i++)
	{
		printf(" %02hhx", data[i]);
	}
	printf("\n");
}

/**
 * print_python_list - print list items
 * @p: pointer to list
 */
void print_python_list(PyObject *p)
{
	const char *item_type;
	Py_ssize_t size = ((PyVarObject *)p)->ob_size, i;
	Py_ssize_t allocated = ((PyListObject *)p)->allocated;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", allocated);

	for (i = 0; i < size; i++)
	{
		item_type = (((PyListObject *)p)->ob_item[i])->ob_type->tp_name;

		printf("Element %ld: %s\n", i, item_type);
		if (PyBytes_Check(item_type))
			print_python_bytes(((PyListObject *)p)->ob_item[i]);
	}
}
