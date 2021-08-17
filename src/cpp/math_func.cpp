using namespace std;

#include <cmath>
#include <stdio.h>
#include <fstream>
#include <iostream>

char const *d = "FINE";

int main(int argc, char *argv[]) {

	std::ifstream datafile("../data/data.csv");
	printf("%d %d %s\n", argc, sizeof(argv), argv[0]);
	// datafile.open("data-practice\\data\\data.csv", ios::in);
	string line;
	// std::ifstream input("../data/data.csv");
	// if (!input) {
	// 	std::cout << "FILE LOAD FAILED" << '\n';
	// }
	if (datafile.is_open()) {
		getline(datafile, line);
		// std::cout << line << '\n';
	}

	printf("%d\n", line.length());

	//
	// datafile.close();

    return 0;
}
