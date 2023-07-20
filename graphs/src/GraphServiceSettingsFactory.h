#pragma once

#include "IServiceSettingsFactory.h"

class GraphServiceSettingsFactory : public IServiceSettingsFactory {

    public:
    GraphServiceSettingsFactory();
    shared_ptr<Settings> get_settings() const final;


    private: 
    shared_ptr<Settings> _settings;
};