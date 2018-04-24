#include <iostream>
using namespace std;

int main(){

cout << endl << endl;
cout << "\033[7;36mInstructions:\033[0m";
cout << "\n\t Type \033[1;36mls\033[0m to list all the file available.";
cout << "\n\t Use \033[1;36mNANO\033[0m or \033[1;36mVIM\033[0m to edit file.";
cout << "\n\t Eg. \'\033[1;36mnano main.cpp\033[0m\' (without quotes).";
cout << "\n\t\t\033[1;36mctrl + x\033[0m to write changes made in the file.\n\t\tPress \033[1;36my\033[0m to save the file.";
cout << "\n\t Compile it manually: \'\033[1;36mg++ main.cpp -o myprog\033[0m\'.";
cout << "\n\t Execute: \'\033[1;36m./myprog\033[0m\'.\n\n";
cout << "\n\033[1;32m>> \033[0mCode from the textarea is saved in \033[1m\033[4;34mmain.cpp\033[0m\033[0m and compiled to \033[1m\033[4;34mmyprog\033[0m\033[0m";
cout << "\n\033[1;32m>> \033[0mEdit the code in  terminal \033[1m\033[4;34mnano main.cpp\033[0m\033[0m";
cout << "\n\033[1;32m>> \033[0mRun the compiled program: \033[1m\033[4;34m./myprog\033[0m\033[0m\n\n\n";

cout << "\033[1;37mEnjoy!\n";
cout << "-Abhishek\033[0m\n\n";

return 0;
}