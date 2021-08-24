using namespace std;

#include <cmath>
#include <stdio.h>
#include <fstream>
#include <iostream>

char const *d = "FINE";

int main(int argc, char *argv[]) {

	std::ifstream datafile("../data/data.csv");
	// printf("%d %d %s\n", argc, sizeof(*argv), argv[0]);
	// datafile.open("data-practice\\data\\data.csv", ios::in);
	string line;
	// std::ifstream input("../data/data.csv");
	// if (!input) {
	// 	std::cout << "FILE LOAD FAILED" << '\n';
	// }
	if (datafile.is_open()) {
		getline(datafile, line);
	}

	string temp;
	int datacount = 1;
	float *data = (float *) calloc(datacount, sizeof(float));

	for (size_t i = 0; i < line.length(); i++) {
		if (line[i] == ',') {
			std::cout << temp << '\n';
			data[datacount - 1] = std::stof(temp);
			datacount++;
			data = (float *) realloc(data, datacount);
			temp = "";
		} else {
			temp += line[i];
		}
		printf("%d\n", i);
	}

	printf("%d %f\n", datacount, data[6]);

	// printf("%d\n", line.length());

	//
	// datafile.close();

    return 0;
}
