
#include <iostream>
#include <string>
#include "pass_stub.cpp"
int main(int argc, char** argv){
    bool sim = false;
    std::string input = "example_ir";
    for(int i=1;i<argc;i++){
        std::string a(argv[i]);
        if(a=="--sim") sim=true;
        else input=a;
    }
    if(sim){
        std::cout << "[apply_pass] Running in --sim mode\n";
        return main_pass_stub(input);
    }else{
        std::cout << "[apply_pass] LLVM not linked; running stub as fallback\n";
        return main_pass_stub(input);
    }
}
