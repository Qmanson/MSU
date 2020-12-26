#pragma once
#include <string>
#include <vector>
#include "Event.h"

class CPlayer;

class CSail;

class CIsland
{
public:
	void generateIsland(std::string type);
	void generateHome();
	void generateUninhab();
	void generateVill();
	void generateTown();
	void generateCity();
	void generateBase();

	void land(CPlayer user);
private:
	CPlayer* User;
	std::vector<CEvent*> Events = {};
	std::string Type;
	int pop;
	bool navy = false;
	bool pirate = false;
	std::vector<std::string> posTypes = {
		"Home",
		"Uninhab",
		"Vill",
		"Town",
		"City",
		"Base"
	};
	std::vector<std::string> posEvents = {
		"Stash",
		"Explore",
		"Bar",
		"Merchant",
		"Doctor",
		"Bounty",
		"Shipyard",
		"Jail",
		"Arena",
		"Davy Back Fight",
		"Plunder"
	};
};

