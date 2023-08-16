OFF = 0
AUTO = 1
INCANDESECENT = 2 
FLUORESCENT = 3
WARM_FLUORESCENT = 4 
DAYLIGHT = 5
CLOUDY_DAYLIGHT = 6 
TWILIGHT = 7
SHADE = 8
MANUAL = 9

wbmode_choices = (
        ('OFF','Off'),
        ('AUTO','auto'),
        ('INCANDESECENT','incandescent'),
        ('FLUORESCENT','fluorescent'),
        ('WARM_FLUORESCENT','warm-fluorescent'),
        ('DAYLIGHT','daylight'),
        ('CLOUDY_DAYLIGHT','cloudy-daylight'),
        ('TWILIGHT','twilight'),
        ('SHADE','shade'),
        ('MANUAL','manual'),
    )
saturation_choices = (
    (0,0),
    (1,1),
    (2,2),
    )
sensor_id_choices = (
    (0,0),
    (1,1),
    )


NOISEREDUCTION_OFF = 0
NOISEREDUCTION_FAST = 1
NOISEREDUCTION_HIGHQUALITY = 2

tnr_mode_choices = (
    ('NOISEREDUCTION_OFF','NoiseReduction_Off'),
    ('NOISEREDUCTION_FAST','NoiseReduction_Fast'),
    ('NOISEREDUCTION_HIGHQUALITY','NoiseReduction_HighQuality'),
    )


EDGEENHANCEMENT_OFF = 0
EDGEENHANCEMENT_FAST = 1
EDGEENHANCEMENT_HIGHQUALITY = 2

ee_mode_choices = (
    ('EDGEENHANCEMENT_OFF','EdgeEnhancement_Off'),
    ('EDGEENHANCEMENT_FAST','EdgeEnhancement_Fast'),
    ('EDGEENHANCEMENT_HIGHQUALITY','EdgeEnhancement_HighQuality'),
    )

AEANTIBANDINGMODE_OFF = 0
AEANTIBANDINGMODE_AUTO = 1
AEANTIBANDINGMODE_50HZ = 2
AEANTIBANDINGMODE_60HZ = 3

aeantibanding_choices = (
    ('AEANTIBANDINGMODE_OFF','AeAntibandingMode_Off'),
    ('AEANTIBANDINGMODE_AUTO','AeAntibandingMode_Auto'),
    ('AEANTIBANDINGMODE_50HZ','AeAntibandingMode_50HZ'),
    ('AEANTIBANDINGMODE_60HZ','AeAntibandingMode_60HZ'),
    )


