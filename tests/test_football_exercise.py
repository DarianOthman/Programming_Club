import pytest
import football_exercise

@pytest.mark.parametrize('score_t1,score_t2,points_t1,points_t2',[
(0,0,1,1),
(1,0,3,0),
(0,1,0,3)
])
def test_calculate_points_oop(score_t1,score_t2,points_t1,points_t2):
    fs=football_exercise.FootballScorer('t1','t2',score_t1,score_t2)
    fs.calculate_points()
    assert fs.points_team_1==points_t1
    assert fs.points_team_2==points_t2


@pytest.mark.parametrize('fs,points_t1,points_t2',[
(football_exercise.FootballScorer('t1','t2',0,0),1,1),
(football_exercise.FootballScorer('t1','t2',5,0),3,0),
(football_exercise.FootballScorer('t1','t2',1,2),0,3)
])
def test_calculate_points_oop1(fs,points_t1,points_t2):
    fs.calculate_points()
    assert fs.points_team_1==points_t1
    assert fs.points_team_2==points_t2