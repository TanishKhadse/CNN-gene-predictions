#pragma once

#include <memory>
#include <restbed> // needs installation https://github.com/Corvusoft/restbed

using namespace std;
using namespace restbed;


class IResourceFactory {
    public:
    virtual shared_ptr<Resource> get_resource() const = 0; // Resource object not found


};