template <typename T>
void simple_array(T* arr, int m, int n, T val) {
	for (int i = 0; i < m * n; i++) {
		arr[i] = val;
	}
}

template <typename T>
void diagonal_array(T* arr, int m, int n, T val) {
	for (int i = 0; i < m * n; i += n) {
		arr[i+(i/n)] = val;
	}
}

template <typename T>
void top_diagonal_array(T* arr, int m, int n, T val) {
	for (int i = 0; i < m * n; i += n) {
		for (int j = (i / n) + 1; j < n; j++) {
			arr[i + j] = val;
		}
	}
}

template <typename T>
void top_and_diagonal_array(T* arr, int m, int n, T val) {
	for (int i = 0; i < m * n; i += n) {
		for (int j = (i / n); j < n; j++) {
			arr[i + j] = val;
		}
	}
}

template <typename T>
void bottom_diagonal_array(T* arr, int m, int n, T val) {
	for (int i = n; i < m * n; i += n) {
		for (int j = 0; j < (i / n); j++) {
			arr[i + j] = val;
		}
	}
}

template <typename T>
void bottom_and_diagonal_array(T* arr, int m, int n, T val) {
	for (int i = 0; i < m * n; i += n) {
		for (int j = 0; j < (i / n) + 1; j++) {
			arr[i + j] = val;
		}
	}
}

template <typename T>
void sec_diagonal_array(T* arr, int m, int n, T val) {
	for (int i = 0; i < m * n; i += n) {
		arr[i + n - 1 - (int)(i / n)] = val;
	}
}

template <typename T>
void top_sec_diagonal_array(T* arr, int m, int n, T val) {
	for (int i = 0; i < m * (n - 1); i += n) {
		for (int j = 0; j < n - 1 - (int)(i / n); j++) {
			arr[i + j] = val;
		}
	}
}

template <typename T>
void top_and_sec_diagonal_array(T* arr, int m, int n, T val) {
	for (int i = 0; i < m * n; i += n) {
		for (int j = 0; j < n - (int)(i / n); j++) {
			arr[i + j] = val;
		}
	}
}

template <typename T>
void bottom_sec_diagonal_array(T* arr, int m, int n, T val) {
	for (int i = n; i < m * n; i += n) {
		for (int j = n - (int)(i / n); j < n; j++) {
			arr[i + j] = val;
		}
	}
}

template <typename T>
void bottom_and_sec_diagonal_array(T* arr, int m, int n, T val) {
	for (int i = n; i < m * n; i += n) {
		for (int j = n - 1 - (int)(i / n); j < n; j++) {
			arr[i + j] = val;
		}
	}
}

template <typename T>
void maker(T* arr, int m, int n, T minval, T maxval, int varient) {
	for (int i = 0; i < m * n; i++) {
		arr[i] = 0;
	}
	if (minval == 0)
		return;


	switch (varient) {
	case 0:
		simple_array(arr, m, n, minval);
		break;
	case 1:
		diagonal_array(arr, m, n, minval);
		break;
	case 2:
		top_diagonal_array(arr, m, n, minval);
		break;
	case 3:
		top_and_diagonal_array(arr, m, n, minval);
		break;
	case 4:
		bottom_diagonal_array(arr, m, n, minval);
		break;
	case 5:
		bottom_and_diagonal_array(arr, m, n, minval);
		break;
	case 6:
		sec_diagonal_array(arr, m, n, minval);
		break;
	case 7:
		top_sec_diagonal_array(arr, m, n, minval);
		break;
	case 8:
		top_and_sec_diagonal_array(arr, m, n, minval);
		break;
	case 9:
		bottom_sec_diagonal_array(arr, m, n, minval);
		break;
	case 10:
		bottom_and_sec_diagonal_array(arr, m, n, minval);
		break;
	}
}


extern "C"  __declspec(dllexport)
void make_int_array(int* arr, int m=0, int n=0, int minval=0, int maxval=0, int varient=0) {
	maker(arr, m, n, minval, maxval, varient);
}

extern "C" __declspec(dllexport)
void make_double_array(double* arr, int m = 0, int n = 0, double minval = 0, double maxval = 0, int varient = 0) {
	maker(arr, m, n, minval, maxval, varient);
}

