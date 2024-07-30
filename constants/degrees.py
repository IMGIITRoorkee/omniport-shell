"""
Degrees offered by IIT Roorkee
"""

# Graduate degrees
BACHELOR_OF_TECHNOLOGY = 'btech'
INTEGRATED_DUAL_DEGREE = 'idd'
BACHELOR_OF_SCIENCE = 'bsc'
BACHELOR_OF_ARCHITECTURE = 'barch'
INTEGRATED_MASTER_OF_SCIENCE = 'imsc'
INTEGRATED_MASTER_OF_TECHNOLOGY = 'imt'
BACHELOR_OF_SCIENCE_MASTER_OF_SCIENCE = 'bsms'
BACHELOR_OF_DESIGN = 'bdes'

GRADUATE_DEGREES = (
    (
        BACHELOR_OF_TECHNOLOGY,
        'B.Tech. - Bachelor of Technology',
    ),
    (
        INTEGRATED_DUAL_DEGREE,
        'Int. M.Tech. - Integrated Dual Degree',
    ),
    (
        BACHELOR_OF_SCIENCE,
        'B.Sc. - Bachelor of Science',
    ),
    (
        BACHELOR_OF_ARCHITECTURE,
        'B.Arch. - Bachelor of Architecture',
    ),
    (
        INTEGRATED_MASTER_OF_SCIENCE,
        'Int. M.Sc. - Integrated Master of Science',
    ),
    (
        INTEGRATED_MASTER_OF_TECHNOLOGY,
        'Int. M.Tech - Integrated Master of Technology',
    ),
    (
        BACHELOR_OF_SCIENCE_MASTER_OF_SCIENCE,
        'BS-MS - Bachelor of Science - Master of Science',
    ),
    (
        BACHELOR_OF_DESIGN,
        'B.Des. - Bachelor of Design',
    )
)

# Postgraduate degrees
MASTER_OF_TECHNOLOGY = 'mtech'
MASTER_OF_SCIENCES = 'msc'
MASTER_OF_ARCHITECTURE = 'march'
MASTER_OF_URBAN_AND_REGIONAL_PLANNING = 'murp'
POSTGRADUATE_DIPLOMA_COURSE = 'pgdip'
MASTER_OF_BUSINESS_ADMINISTRATION = 'mba'
MASTER_OF_COMPUTER_APPLICATIONS = 'mca'
MASTER_OF_DESIGN = 'mdes'
MASTER_IN_INNOVATION_MANAGEMENT = 'mim'

POSTGRADUATE_DEGREES = (
    (
        MASTER_OF_TECHNOLOGY,
        'M.Tech. - Master of Technology',
    ),
    (
        MASTER_OF_SCIENCES,
        'M.Sc. - Master of Science',
    ),
    (
        MASTER_OF_ARCHITECTURE,
        'M.Arch. - Master of Architecture',
    ),
    (
        MASTER_OF_URBAN_AND_REGIONAL_PLANNING,
        'M.U.R.P - Master of Urban and Regional Planning',
    ),
    (
        POSTGRADUATE_DIPLOMA_COURSE,
        'P.G. Dip. - Post-graduate Diploma',
    ),
    (
        MASTER_OF_BUSINESS_ADMINISTRATION,
        'M.B.A. - Master of Business Administration',
    ),
    (
        MASTER_OF_COMPUTER_APPLICATIONS,
        'M.C.A. - Master of Computer Applications',
    ),
    (
        MASTER_OF_DESIGN,
        'M.Des. - Master of Design',
    ),
    (
        MASTER_IN_INNOVATION_MANAGEMENT,
        'Master in Innovation Management',
    ),
)

# Doctorate degrees
DOCTOR_OF_PHILOSOPHY = 'phd'
DOCTORATE_DEGREES = (
    (
        DOCTOR_OF_PHILOSOPHY,
        'Ph.D. - Doctor of Philosophy',
    ),
)

# Postdoctorate degrees
POSTDOCTORATE = 'pdoc'
POSTDOCTORATE_DEGREES = (
    (
        POSTDOCTORATE,
        'Post Doc. - Post-doctorate',
    ),
)

DEGREES = (
        GRADUATE_DEGREES
        + POSTGRADUATE_DEGREES
        + DOCTORATE_DEGREES
        + POSTDOCTORATE_DEGREES
        )
