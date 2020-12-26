#include "Enemy.h"

void CEnemy::AddAction(CAction action)
{
    enemyActions.push_back(action);
    numActions += 1;

}

CAction CEnemy::ChooseRandAction()
{
    int choice = rand() % numActions;
    return enemyActions[choice];
}
