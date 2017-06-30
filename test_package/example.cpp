#include <iostream>
#include <pqxx/pqxx>

int main() {
  try {
    pqxx::connection c;
    pqxx::work w(c);
  }
  catch (const std::exception& e)
  {
    std::cout << "Failed (which is ok): " << e.what() << std::endl;
  }
  return 0;
}
