#include "GraphResourceFactory.h"

GraphResourceFactory::GraphResourceFactory() {
    _resource = std::make_shared<Resource>();

    // api requests
    _resource->set_path(
        "/{disease}"
        "/{numGenes}"
    );
    _resource->set_method_handler("GET", [&](const shared_ptr<Session> session){
        get_handler(session);
    });
}

tuple<string, string> GraphResourceFactory::get_path_paramters(
    const shared_ptr<Session> session) {

        const auto& request = session->get_request();
        auto disease = request->get_path_parameter("disease");
        auto numGenes = request->get_path_parameter("numGenes");

        return make_tuple(disease, numGenes);
}

shared_ptr<Resource> GraphResourceFactory::get_resource() const {
    return _resource;
}

void GraphResourceFactory::get_handler(const shared_ptr<Session> session){
    const auto [disease, numGenes] = get_path_paramters(session);
    const auto result = "TMP_RESULT"; // should be graph
    auto content = to_json(result);
    session->close(OK, content, 
    {{"Content-Length", to_string(content.size())}});

}

string GraphResourceFactory::to_json(string result){
    ostringstream str_stream;
    str_stream << result;
    nlohmann::json jsonResult = {
        {"result", str_stream.str()}
    };
    return jsonResult.dump();
}