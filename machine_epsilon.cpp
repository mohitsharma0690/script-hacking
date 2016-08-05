#include<iostream>
#include<cstdio>
using namespace std;

int main() {
    int a=100000;
    double eps = 1.0;
    int b = 1000000;
    while ((1.0 + 0.5 * eps) != 1.0) {
        eps = eps / 2.0;
    }
    printf("%.20f\n", eps);
    return 0;
}
