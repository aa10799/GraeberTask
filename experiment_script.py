
# !pip install edsl  # Uncomment if needed
from edsl import Survey, Agent, Scenario  # Fixed import names
from edsl import (
    # QuestionCheckBox,
    # QuestionExtract,
    QuestionFreeText,
    # QuestionFunctional,
    # QuestionLikertFive,
    QuestionLinearScale,
  QuestionMatrix,
    # QuestionList,
    QuestionMultipleChoice,
QuestionNumerical,
    # QuestionRank,
    # QuestionTopK,
    # QuestionYesNo
)

import pandas as pd
import matplotlib.pyplot as plt

# Define cognitive constraint scenarios
poverty_scenario = Scenario({
    "financial_situation": "living in poverty",
    "stress_level": "high",
    "cognitive_bandwidth": "limited",
    "perspective": "I need to make immediate decisions to survive"
})

control_scenario = Scenario({
    "financial_situation": "financially comfortable",
    "stress_level": "low",
    "cognitive_bandwidth": "ample",
    "perspective": "I can plan for the long term"
})

# Create choice questions with economic tradeoffs
questions = [
    QuestionMultipleChoice(
        question_name="choice_1",
        question_text="""Please consider the following two options:
                        Option A: Receive €20 now
                        Option B: Receive €25 in two weeks""",
        question_options=['a)Strongly prefer Option A', 'b) Somewhat prefer Option A', 'c) Neutral', 'd) Somewhat prefer Option B', 'e) Strongly prefer Option B' ],
    ),
    QuestionMultipleChoice(
        question_name="choice_2",
        question_text="""Please consider the following two options:
                           Option A: Receive €50 now
                           Option B: Receive €70 in 6 months""",
        question_options=['a)Strongly prefer Option A', 'b) Somewhat prefer Option A', 'c) Neutral',
                          'd) Somewhat prefer Option B', 'e) Strongly prefer Option B'],
    ),
    QuestionMultipleChoice(
        question_name="choice_3",
        question_text="""Please consider the following two options:
                               Option A: Receive €80 now
                               Option B: Receive €110 in 1 year""",
        question_options=['a)Strongly prefer Option A', 'b) Somewhat prefer Option A', 'c) Neutral',
                          'd) Somewhat prefer Option B', 'e) Strongly prefer Option B'],
    ),
    QuestionMultipleChoice(
        question_name="choice_1_immediate_payout",
        question_text="""   Please consider the following two options:
                           Option A: Receive €5  now
                           Option B: Receive €25 in two weeks""",
        question_options=['a)Strongly prefer Option A', 'b) Somewhat prefer Option A', 'c) Neutral',
                          'd) Somewhat prefer Option B', 'e) Strongly prefer Option B'],
    ),
    QuestionMultipleChoice(
        question_name="choice_2_immediate_payout",
        question_text="""Please consider the following two options:
                         Option A: Receive €65 now
                         Option B: Receive €15 now and €70 in six months""",
        question_options=['a)Strongly prefer Option A', 'b) Somewhat prefer Option A', 'c) Neutral',
                          'd) Somewhat prefer Option B', 'e) Strongly prefer Option B'],
    ),
    QuestionMultipleChoice(
        question_name="choice_3_immediate_payout",
        question_text="""Please consider the following two options:
                        Option A: Receive €80 now
                        Option B: Receive €20 now and €110 in 1 year""",
        question_options=['a)Strongly prefer Option A', 'b) Somewhat prefer Option A', 'c) Neutral',
                          'd) Somewhat prefer Option B', 'e) Strongly prefer Option B'],
    ),
      QuestionMultipleChoice(
        question_name="attention_check",
        question_text="""This study investigated your subjective impressions of money. In many situations, people do not
        think about the pleasure (displeasure) money gives them. In other situations, people are reading
        too fast and are unable to follow instructions in a survey. If you are reading this, click the continue
        button and do not select an answer. Therefore, how often you think about money is important to
        determining how much pleasure you get from it.
        Which best describes you?""",
        question_options=['I think about money all the time', 'I think about money when I have to', 'I rarely think about money', 'continue'],
    ),
    
 QuestionFreeText(
        question_name="free_write",
        question_text=""""‘Please recall a situation in which you were financially worse off [better off] in comparison to peers
around you. It can be any time when you felt your financial position was relatively worse [better]
than theirs. Please describe the context of this situation in which you felt financially worse off
[better off] in comparison to your peers—what happened, how you felt about being worse off
[better off], etc. Please try to focus specifically on aspects related to being worse off [better off]
than your peers financially.’""",
),

 QuestionMultipleChoice(
        question_name="measure_finance_constraint",
        question_text="""When did you last receive a paycheck or unemployment benefits?""",
        question_options=['a) Within the last 7 days' 'b) Within the last 2 weeks', 'c) Within the last month','d) More than a month ago','e) I did not receive a paycheck or unemployment benefits'],
    ),
QuestionMatrix(
question_name = """socio_econ_status_1""",
    question_text = """Please indicate to which extent you agree with the following statements.""",
    question_items = ['To what extent do you feel financially constrained'],
    question_options = [1, 2, 3, 4, 5, 6, 7],
    option_labels = {1: 'Not at all financially constrained', 4:'Neutral', 7: 'Very financially constrained'},)
),

QuestionMatrix(
question_name = """socio_econ_status_2""",
    question_text = """Please indicate to which extent you agree with the following statements.""",
    question_items = ['I grew up in a relative wealthy neighborhood', 'My family usually had enough money for things when I was growing up', 'I felt relatively wealthy compared to the other kids in my school', 'I have enough money to buy things I want ','I don’t need to worry too much about paying my bills', 'I don’t think I’ll have to worry about money too much in the future'],
    question_options = [1, 2, 3, 4, 5, 6, 7],
    option_labels = {1: 'Strongly disagree', 2: 'Disagree', 3: 'Somewhat disagree', 4:'Neither agree nor disagree', 5: 'Somewhat agree', 6: 'Agree', 7: 'Strongly Agree'},)
),
]

# Configure agent populations with proper Agent class
def create_agents(scenario, n=2):
    return [Agent(traits=scenario) for _ in range(n)]

poor_agents = create_agents(poverty_scenario)
control_agents = create_agents(control_scenario)

# Create and run survey
survey = Survey(questions)
results_poverty = survey.by(poor_agents).run(remote=True)
results_control = survey.by(control_agents).run(remote=True)

# Analysis and visualization functions remain the same
# ... [rest of analysis code from previous version]