#pragma once
#include <vector>
#include <stdlib.h>
#include "Character.h"
#include "Action.h"
class CEnemy : public CCharacter
{
public:
	void AddAction(CAction action);
	CAction ChooseRandAction();
	void SetID(int id) { ID = id; }
	int GetID() { return ID; }
	int GetNumActions() { return numActions; }
	std::vector<CAction> GetEnemyActions() { return enemyActions; }
private:
	int ID = 0;
	int numActions = 0;
	std::vector<CAction> enemyActions;
};

