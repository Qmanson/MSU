#include "Island.h"
#include "Bounty.h"
#include "Shop.h"
#include "Sail.h"
#include <iostream>
#include <iomanip>
#include <stdlib.h>
#include <time.h>
#include <vector>

void CIsland::generateIsland(std::string type)
{
    Type = type;
    if (type == posTypes[0])
    {
        generateHome();
    }
    else if (type == posTypes[1])
    {
        generateUninhab();
    }
    else if (type == posTypes[2])
    {
        generateVill();
    }
    else if (type == posTypes[3])
    {
        generateTown();
    }
    else if (type == posTypes[4])
    {
        generateCity();
    }
    else if (type == posTypes[5])
    {
        generateBase();
    }
}

void CIsland::generateHome()
{
    pop = 501;
    navy = false;
    pirate = false;
    //std::srand(std::time(NULL));
    int rand = std::rand() % 2;
    if (rand == 1)
    {
        Events.push_back(new CBounty);
    } 
    Events.push_back(new CShop);
}

void CIsland::generateUninhab()
{
    pop = 0;
    navy = false;
    pirate = false;
}

void CIsland::generateVill()
{
    pop = 50;
    navy = false;
    pirate = false;
}

void CIsland::generateTown()
{
    pop = 1000;
    navy = false;
    pirate = false;
}

void CIsland::generateCity()
{
    pop = 30000;
    navy = false;
    pirate = false;
}

void CIsland::generateBase()
{
    pop = 2000;
    navy = true;
    pirate = false;
}

void CIsland::land(CPlayer user)
{
    User = &user;
    std::cout << "\nWould you like to: \n";
    int i;
    for (i = 0; i < Events.size(); i++)
    {
        std::cout << "\n" << i + 1 << ") " << Events[i]->getName() << " ";
    }
    std::cout << "\n" << i + 1 << ") Open Map\n ";
    int EventChoice;
    std::cin >> EventChoice;
    if (!std::cin)
    {
        std::cin.clear();
        std::cin.ignore();
    }
    if(EventChoice > (Events.size()+1) || EventChoice < 0)
    {
        std::cout << "Excuse me ? (only number from 1 to " << Events.size()+1 << ")\n";
        land(user);
    }
    else
    {
        if (EventChoice > Events.size())
        {
            (*user.GetSail()).moveShip((user));
        }
        else
        {
            if (Events[EventChoice - 1]->start(&user))
            {
                land(user);
            }
        }
    }
}
