from dataclasses import dataclass

from mizuchi.analysis import Analysis
from mizuchi.conclusion import Conclusion
from mizuchi.experiment import Experiment
from mizuchi.hypothesis import Hypothesis
from mizuchi.inquiry import Inquiry
from mizuchi.research import Research


@dataclass(slots=True)
class Koine:
    """A structured record of quantitative investigation."""

    inquiry: Inquiry
    research: Research
    hypothesis: Hypothesis
    experiment: Experiment
    analysis: Analysis
    conclusion: Conclusion
