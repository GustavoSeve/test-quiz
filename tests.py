import pytest
from model import Question

def test_create_question():
    question = Question(title='q1')
    assert question.id != None

def test_create_multiple_questions():
    question1 = Question(title='q1')
    question2 = Question(title='q2')
    assert question1.id != question2.id

def test_create_question_with_invalid_title():
    with pytest.raises(Exception):
        Question(title='')
    with pytest.raises(Exception):
        Question(title='a'*201)
    with pytest.raises(Exception):
        Question(title='a'*500)

def test_create_question_with_valid_points():
    question = Question(title='q1', points=1)
    assert question.points == 1
    question = Question(title='q1', points=100)
    assert question.points == 100

def test_create_choice():
    question = Question(title='q1')
    
    question.add_choice('a', False)

    choice = question.choices[0]
    assert len(question.choices) == 1
    assert choice.text == 'a'
    assert not choice.is_correct

# Novos testes

def test_create_choices_with_invalid_text():
    question = Question(title='q1')
    with pytest.raises(Exception):
        question.add_choice(text="")
    with pytest.raises(Exception):
        question.add_choice(text="a"*101)
    with pytest.raises(Exception):
        question.add_choice(text="a"*500)

def test_create_multiples_choices():
    question = Question(title='q1')
    
    question.add_choice('a', False)
    question.add_choice('b', False)

    choice1 = question.choices[0]
    choice2 = question.choices[1]
    assert choice1.id != choice2.id

def test_remove_choice_by_valid_id():
    question = Question(title='q1')
    question.add_choice('a', False)
    question.add_choice('b', False)

    choice1 = question.choices[0]
    choice2 = question.choices[1]
    question.remove_choice_by_id(choice1.id)
    assert len(question.choices) == 1
    assert question.choices[0].id == choice2.id 

def test_remove_choice_by_invalid_id():
    question = Question(title='q1')
    question.add_choice('a', False)
    with pytest.raises(Exception):
        question.remove_choice_by_id(-10)

def test_remove_all_choices():
    question = Question(title='q1')
    
    question.add_choice('a', False)
    question.add_choice('b', False)
    question.add_choice('c', False)
    question.add_choice('d', True)
    assert len(question.choices) == 4
    
    question.remove_all_choices()
    assert len(question.choices) == 0

def test_set_correct_choices_valid_id():
    question = Question(title='q1')
    question.add_choice('a', False)
    question.add_choice('b', False)
    question.add_choice('c', False)
    
    choice1 = question.choices[0]
    choice2 = question.choices[1]
    choice3 = question.choices[2]

    question.set_correct_choices([choice1.id, choice2.id])
    assert (choice1.is_correct and choice2.is_correct) == True 
    assert choice3.is_correct == False 

def test_set_correct_choices_invalid_id():
    question = Question(title='q1')
    question.add_choice('a', False)
    with pytest.raises(Exception):
        question.set_correct_choices([-10, -20])

def test_correct_selected_choices():
    question = Question(title='q1', max_selections=2)

    c1 = question.add_choice('a')
    c2 = question.add_choice('b', True)
    c3 = question.add_choice('c', True)

    result = question.correct_selected_choices([c2.id, c3.id])

    assert result == [c2.id, c3.id]

def test_correct_selected_choices_exceed_limit():
    question = Question(title='q1', max_selections=1)

    c1 = question.add_choice('a')
    c2 = question.add_choice('b')

    with pytest.raises(Exception):
        question.correct_selected_choices([c1.id, c2.id])

def test_remove_same_choice_twice():
    question = Question(title='q1')

    choice = question.add_choice('a')

    question.remove_choice_by_id(choice.id)

    with pytest.raises(Exception):
        question.remove_choice_by_id(choice.id)

# Fixture

@pytest.fixture
def question():
    question = Question(title='q1')
    return question

@pytest.fixture
def question_with_choices():
    question_choices = Question(title='q1')

    question_choices.add_choice('a', False)
    question_choices.add_choice('b', False)
    question_choices.add_choice('c', False)
    question_choices.add_choice('d', False)

    return question_choices

def test_creating_question_with_fixture(question):
    assert question.id != None 

def test_fixture_creating_multiple_choices_in_question(question_with_choices):
    choices = question_with_choices.choices

    ids = [c.id for c in choices]

    assert len(ids) == len(set(ids))












    

