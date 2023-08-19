#include <iostream>
#include <vector>
#include <random>
#include <chrono>
#include <ctime>

void generate_array(std::vector<int>& arr, std::mt19937& gen) {
    std::uniform_int_distribution<> dis(0, 99);

    for (int i = 0; i < arr.size(); ++i) {
        arr[i] = dis(gen);
    }
}

int lcs(const std::vector<int>& a, const std::vector<int>& b) {
    int m = a.size();
    int n = b.size();
    std::vector<std::vector<int>> dp(m + 1, std::vector<int>(n + 1, 0));

    for (int i = 1; i <= m; ++i) {
        for (int j = 1; j <= n; ++j) {
            if (a[i - 1] == b[j - 1]) {
                dp[i][j] = dp[i - 1][j - 1] + 1;
            } else {
                dp[i][j] = std::max(dp[i - 1][j], dp[i][j - 1]);
            }
        }
    }
    return dp[m][n];
}

// int main(int argc, char* argv[]) {
//     if (argc < 2) {
//         std::cerr << "Usage: " << argv[0] << " n" << std::endl;
//         return 1;
//     }
//     int n = std::atoi(argv[1]);

//     int seed = 12345;
//     std::mt19937 gen(seed);
//     std::vector<int> a(n);
//     std::vector<int> b(n);

//     generate_array(a, gen);
//     generate_array(b, gen);

//     auto start = std::chrono::high_resolution_clock::now();
//     int length = lcs(a, b);
//     auto end = std::chrono::high_resolution_clock::now();
//     std::chrono::duration<double> elapsed_seconds = end - start;

//     std::cout << "Time using native C++: " << elapsed_seconds.count() << "s (answer=" << length << ")" << std::endl;

//     return 0;
// }
int main(int argc, char* argv[]) {
    if (argc < 3) {
        std::cerr << "Usage: " << argv[0] << " n n_rep" << std::endl;
        return 1;
    }

    int n = std::atoi(argv[1]);
    int n_rep = std::atoi(argv[2]);

    int seed = 12345;
    std::mt19937 gen(seed);
    std::vector<int> a(n);
    std::vector<int> b(n);

    double duration = 0;
    for (int i = 0; i < n_rep; ++i) {
        generate_array(a, gen);
        generate_array(b, gen);

        auto start = std::chrono::high_resolution_clock::now();
        int length = lcs(a, b);
        auto end = std::chrono::high_resolution_clock::now();
        duration += std::chrono::duration<double>(end - start).count();
    }

    std::cout << "Time using native C++: " << duration << "s (n_rep=" << n_rep << ")" << std::endl;

    return 0;
}
