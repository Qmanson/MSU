#pragma once
#include "Event.h"
#include "Fight.h"
class CBounty : public CEvent
{
public:
	virtual bool start(CPlayer* P1);
	virtual void generate();
	virtual std::string getName() { return "Bounty"; };
};

