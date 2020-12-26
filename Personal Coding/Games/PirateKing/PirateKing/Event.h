#pragma once
#include "Player.h"
#include <string>
class CEvent
{
public:
	virtual std::string getName();
	virtual bool start(CPlayer* P1);
	virtual void generate();

};

