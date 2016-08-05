#include<iostream>
using namespace std;

class Index {
    public:
        int value;
        Index(int v) {
            value = v;
        }
};
void inc_index(Index& i) {
    i.value++;
}

int main() {
    Index idx = Index(5);
    Index& idx_ref = idx;
    inc_index(idx_ref);
    cout << "Index is " << idx.value << endl;
    return 0;
}
