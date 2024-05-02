"""
Residences in IIT Roorkee
"""

# Boys' hostels
# https://www.iitr.ac.in/campus_life/pages/Hostels.html
AZAD_BHAWAN = 'azb'
CAUTLEY_BHAWAN = 'ctb'
GANGA_BHAWAN = 'gnb'
GOVIND_BHAWAN = 'gvb'
JAWAHAR_BHAWAN = 'jlb'
MALVIYA_BHAWAN = 'mvb'
RADHAKRISHNAN_BHAWAN = 'rkb'
RAJENDRA_BHAWAN = 'rjb'
RAJIV_BHAWAN = 'rgb'
RAVINDRA_BHAWAN = 'rvb'
HIMALAYA_BHAWAN_BOYS = 'hlb'
BOYS_HOSTELS = (
    (AZAD_BHAWAN, 'Azad bhawan'),
    (CAUTLEY_BHAWAN, 'Cautley bhawan'),
    (GANGA_BHAWAN, 'Ganga bhawan'),
    (GOVIND_BHAWAN, 'Govind bhawan'),
    (JAWAHAR_BHAWAN, 'Jawahar bhawan'),
    (MALVIYA_BHAWAN, 'Malviya bhawan'),
    (RADHAKRISHNAN_BHAWAN, 'Radhakrishnan bhawan'),
    (RAJENDRA_BHAWAN, 'Rajendra bhawan'),
    (RAJIV_BHAWAN, 'Rajiv bhawan'),
    (RAVINDRA_BHAWAN, 'Ravindra bhawan'),
    (HIMALAYA_BHAWAN_BOYS,'Himalaya bhawan (boys)')
)

# Girls' hostels
# https://www.iitr.ac.in/campus_life/pages/Hostels.html
SAROJINI_BHAWAN = 'snb'
KASTURBA_BHAWAN = 'kgb'
INDIRA_BHAWAN = 'igb'
VIGYAN_BHAWAN_GIRLS = 'vbg'
HIMGIRI_APARTMENT = 'hia'
HIMALAYA_BHAWAN_GIRLS = 'hlg'
GIRLS_HOSTELS = (
    (SAROJINI_BHAWAN, 'Sarojini bhawan'),
    (KASTURBA_BHAWAN, 'Kasturba bhawan'),
    (INDIRA_BHAWAN, ' Indira bhawan'),
    (VIGYAN_BHAWAN_GIRLS, 'Vigyan bhawan (girls)'),
    (HIMGIRI_APARTMENT, 'Himgiri apartment'),
    (HIMALAYA_BHAWAN_GIRLS, 'Himalaya bhawan (girls)')
)

# Married hostels
# https://www.iitr.ac.in/campus_life/pages/Hostels.html
GP_HOSTEL = 'gph'
MR_CHOPRA_HOSTEL = 'mrc'
AZAD_WING = 'azw'
DS_BARRACK = 'dsb'
AN_KHOSLA_HOUSE = 'ank'
KHOSLA_INTERNATIONAL_HOUSE = 'khs'
VIDYASAGAR_BHAWAN = 'mhs'
MARRIED_HOSTELS = (
    (GP_HOSTEL, 'G.P. hostel'),
    (MR_CHOPRA_HOSTEL, 'M.R. Chopra hostel'),
    (AZAD_WING, 'Azad wing'),
    (DS_BARRACK, 'D.S. Barrack hostel'),
    (AN_KHOSLA_HOUSE, 'A.N. Khosla house'),
    (KHOSLA_INTERNATIONAL_HOUSE, 'Khosla international house (stay)'),
    (VIDYASAGAR_BHAWAN, 'Vidyasagar bhawan')
)

# Guest houses
# https://www.iitr.ac.in/campus_life/pages/Guest_Houses.html
NC_NIGAM_VISITOR_HOSTEL = 'ncn'
FACULTY_HOME = 'fah'
KHOSLA_INTERNATIONAL_HOUSE = 'khg'
GUEST_HOUSES = (
    (NC_NIGAM_VISITOR_HOSTEL, 'N.C. Nigam house'),
    (FACULTY_HOME, 'Faculty home'),
    (KHOSLA_INTERNATIONAL_HOUSE, 'Khosla international house (guest)'),
)

# Unclassified residences
# These residences have no official mention anywhere but are known to exist
VIGYAN_BHAWAN = 'vib'
VIKAS_NAGAR = 'vik'
NITI_NAGAR = 'nit'
JAI_KRISHNA_HOUSE = 'jkh'
OLD_TEACHERS_HOSTEL = 'oth'
SHIVALIK_APARTMENTS = 'shi'
HILL_VIEW_APARTMENTS = 'hva'
FACULTY_RESIDENCES = 'far'
DOCTORAL_RESIDENCES = 'doc'
UNCLASSIFIED_RESIDENCES = (
    (VIGYAN_BHAWAN, 'Vigyan bhawan'),
    (VIKAS_NAGAR, 'Vikas nagar'),
    (NITI_NAGAR, 'Niti nagar'),
    (JAI_KRISHNA_HOUSE, 'Jai Krishna house'),
    (SHIVALIK_APARTMENTS, 'Shivalik apartments'),
    (HILL_VIEW_APARTMENTS, 'Hill view apartments'),
    (OLD_TEACHERS_HOSTEL, 'Old teachers\' hostel'),
    (FACULTY_RESIDENCES, 'Faculty residences'),
    (DOCTORAL_RESIDENCES, 'Doctoral residences'),
)

# Other
NON_RESIDENT = 'nor'
OTHER = (
    (NON_RESIDENT, 'Non-resident'),
)

RESIDENCES = (
        BOYS_HOSTELS
        + GIRLS_HOSTELS
        + MARRIED_HOSTELS
        + GUEST_HOUSES
        + UNCLASSIFIED_RESIDENCES
        + OTHER
)
