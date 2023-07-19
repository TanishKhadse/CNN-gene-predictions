#pragma once

#include "IResourceFactory.h"
#include <tuple>
#include <string>

#include <sstream>
#include <iomanip> 
#include <json.hpp>

class GraphResourceFactory : public IResourceFactory {
    public:
    GraphResourceFactory();
    shared_ptr<Resource> get_resource() const final;

    private:

    string to_json(string result); // parameter should be a graph object
    tuple<string, string> get_path_paramters(const shared_ptr<Session> session);
    void get_handler(const shared_ptr<Session> session);
    shared_ptr<Resource> _resource;
};