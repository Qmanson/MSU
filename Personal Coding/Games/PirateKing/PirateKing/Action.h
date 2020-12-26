/* Action header 
 * 
 * Actions are subsections of Items
 * Actions are used in combat 
 * -Quincy Manson 
 */
#pragma once
#include "Item.h"
#include <string>

class CAction : public CItem
{
public:
	void SetCost(int c) { cost = c; }
	int GetCost() { return cost; }
	virtual void SetEnemyDuration(int* dur);
	virtual void SetPlayerDuration(int* dur);
	virtual int* GetEnemyDuration() { return EnemyEffectDuration; }
	virtual int* GetPlayerDuration() { return PlayerEffectDuration; }
	virtual void SetEffectEnemy(int* stats);
	virtual int* GetEffectEnemy() { return statsEffectEnemy; }
	virtual void SetEffectPlayer(int* stats);
	virtual int* GetEffectPlayer() { return statsEffectPlayer; }
private:
	int cost = 0; // Cost: How much energy it takes to use
	int statsEffectEnemy[11] = {};
	int EnemyEffectDuration[11] = {};
	int statsEffectPlayer[11] = {};
	int PlayerEffectDuration[11] = {};
};

