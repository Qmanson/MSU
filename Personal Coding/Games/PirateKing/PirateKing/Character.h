#pragma once
#include "Action.h"
class CCharacter
{
public:
	virtual void SetBaseStats(int stats[11]);
	virtual void SetActionStats(int stats[11]);
	virtual int* GetActionStats() { return actionStats; }
	virtual int* GetBaseStats() { return baseStats; }
	virtual std::string GetName() { return name; }
	virtual void SetName(std::string newName) { name = newName; }
	CAction GetFileAction(int actionID);
	void UpdateOffenseStats(CAction action);
	virtual void UpdateDefenceStats(CAction action, int stats[11]);
	virtual void SetOneActionStat(int newStat, int statNum) { actionStats[statNum] = newStat; }
	std::string IntToName[11]{
		"STR",
		"NAV",
		"MAX HP",
		"BLK",
		"DEX",
		"SPD",
		"WP",
		"HP",
		"MAX ENG",
		"ENG",
		"AIM"
	};
private:
	std::string name = "";
	int baseStats[11] = {};
	int actionStats[11] = {};
};

