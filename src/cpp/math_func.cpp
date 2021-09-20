using namespace std;

#include <cmath>
#include <stdio.h>
#include <fstream>
#include <iostream>
#include <vector>
#include <math.h>
#include <iomanip>

char const *d = "FINE";

int VectorBinarySearch(vector<pair<float, int>> d, int* high, int* low, int* mid, float val) {
	// printf("high = %d, mid = %d, low = %d, val = %f, %f\n", *high, *mid, *low, val, d[*mid].first);
	if (d[*mid].first == val) {
		return *mid;
	} else {
		if (d[*mid].first > val) {
			*high = *mid;
			*mid = round((*high + *low) / 2);
		} else {
			*low = *mid;
			*mid = round((*high + *low) / 2);
		}
		return VectorBinarySearch(d, high, low, mid, val);
	}
}

void printPairVectorF(vector<pair<float, float>> v) {
	for (pair<float, float> co_ord: v) {
		std::cout << " [" + to_string(co_ord.first) + ", " + to_string(co_ord.second) + "]"<< ',';
	}
	std::cout << "" << '\n';
}

void printPairVectorI(vector<pair<float, int>> v) {
	for (pair<float, int> co_ord: v) {
		std::cout << " [" + to_string(co_ord.first) + ", " + to_string(co_ord.second) + "]"<< ',';
	}
	std::cout << "" << '\n';
}

void printIntVector(vector<int> v) {
	for (int item: v) {
		std::cout << to_string(item) << ',';
	}
	std::cout << "" << '\n';
}

void printNFIPEquation(vector<float> c) {
	string eqn = to_string(c[0]) + " + ";

	for (size_t i = 1; i < c.size(); i++) {
		eqn += "(" + to_string(c[i]) + "x^" + to_string(i) + ")";
		eqn += (i == (c.size() - 1) ? "" : " + ");
	}

	std::cout << eqn << '\n';
}

vector<float> NFIP(vector<pair<float, float>> d, int degree) {
	// DEGREE CAN ONLY BE AN EVEN NUMBER DUE TO NATURE OF DATA (DISTRIBUTION IS AN EVEN FUNC)
	vector<float> coefficients;
	int start = 100 - degree;
	int range = degree * 2;

	vector<float> differences[range];
	for (int j = 0; j < range; j++) {
		vector<float> diff;
		for (int i = 0; i < (range - j); i++) {
			if (j == 0) {
				// printf("%f %f\n", d[start + i + 1].second, d[start + i].second);
				diff.push_back(d[start + i + 1].second - d[start + i].second);
			} else {
				diff.push_back(differences[j - 1][i + 1] - differences[j - 1][i]);
			}
		}
		differences[j] = diff;
	}



	// for (int i = 0; i < range; i++) {
	// 	printIntVector(differences[i]);
	// }

	coefficients.push_back(d[start].second);
	for (int i = 0; i < range; i++) {
		coefficients.push_back(differences[i][0]);
	}

	printNFIPEquation(coefficients);

	return coefficients;
}

int main(int argc, char *argv[]) {

	std::ifstream datafile("../data/tdata.csv");
	string line;

	if (datafile.is_open()) {
		getline(datafile, line);
	}

	string temp;
	int datacount = 1;
	vector<pair<float, int>> initial_data;
	float counter = 29.00;

	while (counter < 31.01) {
		float temp = (int)(counter * 100 + 0.5);
		counter = (float)(temp / 100);
		// printf("%f\n", counter);
		initial_data.push_back(
			make_pair(
				counter,
				0
			)
		);
		counter += 0.01;
	}

	for (size_t i = 0; i < line.length(); i++) {
		if (line[i] == ',') {
			// std::cout << temp << '\n';
			float val = std::stof(temp);
			int h = initial_data.size() - 1; int m = (initial_data.size() - 1) / 2; int l = 0;
			initial_data[VectorBinarySearch(initial_data, &h, &l, &m, val)].second++;
			datacount++;
			temp = "";
		} else {
			temp += line[i];
		}
	}

	vector<pair<float, float>> data;


	for (size_t i = 0; i < initial_data.size(); i++) {
		// std::cout << to_string((float) initial_data[i].second / datacount) << '\n';
		data.push_back(
			make_pair(
				initial_data[i].first,
				(float) initial_data[i].second / datacount
			)
		);
	}

	// printPairVectorI(initial_data);
	//
	// printPairVectorF(data);

	// std::cout << to_string(datacount) << '\n';

	NFIP(data, 4);

	datafile.close();

    return 0;
}
