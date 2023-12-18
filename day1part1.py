#include <iostream>
#include <fstream>
#include <string>
#include <vector>

int main(){
  std::string line;
  std::ifstream file("input.txt");
  int sum = 0;
  std::vector<int> vector;
  if (file.is_open()) {
        while (getline(file, line)) {
          for (char c : line){
            if (isdigit(c)){
              vector.push_back(c - '0');
            }
          }
          if (vector.size() == 1){
            sum += vector.at(0) + (vector.at(0) * 10);
          }
          else {
            sum += (vector.at(0) * 10) + vector.back();
          }
          vector.clear();
        }
        file.close();
    }
  std::cout << sum << std::endl;
  return 0;
}
