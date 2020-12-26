// PirateKing.cpp : This file contains the 'main' function. Program execution begins and ends there.
//

#include <iostream>
#include <iomanip>
#include <fstream>
#include <sstream>
#include <string>
#include <map>
#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>
#include <vector>
#include <windows.h>

#include "Island.h"
#include "Event.h"
#include "Player.h"
#include "Enemy.h"
#include "Sail.h"

void questioningClass(CPlayer &P1);
void checkingClass(CPlayer &P1, std::string ChoiceToClass[3], int value);
void questioningName(CPlayer &P1);
void checkingName(CPlayer &P1, std::string userName);


//Starting stats for Fighter, Swordsman, and Sniper
int classStats[3][11] = {
        {5,1,65,0,2,2,3,65,3,3,1},
        {5,1,60,2,5,3,3,60,3,3,1},
        {3,3,55,0,5,3,3,55,3,3,7}
};

//Starting deck for Fighter, Swordsman, and Sniper
int classDeck[3][11] = {
        {1,1,2,0,0,0,2,3,2,2,0},
        {1,1,2,0,0,0,2,3,2,2,0},
        {1,1,2,0,0,0,2,3,2,2,0}
};

int main()
{
    HANDLE hConsole = GetStdHandle(STD_OUTPUT_HANDLE);
    int k = 2;
    SetConsoleTextAttribute(hConsole, k);
    std::cout << "Pirate King!\n";
    // Register the window class.
    CPlayer *P1 = new CPlayer();
    questioningClass(*P1);
    questioningName(*P1);

    std::cout << "\nYou start your journey!";
    std::cout << "\nYou are at your home island\n";
    CShip ship;
    (*P1).SetShip(ship);
    CSail sail(*P1);
    (*P1).SetSail(&sail);
    CIsland island;
    island.generateIsland("Home");
    island.land(*P1);
}

void questioningClass(CPlayer &P1)
{
    //Check if correct input later 
    std::string ChoiceToClass[3];
    ChoiceToClass[0] = "fighter";
    ChoiceToClass[1] = "swordsman";
    ChoiceToClass[2] = "sniper";
    int value;
    std::cout << "\nHow do you fight ?\n\n" << std::setw(6) << "Hands " << "Sword " << "Range\n";
    std::cout << std::setw(4) << "1 " << std::setw(6) << "2 " << std::setw(6) << "3\n";
    std::cin >> value;
    if (!std::cin)
    {
        std::cin.clear();
        std::cin.ignore();
        questioningClass(P1);
    }
    else
    {
        checkingClass(P1, ChoiceToClass, value);
    }
    return;
}

void questioningName(CPlayer &P1)
{
    std::cout << "\nWhat's your name ?\n\n";
    std::string userName;
    std::cin >> userName;
    checkingName(P1, userName);
}

void checkingClass(CPlayer &P1, std::string ChoiceToClass[3], int value)
{
    std::cout << "\nOh you're a " << ChoiceToClass[value - 1] << ", is that right? (y/n)\n";
    (P1).SetBaseStats(classStats[value - 1]);
    int* a = (P1).GetBaseStats();
    for (int i = 0; i < sizeof(classStats[value - 1]) / sizeof(classStats[value - 1][0]); i++)
    {
        if (i != 7 && i != 9 && i!=3)
        {
            std::cout << std::setw(15) << (P1).IntToName[i] << "-" << std::setw(10) << a[i] << "\n";
        }
    }
    std::string answer;
    std::cin >> answer;
    
    if (answer == "y")
    {

        std::vector<CAction> deck;
        for (int i = 0; i < sizeof(classDeck[value - 1])/sizeof(classDeck[value - 1][0]); i++)
        {
            CAction move;
            move = (P1).GetFileAction(classDeck[value - 1][i]);
            deck.push_back(move);
        }
        (P1).SetDeck(deck);
        return;
    }
    else if (answer == "n")
    {
        questioningClass((P1));
        return;
    }
    else
    {
        std::cout << "Excuse me ? (only \"y\" or \"n\")";
        checkingClass(P1, ChoiceToClass, value);
    }
}

void checkingName(CPlayer &P1, std::string userName)
{
    std::cout << "\nSo your name is " << userName << ", is that right? (y/n)\n";
    (P1).SetName(userName);
    std::string answer;
    std::cin >> answer;
    if (answer == "y")
    {
        return;
    }
    else if (answer == "n")
    {
        questioningName(P1);
        return;
    }
    else
    {
        std::cout << "Excuse me ? (only \"y\" or \"n\")";
        checkingName((P1),userName);
    }
}