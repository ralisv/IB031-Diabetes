from enum import Enum


class Diabetes(Enum):
    """
    Enum representing the diabetes status of a person.
    """

    YES = 1
    """ The person has been diagnosed with diabetes. """

    YES_ONLY_DURING_PREGNANCY = 2
    """ The person (female) was diagnosed with diabetes only during pregnancy. """

    NO = 3
    """ The person has not been diagnosed with diabetes. """

    PRE_DIABETES_OR_BORDERLINE = 4
    """ The person has been diagnosed with pre-diabetes or borderline diabetes. """

    DONT_KNOW_OR_NOT_SURE = 7
    """ The person is not sure or doesn't know about their diabetes status. """

    REFUSED = 9
    """ The person refused to answer about their diabetes status. """

    Blank = None
    """ The value is not asked or missing. """


class HighBloodPressure(Enum):
    """
    Enum representing whether an adult has been told they have high blood pressure by a healthcare professional.
    """

    NO = 1
    """ No, the person has not been told they have high blood pressure. """

    YES = 2
    """ Yes, the person has been told they have high blood pressure. """

    DONT_KNOW_OR_NOT_SURE_OR_REFUSED_OR_MISSING = 9
    """ The person doesn't know, is not sure, refused to answer, or the value is missing. """


class BloodCholesterolHigh(Enum):
    """
    Enum representing whether a person has ever been told by a healthcare professional that their blood cholesterol is high.
    """

    YES = 1
    """ Yes, the person has been told their blood cholesterol is high. """

    NO = 2
    """ No, the person has not been told their blood cholesterol is high. """

    DONT_KNOW_OR_NOT_SURE = 7
    """ The person doesn't know or is not sure if they have been told their blood cholesterol is high. """

    REFUSED = 9
    """ The person refused to answer. """


class CholesterolChecked(Enum):
    """
    Enum representing whether a person has had their cholesterol checked within the past five years.
    """

    CHECKED_IN_PAST_5_YEARS = 1
    """ The person had their cholesterol checked in the past 5 years. """

    NOT_CHECKED_IN_PAST_5_YEARS = 2
    """ The person did not have their cholesterol checked in the past 5 years. """

    NEVER_CHECKED = 3
    """ The person has never had their cholesterol checked. """

    DONT_KNOW_OR_NOT_SURE_OR_REFUSED_OR_MISSING = 9
    """ The person doesn't know, is not sure, refused to answer, or the value is missing. """


class SmokedAtLeast100Cigarettes(Enum):
    """
    Enum representing whether a person has smoked at least 100 cigarettes in their entire life.
    """

    YES = 1
    """ Yes, the person has smoked at least 100 cigarettes in their entire life. """

    NO = 2
    """ No, the person has not smoked at least 100 cigarettes in their entire life. """

    DONT_KNOW_OR_NOT_SURE = 7
    """ The person doesn't know or is not sure if they have smoked at least 100 cigarettes in their entire life. """

    REFUSED = 9
    """ The person refused to answer. """

    Blank = None
    """ The question was not asked or the value is missing. """


class EverDiagnosedWithStroke(Enum):
    """
    Enum representing whether a person has ever been told they had a stroke.
    """

    YES = 1
    """ Yes, the person has been told they had a stroke. """

    NO = 2
    """ No, the person has not been told they had a stroke. """

    DONT_KNOW_OR_NOT_SURE = 7
    """ The person doesn't know or is not sure if they have been told they had a stroke. """

    REFUSED = 9
    """ The person refused to answer. """


class EverHadCHDorMI(Enum):
    """
    Enum representing whether a person has ever reported having coronary heart disease (CHD) or myocardial infarction (MI).
    """

    REPORTED_HAVING_MI_OR_CHD = 1
    """ The person reported having MI or CHD. """

    DID_NOT_REPORT_HAVING_MI_OR_CHD = 2
    """ The person did not report having MI or CHD. """

    Blank = None
    """ The question was not asked or the value is missing. """


class LeisureTimePhysicalActivity(Enum):
    """
    Enum representing whether an adult reported doing physical activity or exercise during the past 30 days other than their regular job.
    """

    HAD_PHYSICAL_ACTIVITY_OR_EXERCISE = 1
    """ The person had physical activity or exercise in the last 30 days. """

    NO_PHYSICAL_ACTIVITY_OR_EXERCISE_IN_LAST_30_DAYS = 2
    """ The person had no physical activity or exercise in the last 30 days. """

    DONT_KNOW_OR_REFUSED_OR_MISSING = 9
    """ The person didn't know, refused to answer, or the value is missing. """


class ConsumeFruitFrequency(Enum):
    """
    Enum representing the frequency of fruit consumption per day.
    """

    ONE_OR_MORE_TIMES_PER_DAY = 1
    """ Consumed fruit one or more times per day. """

    LESS_THAN_ONE_TIME_PER_DAY = 2
    """ Consumed fruit less than one time per day. """

    DONT_KNOW_OR_REFUSED_OR_MISSING = 9
    """ Don't know, refused to answer, or the value is missing. """


class ConsumeVegetablesFrequency(Enum):
    """
    Enum representing the frequency of vegetable consumption per day.
    """

    ONE_OR_MORE_TIMES_PER_DAY = 1
    """ Consumed vegetables one or more times per day. """

    LESS_THAN_ONE_TIME_PER_DAY = 2
    """ Consumed vegetables less than one time per day. """

    DONT_KNOW_OR_REFUSED_OR_MISSING = 9
    """ Don't know, refused to answer, or the value is missing. """


class HeavyAlcoholConsumption(Enum):
    """
    Enum representing heavy alcohol consumption for adults.
    Heavy drinkers are defined as adult men having more than 14 drinks per week and adult women having more than 7 drinks per week.
    """

    NO = 1
    """ No, the person is not a heavy drinker. """

    YES = 2
    """ Yes, the person is a heavy drinker. """

    DONT_KNOW_OR_REFUSED_OR_MISSING = 9
    """ Don't know, refused to answer, or the value is missing. """


class HealthCareCoverage(Enum):
    """
    Enum representing whether a person has any kind of health care coverage.
    This includes health insurance, prepaid plans such as HMOs, government plans such as Medicare, or Indian Health Service.
    """

    YES = 1
    """ Yes, the person has health care coverage. """

    NO = 2
    """ No, the person does not have health care coverage. """

    DONT_KNOW_OR_NOT_SURE = 7
    """ The person doesn't know or is not sure if they have health care coverage. """

    REFUSED = 9
    """ The person refused to answer. """


class CouldNotSeeDoctorBecauseOfCost(Enum):
    """
    Enum representing whether there was a time in the past 12 months when a person needed to see a doctor but could not because of cost.
    """

    YES = 1
    """ Yes, there was a time in the past 12 months when the person needed to see a doctor but could not because of cost. """

    NO = 2
    """ No, there was no time in the past 12 months when the person needed to see a doctor but could not because of cost. """

    DONT_KNOW_OR_NOT_SURE = 7
    """ The person doesn't know or is not sure if there was a time in the past 12 months when they needed to see a doctor but could not because of cost. """

    REFUSED = 9
    """ The person refused to answer. """

    BLANK = None
    """ The question was not asked or the value is missing. """


from enum import Enum


class GeneralHealth(Enum):
    """
    Enum representing a person's general health status.
    """

    EXCELLENT = 1
    """ Excellent general health. """

    VERY_GOOD = 2
    """ Very good general health. """

    GOOD = 3
    """ Good general health. """

    FAIR = 4
    """ Fair general health. """

    POOR = 5
    """ Poor general health. """

    DONT_KNOW_OR_NOT_SURE = 7
    """ The person doesn't know or is not sure about their general health. """

    REFUSED = 9
    """ The person refused to answer about their general health. """

    Blank = None
    """ The question was not asked or the value is missing. """


from enum import Enum


class DaysMentalHealthNotGood(Enum):
    """
    Enum representing the number of days during the past 30 days when a person's mental health was not good.
    Mental health includes stress, depression, and problems with emotions.
    """

    NONE = 88
    """ No days during the past 30 days when mental health was not good. """

    DONT_KNOW_OR_NOT_SURE = 77
    """ The person doesn't know or is not sure about the number of days when their mental health was not good. """

    REFUSED = 99
    """ The person refused to answer about the number of days when their mental health was not good. """

    @property
    def days(self):
        """
        Returns the number of days when mental health was not good.
        If the value is not a valid number of days (1-30), returns None.
        """
        if 1 <= self.value <= 30:
            return self.value
        return None


from enum import Enum


class DifficultyWalkingOrClimbingStairs(Enum):
    """
    Enum representing whether a person has serious difficulty walking or climbing stairs.
    """

    YES = 1
    """ Yes, the person has serious difficulty walking or climbing stairs. """

    NO = 2
    """ No, the person does not have serious difficulty walking or climbing stairs. """

    DONT_KNOW_OR_NOT_SURE = 7
    """ The person doesn't know or is not sure if they have serious difficulty walking or climbing stairs. """

    REFUSED = 9
    """ The person refused to answer about their difficulty walking or climbing stairs. """

    Blank = None
    """ The question was not asked or the value is missing. """


class RespondentSex(Enum):
    """
    Enum representing the sex of the respondent.
    """

    MALE = 1
    """ Male respondent. """

    FEMALE = 2
    """ Female respondent. """


class AgeFiveYearCategories(Enum):
    """
    Enum representing the fourteen-level age category based on the reported age.
    """

    AGE_18_TO_24 = 1
    """ Age 18 to 24. """

    AGE_25_TO_29 = 2
    """ Age 25 to 29. """

    AGE_30_TO_34 = 3
    """ Age 30 to 34. """

    AGE_35_TO_39 = 4
    """ Age 35 to 39. """

    AGE_40_TO_44 = 5
    """ Age 40 to 44. """

    AGE_45_TO_49 = 6
    """ Age 45 to 49. """

    AGE_50_TO_54 = 7
    """ Age 50 to 54. """

    AGE_55_TO_59 = 8
    """ Age 55 to 59. """

    AGE_60_TO_64 = 9
    """ Age 60 to 64. """

    AGE_65_TO_69 = 10
    """ Age 65 to 69. """

    AGE_70_TO_74 = 11
    """ Age 70 to 74. """

    AGE_75_TO_79 = 12
    """ Age 75 to 79. """

    AGE_80_OR_OLDER = 13
    """ Age 80 or older. """

    DONT_KNOW_REFUSED_OR_MISSING = 14
    """ Don't know, refused, or missing age value. """


class EducationLevel(Enum):
    """
    Enum representing the highest grade or year of school completed by the respondent.
    """

    NEVER_ATTENDED_OR_ONLY_KINDERGARTEN = 1
    """ Never attended school or only attended kindergarten. """

    GRADES_1_TO_8 = 2
    """ Completed grades 1 through 8 (Elementary). """

    GRADES_9_TO_11 = 3
    """ Completed grades 9 through 11 (Some high school). """

    GRADE_12_OR_GED = 4
    """ Completed grade 12 or obtained a GED (High school graduate). """

    COLLEGE_1_TO_3_YEARS = 5
    """ Completed 1 year to 3 years of college or technical school (Some college or technical school). """

    COLLEGE_4_YEARS_OR_MORE = 6
    """ Completed 4 years or more of college (College graduate). """

    REFUSED = 9
    """ The respondent refused to answer. """


class IncomeLevel(Enum):
    """
    Enum representing the annual household income level from all sources.
    """

    LESS_THAN_10000 = 1
    """ Annual household income is less than $10,000. """

    LESS_THAN_15000 = 2
    """ Annual household income is less than $15,000 ($10,000 to less than $15,000). """

    LESS_THAN_20000 = 3
    """ Annual household income is less than $20,000 ($15,000 to less than $20,000). """

    LESS_THAN_25000 = 4
    """ Annual household income is less than $25,000 ($20,000 to less than $25,000). """

    LESS_THAN_35000 = 5
    """ Annual household income is less than $35,000 ($25,000 to less than $35,000). """

    LESS_THAN_50000 = 6
    """ Annual household income is less than $50,000 ($35,000 to less than $50,000). """

    LESS_THAN_75000 = 7
    """ Annual household income is less than $75,000 ($50,000 to less than $75,000). """

    GREATER_THAN_OR_EQUAL_75000 = 8
    """ Annual household income is $75,000 or more. """

    DONT_KNOW_OR_NOT_SURE = 77
    """ The respondent doesn't know or is not sure about their annual household income. """

    REFUSED = 99
    """ The respondent refused to answer about their annual household income. """

    Blank = None
    """ The question was not asked or the value is missing. """
