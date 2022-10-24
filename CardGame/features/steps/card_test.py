from behave import *
import main


@Given('I have created a rank object')
def step_impl(context):
    pass


@when('i make a new rank class')
def step_impl(context):
    new_rank = main.Rank('Ace')
    assert new_rank is not None
    context.rank_holder = new_rank


@Then('the value of ranks is stored')
def step_impl(context):
    assert context.rank_holder.curr_rank == 'Ace'


@Given('i make a new Suit Object')
def step_impl(context):
    pass


@When('i make a new suit class')
def step_impl(context):
    new_suit = main.Suit('Clubs')
    assert new_suit is not None
    context.suit_holder = new_suit


@Then('the value of suit is stored')
def step_impl(context):
    assert context.suit_holder.curr_suit == 'Clubs'


@Given('i have a set of cards')
def step_impl(context):
    context.deck = main.Set()
    assert context.deck is not None


@When('i draw a card')
def step_impl(context):
    context.full_deck = len(context.deck.card_set)
    context.used_card = context.deck.get_card()
    assert context.used_card is not None


@Then('It will be removed from the list')
def step_impl(context):
    assert len(context.deck.card_set) < context.full_deck
    assert context.used_card not in context.deck.card_set

