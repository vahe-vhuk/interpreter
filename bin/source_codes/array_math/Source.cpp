#include <iostream>

template <typename T>
void entrywise_sum(T* res, T* arr_1, T* arr_2, int m1, int n1, int m2, int n2) {
	int m = (m1 < m2) ? m1 : m2;
	int n = (n1 < n2) ? n1 : n2; 
	int ind = 0;
	for (int i = 0; i < m*n1; i+=n1){
		for (int j = 0; j < n; j++){
			res[ind++] = arr_1[i + j] + arr_2[(int)(i / n1) * n2 + j];
		}
	}

}

template <typename T>
void direct_sum(T* res, T* arr_1, T* arr_2, int m1, int n1, int m2, int n2) {
	int m = m1 + m2;
	int n = n1 + n2;
	int ind1 = 0;
	int ind2 = 0;
	for (int i = 0; i < m*n; i += n) {
		for (int j = 0; j < n; j++){
			if ((int)(i / n) < m1 && j < n1)
				res[i + j] = arr_1[ind1++];
			else if (!((int)(i / n) < m1 || j < n1))
				res[i + j] = arr_2[ind2++];
			else
				res[i + j] = 0;
		}
	}
}

template <typename T>
void right_sum(T* res, T* arr_1, T* arr_2, int m1, int n1, int m2, int n2) {
	int m = (m1 < m2) ? m1 : m2;
	int n = n1 + n2;
	int ind1 = 0;
	int ind2 = 0;
	for (int i = 0; i < m*n; i+=n){
		for (int j = 0; j < n; j++){
			if (j < n1)
				res[i + j] = arr_1[ind1++];
			else
				res[i + j] = arr_2[ind2++];
		}
	}
}

template <typename T>
void bottom_sum(T* res, T* arr_1, T* arr_2, int m1, int n1, int m2, int n2) {
	int m = m1 + m2;
	int n = (n1 < n2) ? n1 : n2;
	int ind1 = 0;
	int ind2 = 0;
	for (int i = 0; i < m * n; i += n) {
		for (int j = 0; j < n; j++) {
			if ((int)(i/n) < m1)
				res[i + j] = arr_1[ind1++];
			else
				res[i + j] = arr_2[ind2++];
		}
	}
}

template <typename T>
void multiple(T* res, T* arr_1, T* arr_2, int m1, int n1, int m2, int n2) {
	int m = m1;
	int n = (n1 < m2) ? n1 : m2;
	

	int ind = 0;
	for (int i = 0; i < m1; i++){
		for (int j = 0; j < n2; j++){
			res[ind] = 0;
			for (int l = 0; l < n; l++){
				res[ind] += arr_1[i * n1 + l] * arr_2[l * n2 + j];
			}
			ind++;
		}

	}

}

template <typename T>
void entrywise_mul(T* res, T* arr_1, T* arr_2, int m1, int n1, int m2, int n2) {
	int m = (m1 < m2) ? m1 : m2;
	int n = (n1 < n2) ? n1 : n2;
	int ind = 0;
	for (int i = 0; i < m * n1; i += n1) {
		for (int j = 0; j < n; j++) {
			res[ind++] = arr_1[i + j] * arr_2[(int)(i / n1) * n2 + j];
		}
	}

}

extern "C"  __declspec(dllexport)
void entrywise_int_sum(int* res, int* arr_1, int* arr_2, int m1, int n1, int m2, int n2) {
	entrywise_sum(res, arr_1, arr_2, m1, n1, m2, n2);
}

extern "C" __declspec(dllexport)
void entrywise_float_sum(double* res, double* arr_1, double* arr_2, int m1, int n1, int m2, int n2) {
	entrywise_sum(res, arr_1, arr_2, m1, n1, m2, n2);
}


extern "C" __declspec(dllexport)
void direct_int_sum(int* res, int* arr_1, int* arr_2, int m1, int n1, int m2, int n2) {
	direct_sum(res,arr_1,arr_2,m1,n1,m2,n2);
}

extern "C" __declspec(dllexport)
void direct_float_sum(double* res, double* arr_1, double* arr_2, int m1, int n1, int m2, int n2) {
	direct_sum(res, arr_1, arr_2, m1, n1, m2, n2);
}

extern "C" __declspec(dllexport)
void right_int_sum(int* res, int* arr_1, int* arr_2, int m1, int n1, int m2, int n2) {
    right_sum(res, arr_1, arr_2, m1, n1, m2, n2);
}

extern "C" __declspec(dllexport)
void right_float_sum(double* res, double* arr_1, double* arr_2, int m1, int n1, int m2, int n2) {
   right_sum(res, arr_1, arr_2, m1, n1, m2, n2);
}

extern "C" __declspec(dllexport)
void bottom_int_sum(int* res, int* arr_1, int* arr_2, int m1, int n1, int m2, int n2) {
    bottom_sum(res, arr_1, arr_2, m1, n1, m2, n2);
}

extern "C" __declspec(dllexport)
void bottom_float_sum(double* res, double* arr_1, double* arr_2, int m1, int n1, int m2, int n2) {
    bottom_sum(res, arr_1, arr_2, m1, n1, m2, n2);
}

extern "C" __declspec(dllexport)
void float_mul(double* res, double* arr_1, double* arr_2, int m1, int n1, int m2, int n2) {
	multiple(res, arr_1, arr_2, m1, n1, m2, n2);
}

extern "C" __declspec(dllexport)
void int_mul(int* res, int* arr_1, int* arr_2, int m1, int n1, int m2, int n2) {
	multiple(res, arr_1, arr_2, m1, n1, m2, n2);
}

extern "C"  __declspec(dllexport)
void entrywise_int_mul(int* res, int* arr_1, int* arr_2, int m1, int n1, int m2, int n2) {
	entrywise_mul(res, arr_1, arr_2, m1, n1, m2, n2);
}

extern "C" __declspec(dllexport)
void entrywise_float_mul(double* res, double* arr_1, double* arr_2, int m1, int n1, int m2, int n2) {
	entrywise_mul(res, arr_1, arr_2, m1, n1, m2, n2);
}



