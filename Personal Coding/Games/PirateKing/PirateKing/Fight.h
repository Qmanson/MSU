/* Fight header
 * 
 * Fight is subsection of Event
 * Fight handles fighting on islands
 * -Quincy Manson
 */
#pragma once
#include "Event.h"
#include "Enemy.h"
#include "Player.h"
#include <vector>
class CFight
{
public:
	bool startBattle(CPlayer user, std::vector<CEnemy> enemies);
	bool playerStartAction();
	void Display(int card);
	bool playerAction();
	bool CardSelect(int card);
	bool playerActionEnd();
	bool enemyAction();
	bool enemyActionEnd();
	void AddEnemies(int enemyNum);
	CAction GetFileAction(int actionID);
	std::vector<CEnemy> GetEnemies() { return Enemies; }
private:
	std::vector<CEnemy> Enemies = {}; //Vector of Enemies in battle
	int enemyCounter = 0; //Number of enemies in battle
	CPlayer User;	//User in battle 
};

