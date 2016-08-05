#include<iostream>

 class InefficientValueMaker {
 public:
 	int GetValue() const {
 		return 0;
 	}
 };
 class SomethingExtraordinary { 

 	public: SomethingExtraordinary() : mCacheValue(-1) {}
 	 int GetValue() {
 	 	printf("non const version\n");
 	 	if (mCacheValue == -1)
 	 		 mCacheValue = mValueMaker.GetValue();
 	 	 return mCacheValue; 
 	 } 

 	 int GetValue() const {
 	 	printf("const version\n");
 	 	 if (mCacheValue != -1)
 	 	 	 return mCacheValue;
 	 	 return mValueMaker.GetValue();
 	 }

	public:
 	 		InefficientValueMaker mValueMaker; int mCacheValue; 
 };

int main() {
	const SomethingExtraordinary s;
	
	printf("val is %d\n", s.GetValue());
	return 0;
}