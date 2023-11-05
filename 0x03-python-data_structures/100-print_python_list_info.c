#include <Python.h>
#include <stdio.h>

/**
 * print_python_list_info - prints basics info about Python lists
 * @p: ptr->Python_lists
 */
void print_python_list_info(PyObject *p)
{
	Py_ssize_t i, list_size, num_allocated;
	PyObject *item, *item_str;
	char *str;

	if (PyList_Check(p))
	{
		list_size = PyList_Size(p);
		num_allocated = PyList_GET_SIZE(p);

		printf("[*] Size of the Python List = %zd\n", list_size);
		printf("[*] Allocated = %zd\n", num_allocated);

		for (i = 0; i < list_size; i++)
		{
			item = PyList_GetItem(p, i);
			printf("Element %zd: ", i);
			if (item)
			{
				item_str = PyObject_Str(item);
				if (item_str)
				{
					str = (char *)PyUnicode_AsUTF8(item_str);
					printf("%s\n", str);
					free(item_str);
					free(str);
				}
			}
		}
	}
}
