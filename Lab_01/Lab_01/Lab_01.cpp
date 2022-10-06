#include <iostream>
#include <locale>
#include <math.h>
#include "boost/multiprecision/cpp_int.hpp"
#include "boost/multiprecision/cpp_dec_float.hpp"

using std::cout;
using std::cin;
using std::endl;
using namespace boost::multiprecision;

int1024_t SochNoRep(int n, int m);//Сочетание без повторений
int1024_t RazWithRep(int n, int m);//Размещение с повторениями
int1024_t Permutations(int n);//Перестановки
int1024_t PerWithRep(int n, int N[], int k);//Перестановки с повторениями

void main()
{
	setlocale(LC_ALL, "RUS");//Добавление русских букв
	unsigned int n, m;
	int1024_t result;
	int choose;

	cout << "\t\t\tВыберите задание" <<
		endl << "1: Элементы комбинаторики" <<
		endl << "2: Классическое определение вероятности" << endl;
	cin >> choose;

	if (choose == 1)
	{
		cout << "Выберите комбинацию (Введите соответствующую цифру)." << endl
			<< "1: Сочитание без повторения" << endl
			<< "2: Размещение с повторениями" << endl
			<< "3: Перестановки" << endl;
		cin >> choose;

		//Задание 1
		switch (choose)
		{
		case 1://Ввод и обработка данных сочетания без повторений
		{
			cout << "Формула: n!/ (m!(n - m)!)" << endl;
			cout << "Введите число благоприятных исходов m (В диапазоне[0..165535]): ";
			cin >> m;
			cout << "Введите число всех исходов n (В диапазоне[0..165535]): ";
			cin >> n;
			result = SochNoRep(n, m);
			cout << "Результат: " << result << ".";
			break;
		}
		case 2://Ввод и обработка данных размещения с повторениями
		{
			cout << "Формула: n^m" << endl;
			cout << "Введите число благоприятных исходов m (В диапазоне[0..165535]): ";
			cin >> m;
			cout << "Введите число всех исходов n (В диапазоне[0..165535]): ";
			cin >> n;
			result = RazWithRep(n, m);
			cout << "Результат: " << result << ".";
			break;
		}
		case 3: //Ввод и обработка данных перестановки
		{
			cout << "Формула: n!" << endl;
			cout << "Введите число всех исходов n (В диапазоне[0..165535]): ";
			cin >> n;
			result = Permutations(n);
			cout << "Результат: " << result << ".";
			break;
		}
		default://Сообщение пользователю об ошибке в случае, когда он введет неверное число
		{
			cout << "Неверный выбор";
			break;
		}
		}
	}
	else if (choose == 2)
	{
		//Задание 2

		int choose;
		cout << "Выберите комбинацию (Введите соответствующую цифру)." << endl
			<< "1: Типовые задачки №2" << endl
			<< "2: Типовые задачки №4" << endl;
		cin >> choose;

		switch (choose)
		{
		case 1://Решение второй задачи и ее аналогов
		{
			cout << endl << "\t\t||||||||||||||||||||||||||||||"
				<< endl << endl << "\t\t  Решение по типу задачи №2"
				<< endl << endl << "\t\t||||||||||||||||||||||||||||||"
				<< endl << endl << "Формула: (m!*(m-n)!)/n!" << endl;
			cout << "Введите число благоприятных исходов m (В диапазоне[0..165535]): ";
			cin >> m;
			cout << "Введите число всех исходов n (В диапазоне[0..1,65535]): ";
			cin >> n;
			cout << "Находим вероятность числа особых исходов из всех" << endl;
			cout << "Ответ: " << 1 / (cpp_dec_float_100) SochNoRep(n, m) << ".";

			break;
		}
		case 2://Решение четвёртой задачи и ее аналогов
		{
			cout << endl << "\t\t||||||||||||||||||||||||||||||"
				<< endl << endl << "\t\t  Решение по типу задачи №4"
				<< endl << endl << "\t\t||||||||||||||||||||||||||||||"
				<< endl << endl << "Формула: n! / n^m * (n1! * n2! * ... * n(k)!)" << endl;
			cout << "Введите число благоприятных исходов m (В диапазоне[0..165535]): ";
			cin >> m;
			cout << "Введите число всех исходов n (В диапазоне[0..1,65535]): ";
			cin >> n;

			int k;
			cout << "Введите кол-во элементов k: ";
			cin >> k;
			int* N = new int[k];

			cout << "Введите значение элементов" << endl;
			cout << "Сумма элементов массива должна быть равна m" << endl;
			int sumN = 0;
			for (int i = 0; i < k; i++)//Ввод элементов n(k)
			{
				cout << "n" << i + 1 << " = ";
				cin >> N[i];
				sumN +=N[i];
			}

			if (m == sumN)//Проверка, чтобы m был равен сумме n элементов
			{
				cout << "Находим вероятность числа особых исходов из всех" << endl;
				cout << "Ответ: " << (cpp_dec_float_100) PerWithRep(m, N, k) / (cpp_dec_float_100) RazWithRep(n, m) << ".";
			}
			else
			{
				cout << "Неверный набор данных";
			}
			
			break;
		}
		default:
		{
			cout << "Неверный выбор";
			break;
		}
		}
	}
	else
	{
		cout << "Неверный выбор";
	}
}

int1024_t SochNoRep(int n, int m)//Функция расчета сочетания без повторений
{
	cpp_dec_float_100 result = 1;

	for (int i = n - (n - m) + 1; i < n + 1; i++)
	{
		result *= i;
	}
	
	for (int i = 2; i < n - m + 1; i++)
	{
		result /= i;
	}

	return (cpp_integer_type) result;
}

int1024_t RazWithRep(int n, int m)//Функция расчета размещения с повторениями
{
	int1024_t result = n;

	for (int i = 0; i < m - 1; i++)
	{
		result *= n;
	}

	return result;
}

int1024_t Permutations(int n)//Функция расчета перестановок
{
	int1024_t result = 1;

	for (int i = n; i > 1; i--)
	{
		result *= i;
	}

	return result;
}

//перестановка с повторениями / размещение с повторениями

int1024_t PerWithRep(int m, int N[], int k)//перестановка с повторениями
{
	cpp_dec_float_100 result = (cpp_dec_float_100) Permutations(m);
	int1024_t ZN = 1;
	
	for (int i = 0; i < k; i++)
	{
		ZN *= Permutations(N[i]);
	}

	result /= (cpp_dec_float_100) ZN;

	return (cpp_integer_type) result;
}