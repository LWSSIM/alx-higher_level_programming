#include <Python.h>
#include <stdio.h>

/**
* print_python_float - prints float info
* @p: ptr to list
*/
void print_python_float(PyObject *p)
{
	char *data;

	long double i;

	fflush(stdout);
	printf("[.] float object info\n");
	if (!PyFloat_CheckExact(p))
	{
		printf("  [ERROR] Invalid Float Object\n");
		return;
	}
	i = ((PyFloatObject *)p)->ob_fval;
	data = PyOS_double_to_string(i, 'r', 0, Py_DTSF_ADD_DOT_0, NULL);
	printf("  value: %s\n", data);
}
/**
* print_python_bytes - print byts info
* @p: ptr to list
*/
void print_python_bytes(PyObject *p)
{
	char *data;
	long int size, i;

	fflush(stdout);

	printf("[.] bytes object info\n");
	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}
	size = PyBytes_Size(p);
	data = (assert(PyBytes_Check(p)), (((PyBytesObject *)(p))->ob_sval));
	printf("  size: %ld\n", size);
	printf("  trying string: %s\n", data);
	if (size >= 10)
		printf("  first 10 bytes:");
	else
		printf("  first %ld bytes:", ++size);
	for (i = 0; i < size && i < 10; i++)
	{
		if (data[i] >= 0)
			printf(" %02x", data[i]);
		else
			printf(" %02x", 256 + data[i]);
	}
	printf("\n");
}

/**
* print_python_list - print list items
* @p: pointer to list
*/
void print_python_list(PyObject *p)
{
	PyObject *object;
	long int size = ((PyVarObject *)p)->ob_size, i;

	Py_ssize_t allocated = ((PyListObject *)p)->allocated;

	fflush(stdout);

	printf("[*] Python list info\n");
	if (!PyList_CheckExact(p))
	{
		printf("  [ERROR] Invalid List Object\n");
		return;
	}
	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", allocated);

	for (i = 0; i < size; i++)
	{
		object = ((PyListObject *)p)->ob_item[i];

		printf("Element %ld: %s\n", i, ((object)->ob_type)->tp_name);
		if (PyBytes_Check(object))
			print_python_bytes(object);
		if (PyFloat_Check(object))
			print_python_float(object);
	}
}
