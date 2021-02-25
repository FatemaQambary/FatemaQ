#include <iostream>
using namespace std;
//constructors:works like unload method
//we dont call the class
//
class abc{
	public:
		int a,b,c;
		abc(){
			a=10;
			b=20;
			c=a+b;
		}
		void display(){
			cout<<"result: "<<c;
		}
};
int main(){
	abc obj1;
	obj1.display();
}
