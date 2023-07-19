#include "GraphServiceSettingsFactory.h"

GraphServiceSettingsFactory::GraphServiceSettingsFactory() {
    _settings = make_shared<Settings>();
    _settings->set_port(8080);
    _settings->set_default_header("Connection", "close");
    _settings->set_default_header("Access-Control-Allow-Origin", "*"); //CORS

}

shared_ptr<Settings> GraphServiceSettingsFactory::get_settings() const {
    return _settings;
}