#include <string>
#include <vector>

class SumOfDivided
{
public:
    static std::string sumOfDivided(std::vector<int> &lst);
};

std::string SumOfDivided::sumOfDivided(std::vector<int> &lst) {
    int max = 0;
    for ( int i = 0; i < lst.size(); i++ ) {
        if ( max < std::abs(lst[i]) ) max = std::abs(lst[i]);
    }
    if ( max <= 2 ) return "";
    std::vector<bool> prime(max + 1, true);
    for ( int i = 3; i <= max; i++ ) {
        if ( i % 2 == 0 ) prime[i] = false;
    }
    for ( int i = 3; i * i <= max; i++ ) {
        if ( prime[i] ) {
            for ( int j = i * i; j <= max; j += 2 * i ) {
                prime[j] = false;
            }
        }
    }
    std::string res = "";
    for ( int i = 2; i <= max; i++ ) {
        if ( prime[i] ) {
            long sum = 0;
            bool flag = false;
            for ( int j = 0; j < lst.size(); j++ ) {
                if ( lst[j] % i == 0 ){
                    sum += lst[j];
                    flag = true;
                }
            }
            if ( flag ) res += ('(' + std::to_string(i) + ' ' + std::to_string(sum) + ')');
        }
    }
    return res;
}