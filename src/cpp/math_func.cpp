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

void printPairVector(vector<pair<float, int>> v) {
	for (pair<float, int> co_ord: v) {
		std::cout << " [" + to_string(co_ord.first) + ", " + to_string(co_ord.second) + "]"<< ',';
	}
}

vector<float> NFIP(vector<pair<float, int>> d, int degree) {
	vector<float> coefficients;

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
	vector<pair<float, int>> data;
	float counter = 29.00;

	while (counter < 31.01) {
		float temp = (int)(counter * 100 + 0.5);
		counter = (float)(temp / 100);
		// printf("%f\n", counter);
		data.push_back(
			make_pair(
				counter,
				0
			)
		);
		counter += 0.01;
	}

	for (size_t i = 0; i < line.length(); i++) {
		if (line[i] == ',') {
			std::cout << temp << '\n';
			float val = std::stof(temp);
			int h = data.size() - 1; int m = (data.size() - 1) / 2; int l = 0;
			data[VectorBinarySearch(data, &h, &l, &m, val)].second++;
			datacount++;
			temp = "";
		} else {
			temp += line[i];
		}
	}

	printPairVector(data);

	std::cout << to_string(datacount) << '\n';

	datafile.close();

    return 0;
}
