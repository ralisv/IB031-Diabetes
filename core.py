from enum import Enum, EnumMeta
from pathlib import Path

import pandas as pd

import categories as cat


def load_dataset(part_dir) -> pd.DataFrame:
    dataset_parts_df = [
        pd.read_csv(Path(part_dir) / f"part{part_num}.csv") for part_num in range(1, 6)
    ]
    return pd.concat(dataset_parts_df)


def get_column_mapping() -> dict[str, str]:
    """Return a dictionary mapping the original column names to more descriptive names"""
    return {
        "DIABETE3": "diabetes",
        "_RFHYPE5": "high_blood_pressure",
        "TOLDHI2": "high_cholesterol",
        "_CHOLCHK": "cholesterol_check",
        "_BMI5": "bmi",
        "SMOKE100": "smoked_100_cigarettes",
        "CVDSTRK3": "stroke",
        "_MICHD": "coronary_disease",
        "_TOTINDA": "exercise",
        "_FRTLT1": "consumes_fruit",
        "_VEGLT1": "consumes_vegetable",
        "_RFDRHV5": "heavy_alcohol_drinker",
        "HLTHPLN1": "insurance",
        "MEDCOST": "no_doctor_money",
        "GENHLTH": "health",
        "MENTHLTH": "mental_health",
        "PHYSHLTH": "physical_health",
        "DIFFWALK": "climb_difficulty",
        "SEX": "sex",
        "_AGEG5YR": "age_category",
        "EDUCA": "education_level",
        "INCOME2": "income",
    }


def get_enum_mapping() -> dict[str, EnumMeta]:
    """Return a dictionary mapping the original column names to a dictionary that maps the original values to more descriptive values"""
    return {
        "diabetes": cat.Diabetes,
        "high_blood_pressure": cat.HighBloodPressure,
        "high_cholesterol": cat.BloodCholesterolHigh,
        "cholesterol_check": cat.CholesterolChecked,
        "smoked_100_cigarettes": cat.SmokedAtLeast100Cigarettes,
        "stroke": cat.EverDiagnosedWithStroke,
        "coronary_disease": cat.EverHadCHDorMI,
        "exercise": cat.LeisureTimePhysicalActivity,
        "consumes_fruit": cat.ConsumeFruitFrequency,
        "consumes_vegetable": cat.ConsumeVegetablesFrequency,
        "heavy_alcohol_drinker": cat.HeavyAlcoholConsumption,
        "insurance": cat.HealthCareCoverage,
        "no_doctor_money": cat.CouldNotSeeDoctorBecauseOfCost,
        "health": cat.GeneralHealth,
        "climb_difficulty": cat.DifficultyWalkingOrClimbingStairs,
        "sex": cat.RespondentSex,
        "age_category": cat.AgeFiveYearCategories,
        "education_level": cat.EducationLevel,
        "income": cat.IncomeLevel,
    }


def process_columns(dataset: pd.DataFrame) -> None:
    """Process the columns of the dataset to make them more descriptive and categorical"""

    dataset.rename(columns=get_column_mapping(), inplace=True)

    def to_category_values(val):
        """Convert numerical values to string representations from the corresponding Enum classes"""

        convert_to_nan = {
            "REFUSED",
            "Blank",
            "DONT_KNOW_OR_NOT_SURE",
            "DONT_KNOW_OR_NOT_SURE_OR_REFUSED_OR_MISSING",
            "DONT_KNOW_OR_REFUSED_OR_MISSING",
            "BLANK",
            "DONT_KNOW_REFUSED_OR_MISSING",
            "NONE"
        }

        if pd.isna(val) or enum_class(val).name in convert_to_nan:  # type: ignore
            return pd.NA
        return str(enum_class(val))

    for column_name, enum_class in get_enum_mapping().items():
        dataset[column_name] = dataset[column_name].apply(to_category_values)

    object_cols = dataset.select_dtypes(include=["object"]).columns
    dataset[object_cols] = dataset[object_cols].astype("category")
