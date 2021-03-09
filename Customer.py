
DATETIME_FORMAT = "%Y-%m-%dT%H:%M:%S"
DATETIME_FORMAT_2 = "%Y-%m-%d"
DATETIME_FORMAT_3 = "T%H:%M"

class Customer(Record):
    """Customer details."""

    system_cif_number = AlphanumericField(
        required=True,
        max_length=60,
        validators=[does_not_contain(" ","|")],
        metadata={
            "description": (
                "The customer/business unique number that is in the core banking application"
            )
        },
    )
    sis_cif_number =   NumericField(
        required=False,
        max_length=60,
        metadata={
            "description": (
                "SIS will create its own unique Customer ID"
            )
        },
    )
    cif_type =  AlphanumericField(
        required=True,
        max_length=10,
        choices=[t.value for t in list(enums.CIFType)],
        metadata={
            "description": (
                "A code that indicates the category a customer falls in."
                "The tax category code of the Account Holder This is the set of valid codes for the Nature of Person."
            )
        },
    )
    sector_code = AlphanumericField(
        required=True,
        max_length=10,
        choices=[t.value for t in list(enums.SectorCode)],
        metadata={
            "description": (
                "The Sector code the customer either works or represents."
            )
        },
    )
    industry_id = AlphanumericField(
        required=True,
        max_length=10,
        choices=[t.value for t in list(enums.IndustryID)],
        metadata={
            "description": (
                "The Industry the customer or business resides in"
            )
        },
    )
    industry_high_level = AlphanumericField(
        required=True,
        max_length=10,
        choices=[t.value for t in list(enums.IndustryHighLevel)],
        metadata={
            "description": (
                "CIF Income Source"
            )
        },
    )
    status = AlphanumericField(
        required=True,
        max_length=2,
        choices=["A", "I"],  # Active, Inactive
        metadata={
            "description": (
                "The Status of the customer/business in the core banking system"
            )
        },
    )
    customer_title = AlphanumericField(
        required=False,
        max_length=2,
        choices=[t.value for t in list(enums.CustomerTitle)],
        metadata={
            "description": (
                "The Title of the Customer or Account Holder"
            )
        },
    )
    name = FreeTextField(
        required=False,
        max_length=100,
        metadata={
            "description": (
                "The First Name of The Customer. Personal particulars"
            )
        },
    )
    surname = FreeTextField(
        required=False,
        max_length=60,
        metadata={
            "description": (
                "The Last Name of the Customer or Account Holder Surname."
            )
        },
    )
    customer_initials = FreeTextField(
        required=False,
        max_length=15,
        metadata={
            "description": (
                "The Initials of the Customer or Account Holder Initials."
            )
        },
    )
    customer_preferred_name = FreeTextField(
        required=False,
        max_length=100,
        metadata={
            "description": (
                "The preferred Name the customer would like to be called"
            )
        },
    )
    identification_type_code_1 = NumericField(
        required=True,
        max_length=2,
        choices=[t.value for t in list(enums.IdentificationTypeCode1)],
        metadata={
            "description": (
                "A code selected from the table of Identification Types to indicate if an ID Number, Passport Number or Date of Birth is the form of identification of the Customer"
            )
        },
    )
    identity_number_1 = FreeTextField(
        required=True,
        max_length=13,
        metadata={
            "description": (
                "Personal particulars – South African Identity number of the individual taxpayer."
                "a) At least one of the Account Holder Identity number, A Passport Number or Account Holder Date of Birth fields must be completed for Individuals, not required for all other NPOs (Non-Profit Organisation)"
            )
        },
    )
    identity_1_issued_date =  DateTimeField(
        required=False,
        max_length=8,
        min_length=8,
        validators=[not_in_past(value)],
        metadata={
            "description": (
                "Date the passport was issued/"
                "Temporary permit number/"
                "Foreign ID"
            )
        },
        serialized_format=DATETIME_FORMAT_2,
    )
    identity_1_country = AlphanumericField(
        required=False,
        max_length=10,
        metadata={
            "description": (
                "The Country the Passport was issued"
            )
        },
    )
    identity_1_expiry_date = DateTimeField(
        required=False,
        max_length=8,
        min_length=8,
        validators=[not_in_past(value)],
        metadata={
            "description": (
                "Date Passport/temporary ID Number/Foreign ID will expire"
            )
        },
        serialized_format=DATETIME_FORMAT_2,
    )
    identification_type_code_2 = AlphanumericField(
        required=False,
        max_length=2,
        choices=[t.value for t in list(enums.IdentificationTypeCode2)],
        metadata={
            "description": (
                "A code selected from the table of Identification Types to indicate if an ID Number, Passport Number or Date of Birth is the form of identification of the Customer"
                "This field is used if an individual has 2 identification types"
            )
        },
    )
    identity_number_2 = FreeTextField(
        required=False,
        max_length=25,
        metadata={
            "description": (
                "Personal particulars – South African Identity number of the individual taxpayer."
                "a) At least one of the Account Holder Identity number, Account Holder Passport Number or Account Holder Date of Birth fields must be completed for Individuals, not required for all other NoPs"
            )
        },
    )
    identity_2_issued_date = DateTimeField(
        required=False,
        max_length=8,
        min_length=8,
        metadata={
            "description": (
                "Date the passport was issued/ temporary permit number/Foreign ID"
            )
        },
        serialized_format=DATETIME_FORMAT_2,
    )
    identity_2_country = AlphanumericField(
        required=False,
        max_length=7,
        metadata={
            "description": (
                "The Country the Passport was issued"
            )
        },
    )
    identity_2_expiry_date = DateTimeField(
        required=False,
        max_length=8,
        min_length=8,
        metadata={
            "description": (
                "Date Passport/"
                "Temporary ID Number/"
                "Foreign ID will expire"
            )
        },
    )
    tax_number_of_individual = FreeTextField(
        required=False,
        max_length=30,
        metadata={
            "description": (
                "The tax number for the business or individual"
            )
        },
    )
    customer_birth_date = DateTimeField(
        required=False,
        max_length=8,
        min_length=8,
        metadata={
            "description": (
                "Customer Date of Birth"
            )
        },
        serialized_format=DATETIME_FORMAT_2,
    )
    residence indicator = AlphanumericField(
        required=False,
        max_length=10,
        metadata={
            "description": (
                "South African residence indicator"
            )
        },
        serialized_format=DATETIME_FORMAT_2,
    )
    system_id = AlphanumericField(
        required=True,
        max_length=8,
        metadata={
            "description": (
                "System_ID"
            )
        },
    )
    created_cif_date = DateTimeField(
        required=True,
        max_length=8,
        min_length=8,
        metadata={
            "description": (
                "The date the customer registered at the bank. This will be the date the customer profile was approved."
            )
        },
        serialized_format=DATETIME_FORMAT_2,
    )
    fica_status = AlphanumericField(
        required=True,
        max_length=10,
        choices=[t.value for t in list(enums.FicaStatus)],
        metadata={
            "description": (
                "FICA status of the customer."
            )
        },
    )
    fica_reg_date = DateTimeField(
        required=False,
        max_length=8,
        min_length=8,
        validators=[not_in_future],
        metadata={
            "description": (
                "The Date the FICA was completed"
            )
        },
        serialized_format=DATETIME_FORMAT_2,
    )
    fica_expired_date = DateTimeField(
        required=False,
        max_length=8,
        min_length=8,
        validators=[not_in_past],
        metadata={
            "description": (
                "The Date FICA will Expire"
            )
        },
        serialized_format=DATETIME_FORMAT_2,
    )
    phone_number_1 = NumericField(
        required=False,
        max_length=15,
        min_length=9,
        metadata={
            "description": (
                "Customer Home Phone Number or Business Primary Number"
            )
        },
    )
    phone_number_2 = NumericField(
        required=False,
        max_length=15,
        min_length=9,
        metadata={
            "description": (
                "Customer 2nd Phone Number or business 2nd Phone Number"
            )
        },
    )
    cell_number = NumericField(
        required=False,
        metadata={
            "description": (
                "Customer Cell Number or Business Cell Number"
            )
        },
    )
    fax_number = NumericField(
        required=False,
        metadata={
            "description": (
                "Customer Cell Number or Business Cell Number"
            )
        },
    )
    customer_gender = AlphanumericField(
        required=False,
        max_length=10,
        choices=[t.value for t in list(enums.CustomerGender)],
        metadata={
            "description": (
                "The sex of the customer"
            )
        },
    )
    customer_marital_status = AlphanumericField(
        required=False,
        max_length=10,
        metadata={
            "description": (
                "The Marital status of the customer"
            )
        },
    )
    customer_employment_status = AlphanumericField(
        required=True,
        max_length=10,
        choices=[t.value for t in list(enums.CustomerEmploymentStatus)],
        metadata={
            "description": (
                "Employment status of the customer"
            )
        },
    )
    customer_position = NumericField(
        required=False,
        max_length=10,
        choices=[t.value for t in list(enums.CustomerPosition)],
        metadata={
            "description": (
                "The Position of customers employment"
            )
        },
    )
    customer_salary_deposit_in_acc = FreeTextField(
        required=False,
        max_length=10,
        metadata={
            "description": (
                "Defines if the customer salary will be deposited into the account"
            )
        },
    )
    customer_frequency_income = AlphanumericField(
        required=False,
        max_length=10,
        choices=[t.value for t in list(enums.CustomerFrequencyIncome)],
        metadata={
            "description": (
                "The frequency customer income"
            )
        },
    )
    customer_employer_name = FreeTextField(
        required=False,
        max_length=50,
        metadata={
            "description": (
                "The name of the company or person working for"
            )
        },
    )
    customer_employed_from = DateTimeField(
        required=False,
        max_length=8,
        min_length=8,
        metadata={
            "description": (
                "The date customer was employed at the above company / person < Customer_Employer_Name>"
            )
        },
        serialized_format=DATETIME_FORMAT_2,
    )
    customer_ethnic_group = AlphanumericField(
        required=False,
        max_length=10,
        choices=[t.value for t in list(enums.CustomerEthnicGroup)],
        metadata={
            "description": (
                "The Ethnic Group of the customer"
            )
        },
    )
    customer_home_language = AlphanumericField(
        required=False,
        max_length=10,
        choices=[t.value for t in list(enums.CustomerHomeLanguage)],
        metadata={
            "description": (
                "The Home Language of the customer"
            )
        },
    )
    customer_estimated_monthly_turnover = AlphanumericField(
        required=False,
        max_length=10,
        choices=[t.value for t in list(enums.CustomerEstimatedMonthlyTurnover)]
        metadata={
            "description": (
                "Customer's estimated monthly turnover"
            )
        },
    )
    customer_est_trans_rand_value = AlphanumericField(
        required=False,
        max_length=10,
        choices=[t.value for t in list(enums.CustomerEstTransRandValue)],
        metadata={
            "description": (
                "Customer's estimated transaction rand value"
            )
        },
    )
    customer_expected_source_of_funds = AlphanumericField(
        max_length=10,
        required=True,
        choices=[t.value for t in list(enums.CustomerExpectedSourceOfFunds)],
        metadata={
            "description": (
                "Expected Source customer will receive funds into the account"
            )
        },
    )
    customer_est_cash_transact_value = AlphanumericField(
        max_length=10,
        required=True,
        choices=[t.value for t in list(enums.CustomerEstCashTransactValue)],
        metadata={
            "description": (
                "Estimated cash transaction value a customer will receive into the account"
            )
        },
    )
    customer_expected_use_of_channel = AlphanumericField(
        max_length=10,
        required=True,
        choices=[t.value for t in list(enums.CustomerExpectedUseOfChannel)],
        metadata={
            "description": (
                "The channel that the customer will use for foreign transactions"
            )
        },
    )
    customer_expected_foreign_transactions = AlphanumericField(
        required=True,
        max_length=10,
        choices=[t.value for t in list(enums.CustomerExpectedForeignTransactions)],
        metadata={
            "description": (
                "The amount of foreign transactions expected"
            )
        },
    )
    customer_expected_foreign_country = AlphanumericField(
        required=False,
        max_length=10,
        choices=[t.value for t in list(enums.CustomerExpectedForeignCountry)],
        metadata={
            "description": (
                "The expected foreign country"
            )
        },
    )
    customer_declared_insolvent = AlphanumericField(
        required=False,
        max_length=10,
        choices=["T", "F"],  # True, False
        metadata={
            "description": (
                "Customer has declared insolvency"
            )
        },
    )
    customer_rehabilitated = group_id = AlphanumericField(
        required=False,
        max_length=10,
        choices=["T", "F"],  # True, False
        metadata={
            "description": (
                "Customer is undergoing rehab"
            )
        },
    )
    customer_rehab_start_date = DateTimeField(
        required=False,
        max_length=8,
        min_length=8,
        metadata={
            "description": (
                "Date Customer started Rehab"
            )
        },
        serialized_format=DATETIME_FORMAT_2,
    )
    customer_court_order_ref_num = FreeTextField(
        required=False,
        max_length=65,
        metadata={
            "description": (
                "The court order reference number"
            )
        },
    )
    consultant_id = AlphanumericField(
        required=False,
        max_length=10,
        metadata={
            "description": (
                "The Name of the staff member / "
                "consultant who created /"
                "updated the customer profile"
            )
        },
    )
    relationship_manager_id = AlphanumericField(
        required=False,
        max_length=10,
        metadata={
            "description": (
                "The relationship manager for the account"
            )
        },
    )
    rm3_risk_rating = AlphanumericField(
        required=False,
        max_length=10,
        choices=[t.value for t in list(enums.Rm3RiskRating)],
        metadata={
            "description": (
                "This will be a SARB Rating if it’s an individual"
                "or RM3 if its business"
            )
        },
    )
    branch_suite_id = AlphanumericField(
        required=False,
        max_length=20,
        metadata={
            "description": (
                "The Suite the customer will use for queries/Transactions"
            )
        },
    )
    risk_rating = AlphanumericField(
        required=False,
        max_length=10,
        metadata={
            "description": (
                "Internal Risk Rating"
            )
        },
    )
    credit_risk = AlphanumericField(
        required=False,
        max_length=10,
        metadata={
            "description": (
                "Credit Risk Rating"
            )
        },
    )
    marketing_ind = AlphanumericField(
        required=False,
        max_length=10,
        choices=["T", "F"],  # True, False
        metadata={
            "description": (
                "If the customer would like marketing content from Grobank"
            )
        },
    )
    suitable_contact_time = AlphanumericField(
        required=False,
        max_length=10,
        choices=[t.value for t in list(enums.SuitableContactTime)],
        metadata={
            "description": (
                "The time Grobank should contact the customer for marketing"
            )
        },
    )
    customer_nationality = AlphanumericField(
        required=True,
        max_length=10,
        choices=[t.value for t in list(enums.CustomerNationality)],
        metadata={
            "description": (
                "The Nationality of customer"
            )
        },
    )
    email = FreeTextField( //  EmailField
        required=False,
        max_length=100,
        metadata={
            "description": (
                "The primary email address for the contact person, either for business or individual"
            )
        },
    )
    business_name = FreeTextField(
        required=False,
        max_length=100,
        metadata={
            "description": (
                "Name of the business/entity or Registered Name of Account Holder."
            )
        },
    )
    business_registration_number = FreeTextField(
        required=False,
        max_length=50,
        metadata={
            "description": (
                "Registration number of the entity"
            )
        },
    )
    business_type_of_business = AlphanumericField(
        required=False,
        max_length=10,
        choices=[t.value for t in list(enums.BusinessTypeOfBusiness)],
        metadata={
            "description": (
                "The type of business"
            )
        },
    )
    business_trading_name = FreeTextField(
        required=False,
        max_length=100,
        metadata={
            "description": (
                "The trading name of the business"
            )
        },
    )
    business_vat_number = FreeTextField(
        required=False,
        max_length=20,
        metadata={
            "description": (
                "The VAT number of the business"
            )
        },
    )
    business_reg_date = DateTimeField(
        required=False,
        max_length=8,
        min_length=8,
        metadata={
            "description": (
                "The date the business was registered"
            )
        },
        serialized_format=DATETIME_FORMAT_2,
    )
    business_tax_number = FreeTextField(
        required=False,
        max_length=30,
        metadata={
            "description": (
                "The tax number for the business"
            )
        },
    )
    business_tax_clearance_cert_num = FreeTextField(
        required=False,
        max_length=30,
        metadata={
            "description": (
                "The tax clearance cert number for the business"
            )
        },
    )
    business_contact_person_name = FreeTextField(
        required=False,
        max_length=10,
        metadata={
            "description": (
                "The primary contact person name"
            )
        },
    )
    business_profile_status = AlphanumericField(
        required=False,
        max_length=10,
        metadata={
            "description": (
                "Business profile status"
            )
        },
    )
    business_rehabilitated = AlphanumericField(
        required=False,
        max_length=10,
        choices=["Y", "N"],  # Yes, No
        metadata={
            "description": (
                "Business seeking financial advice status"
            )
        },
    )
    business_bee_status = AlphanumericField(
        required=False,
        max_length=10,
        metadata={
            "description": (
                "The BEE status of the business"
            )
        },
    )
    unit_number_plot_or_farm_number = FreeTextField(
        required=False,
        max_length=10,
        metadata={
            "description": (
                "Indicates unit number of the Account Holder Physical address."
            )
        },
    )
    complex_name_plot_or_farm_name = FreeTextField(
        required=False,
        max_length=100,
        metadata={
            "description": (
                "Indicates the complex name of the Account Holder Physical address."
            )
        },
    )
    street_number = FreeTextField(
        required=False,
        max_length=10,
        metadata={
            "description": (
                "Indicates the street number of the Account Holder Physical address."
            )
        },
    )
    street_name = FreeTextField(
            required=False,
            max_length=100,
            min_length=1,
            metadata={
            "description": (
                "Street_Name Indicates the street name"
            )
        },
    )
    city_town = FreeTextField(
            required=False,
            max_length=50,
            min_length=1,
            metadata={
            "description": (
                "City/Town"
            )
        },
    )
    province = AlphanumericField(
        required=False,
        max_length=20,
        choices=[c.value for c in list(enums.Province)],
        metadata={
            "description": (
                "Represent the province the account holder resides"
            )
        },
    )
    country = AlphanumericField(
        required=False,
        max_length=50,
        choices=[t.value for t in list(enums.Country)],
        metadata={
            "description": (
                "The country code for the account holder"
            )
        },
    )
    address_postal_code = AlphanumericField(
        required=False,
        max_length=9,
        min_length=1,
        metadata={
            "description": (
                "Indicates the postal code of the Account Holder Physical address"
            )
        },
    )
    suburb_district = FreeTextField(
            required=False,
            max_length=50,
            min_length=1,
            metadata={
            "description": (
                "Indicates the Suburb/District of the Account Holder Physical address"
            )
        },
    )
    postal_adress_ind = AlphanumericField(
            required=False,
            max_length=1,
            min_length=1,
            metadata={
            "description": (
                "Postal address indicator if same as residential address"
            )
        },
    )
    postal_suburb = FreeTextField(
            required=False,
            max_length=50,
            min_length=1,
            metadata={
            "description": (
                "The suburb where the postal code resides"
            )
        },
    )
    postal_country = AlphanumericField(
            required=False,
            max_length=50,
            choices=[t.value for t in list(enums.PostalCountry)],
            metadata={
            "description": (
                "The postal country code"
            )
        },
    )
    postal_province = AlphanumericField
            required=False,
            max_length=20,
            choices=[t.value for t in list(enums.PostalProvince)],
            metadata={
            "description": (
                "The province the postal resides"
            )
        },
    )
    postal_address = FreeTextField(
            required=False,
            max_length=100,
            min_length=1,
            metadata={
            "description": (
                "The postal address line"
            )
        },
    )
    postal_code = AlphanumericField(
            required=False,
            max_length=10,
            min_length=1,
            metadata={
            "description": (
                "The postal code"
            )
        },
    )
    group_name = AlphanumericField(
         required=False,
         max_length=45,
         metadata={
            "description": (
                "The Name of the group the CIF belongs to"
            )
        },
    )
    group_code = AlphanumericField(
        required=False,
        max_length=10,
         metadata={
            "description": (
                "The Group Code assigned to the CIF"
            )
        },
    )
    cif_record_type = FreeTextField(
        required=True,
        max_length=1,
        min_length=1,
        choices=["N", "D", "U"],  # New, Delete, Update
        metadata={
            "description": (
                "The record type could be new, delete or update"
                "e.g. if a record has been edited in source system then the full record should be sent with U"
            )
        },
    )
    postal_city = FreeTextField(
        required=True,
        max_length=100,
        metadata={
            "description": (
                "The postal address city"
            )
        },
    )
    business_contact_person_surname = FreeTextField(
        required=False,
        max_length=60,
        metadata={
            "description": (
                "The primary contact person surname"
            )
        },
    )
    financial_turnover = NumericField(
        required=False,
        max_length=40,
        min_length=1,
        metadata={
            "description": (
                "The customer/business financial turnover for the year"
            )
        },
    )
    suitable_contact_start_time = FreeTextField(
        required=False,
        max_length=5,
        metadata={
            "description": (
                "The effective start time to call the customer"
            )
        },
        serialized_format=DATETIME_FORMAT_3,
    )
    suitable_contact_end_time = FreeTextField(
        required=False,
        max_length=5,
        metadata={
            "description": (
                "The effective end time to call the customer"
            )
        },
    )
    watch_list_indicator = FreeTextField(
        required=True,
        max_length=3,
        choices=["Y", "N"],  # Yes, No
        metadata={
            "description": (
                "This is to identify that the customer record is on the Watchlist. Watchlist clients are closely monitored by Grobank"
            )
        },
    )
    residential_status_code = AlphanumericField(
        required=True,
        max_length=30,
        choices=[t.value for t in list(enums.ResidentialStatusCode)],
        metadata={
            "description": (
                "It’s included in the address details for the Customer."
            )
        },
    )

