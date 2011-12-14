#include <iostream>
#include <cmath>
using namespace std;

class Analyzer{
    public:
	Analyzer(long);
	long return_n();
	long return_g_k();
    private:
	long n;
	long g_k;
	void calculate_g_k();
};

Analyzer::Analyzer(long n)
	 :n(n){
	g_k = 0;
	calculate_g_k();
}

long Analyzer::return_n(){
    return n;
}

long Analyzer::return_g_k(){
    return g_k;
}

void Analyzer::calculate_g_k(){
    long ten_to_the_power = 1L;
    int digits = 0;
    long likelyhood = 0L;
    double probability = 0.;
    double residual = 1.;
    int index;

    while( n > ten_to_the_power){
	ten_to_the_power *= 10L;
	digits++;
    }

    cout << digits << endl;
    likelyhood = (long)pow(10., (long)digits);
    cout << "lklyhd: " << likelyhood << endl;

    index = 0;
    while( probability < .5){
	probability += residual / (double)likelyhood;
	likelyhood -= probability;
	index++;
    }

    cout << "probability: " << probability << endl;
    cout << "index: " << index << endl;
}

int main(){
    Analyzer x(535L);
    
    cout << x.return_n() << " " << x.return_g_k() << endl;
}
