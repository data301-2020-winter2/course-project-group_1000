[![Work in Repl.it](https://classroom.github.com/assets/work-in-replit-14baed9a392b3a25080506f3b7b6d57f295ec2978f6f33ec97e36a161684cbe9.svg)](https://classroom.github.com/online_ide?assignment_repo_id=361469&assignment_repo_type=GroupAssignmentRepo)
# Medical Expenses Analysis with Insurance Premium Estimation

<div align="center"><font size = "2">Data301 Project by Group 1000</font></div>


&emsp;

## Milestones

#### Milestone 1.
&nbsp;&nbsp;&nbsp;&nbsp; - Add necessary files and directories listed in Milestone 1

&nbsp;&nbsp;&nbsp;&nbsp; - Choose an appropriate dataset and load in the data

&nbsp;&nbsp;&nbsp;&nbsp; - Describe project topic and dataset

&emsp;

## Our Topic

Our chosen topic is derived from a dataset of medical costs from health insurance providers along with the personal data of the person being insured. The dataset includes both quantitative and categorical data. Quantitative data includes age, BMI, medical charges and number of children and categorical data includes the gender, whether they smoke, and the region they are located. With quantitative data, we can discover correlations by plotting graphs and see if and how each attribute is related to each other and derive a quantitative solution to prove this reasoning. Categorical data can also be used to see the certain characteristics the people insured have and categorize them into groups to explain explicitly the relationship between the characteristics and their medical bills. Charts can be useful to demonstrate categorical relationships and from this dataset we can discover the way health insurance providers determine the amount of coverage and potentially how a computer system can be developed to calculate and predict the risks of the person insured.

&emsp;

## Dataset

> *Acknowledgements: The dataset used in this project originated from [**Machine Learning with R**](https://www.amazon.com/Machine-Learning-techniques-predictive-modeling/dp/1788295862/ref=sr_1_1?dchild=1&keywords=machine+learning+with+r+brett&qid=1613374318&sr=8-1) - a widely-acclaimed machine learning book by Brett Lantz - as a practical example for "predicting medical expenses using linear regression" on pg. 182.*

> *The original dataset [insurance.csv] was later released in the public domain by Miri Choi as [Medical_Cost.csv] in Febuary 2018.*

---

The dataset ressembled demographic statistics from the US Census Bureau and simulated 1,388 individuals currently enrolled in an insurance plan. The dataset consist of the medical charges as well as 6 characteristics of each individual.


### *Attributes*
1. **Age**
   - *[Numerical Discrete]* An integer that denotes the age of each patient.
2. **Sex**
    - *[Categorical Nominal]* A String that denotes patients gender (male or female).
3. **BMI**
    - *[Numerical Continuous]* The body mass index. Indicates whether the patient is overweight or underweight in regards to his/her height.
4. **Children**
   - *[Numerical Discrete]* Provides the number of children covered by the medical insurance.
5. **Smoker**
   - *[Categorical Nominal]* Indicates whether the beneficiary smoke cigarettes.
6. **region**
    - *[Categorical Nominal]* Place of residence in the US. Divided into four regions: northeast, northwest, southeast, southwest.
7. **Medical Charges**
   - *[Numerical Continuous]* Indicates the beneficiary's annual medical expenses.

---

### *Purpose*
All of the attributes mentioned above provide substantial insights to how each factors may relate to one's medical expenses. Our goal of this analysis builds on top of the relationship among these attributes; with the help of data analysis tools, we seek to visualize the correlation of each attributes and medical cost. In return, we may be able to estimate one's insurance premium based on our findings.

&nbsp;

### *Correlation Interests*
1. How does geographic regions correlates to medical charges and other personal characteristics?
2. Visualize relevant correlations between multiple quantitative variables.
3. We expect elderlies and smokers to be burdened with higher insurance premium due to higher likelyhood of health issues, but by how much? And how does the BMI affect the costs?


&emsp;

## Team Members

- Hayward Chow: Not exactly knowledgeable and educated about data analysis but I'm excited to learn a lot through this project.
- Ryan S.H. Lu: I have a feeling that this project is going to be *mind-blowing*.
- Siqiao Yuan: I'm still new to computer programming, but I hope I can learn to become more fluent with my coding.

&emsp;

## References

[GitHub](https://gist.github.com/meperezcuello/82a9f1c1c473d6585e750ad2e3c05a41) - Medical Cost Personal Dataset by meperezcuello

[Kaggle](https://www.kaggle.com/mirichoi0218/insurance) - Medical Cost Personal Dataset by Miri Choi
