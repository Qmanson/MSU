#include "Bounty.h"
#include <iostream>

bool CBounty::start(CPlayer* P1)
{
    CFight fight;
    fight.AddEnemies(1);
    if (fight.startBattle(*P1, fight.GetEnemies()))
    {
        std::cout << "\nCongrats You Won!";
        return true;
    }
    else
    {
        std::cout << "\nYou lost :[";
        return false;
    }
}

void CBounty::generate()
{
}
