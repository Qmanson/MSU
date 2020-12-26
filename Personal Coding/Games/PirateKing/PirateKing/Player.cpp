#include "Player.h"
#include "Sail.h"

CPlayer::CPlayer()
{
    SetMoney(50);
    std::vector<CItem> inv = {};
    SetInv(inv);
    std::vector<CAction> temp = {};
    SetDeck(temp);
    SetHand(temp);
    SetDiscard(temp);
    SetDraw(temp);
    SetCardsOnDraw(3);
}

CPlayer::~CPlayer()
{
}

void CPlayer::DiscardHand()
{
    if (GetHand().size() != 0)
    {
        std::vector<CAction> tempDiscard = GetDiscard();
        for (CAction a : GetHand())
        {
            tempDiscard.push_back(a);
        }
        SetDiscard(tempDiscard);
        SetHand({});
    }
}

void CPlayer::DisplayHand()
{
    for (int i = 0; i < cardsOnDraw; i++)
    {
        if (Deck.size() == 0)
        {
            //need to randomize still
            Deck = Discard;
            Discard = {};
        }
        if (Deck.size() != 0)
        {
            Hand.push_back(Deck.at(0));
            Deck.erase(Deck.begin());
        }
    }
}

void CPlayer::RemoveCardHand(int remove)
{
    CAction DiscardedCard = Hand.at(remove);
    Hand.erase(Hand.begin() + (remove));
    Discard.push_back(DiscardedCard);
}