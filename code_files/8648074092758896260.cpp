
#include <iostream>
using namespace std;

int main(){
cout << "[1;31mForgot to type in some code,[0m [1;32m or was it intentional beta testing?[0m\n";
cout << "[1;36mHere's a hello world program for you![0m\n\n";
cout << "\t[1;33m#include <iostream>\n";
cout << "\tusing namespace std;\n\n";
cout << "\tint main() \n";
cout << "\t{\n";
cout << "\t    cout << 'Hello, World!'\n";
cout << "\t    return 0;\n";
cout << "\t}\n[0m";
cout << endl << endl;
cout << "[7;36mInstructions:[0m";
cout << "
	 Type [1;36mls[0m to list all the file available.";
cout << "
	 Use [1;36mNANO[0m or [1;36mVIM[0m to edit file.";
cout << "
	 Eg. '[1;36mnano main.cpp[0m' (without quotes).";
cout << "
		[1;36mctrl + x[0m to write changes made in the file.
		Press [1;36my[0m to save the file.";
cout << "
	 Compile it manually: '[1;36mg++ main.cpp -o myprog[0m'.";
cout << "
	 Execute: '[1;36m./myprog[0m'.

";
cout << "
[1;32m>> [0mCode from the textarea is saved in [1m[4;34mmain.cpp[0m[0m and compiled to [1m[4;34mmyprog[0m[0m";
cout << "
[1;32m>> [0mEdit the code in  terminal [1m[4;34mnano main.cpp[0m[0m";
cout << "
[1;32m>> [0mRun the compiled program: [1m[4;34m./myprog[0m[0m


";
cout << "[1;37mEnjoy!
";
cout << "-Abhishek[0m

";
return 0;
}