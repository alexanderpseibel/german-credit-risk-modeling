COLUMN_RENAME_MAP = {
    "laufkont": "status",
    "laufzeit": "duration",
    "moral": "credit_history",
    "verw": "purpose",
    "hoehe": "amount",
    "sparkont": "savings",
    "beszeit": "employment_duration",
    "rate": "installment_rate",
    "famges": "personal_status_sex",
    "buerge": "other_debtors",
    "wohnzeit": "present_residence",
    "verm": "property",
    "alter": "age",
    "weitkred": "other_installment_plans",
    "wohn": "housing",
    "bishkred": "number_credits",
    "beruf": "job",
    "pers": "people_liable",
    "telef": "telephone",
    "gastarb": "foreign_worker",
    "kredit": "kredit"
}

NUMERICAL_FEATURES = ["duration", "amount", "age"]

ORDINAL_FEATURES = [
    "status",
    "employment_duration",
    "installment_rate",
    "present_residence",
    "number_credits",
    "job"
]

CATEGORICAL_FEATURES = [
    "credit_history",
    "purpose",
    "savings",
    "personal_status_sex",
    "other_debtors",
    "other_installment_plans",
    "housing",
    "property"
]

BINARY_FEATURES = ["people_liable", "telephone", "foreign_worker"]
