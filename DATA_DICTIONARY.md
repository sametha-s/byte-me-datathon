# Data Dictionary

### Dataset: IPI by Division (2 digit)
Real output of the three main industrial sectors by MSIC division (2 digit).

*Source:* Department of Statistics Malaysia (OpenDOSM)\
*Link:* https://open.dosm.gov.my/data-catalogue/ipi_2d 

### Raw dataset variables
| Variable | Type | Definition |
|----------|------|------------|
|`series` | String | Series type; absolute values (`abs`), year-on-year growth (`growth_yoy`), month-on-month growth (`growth_mom`) |
|`date` | Date | Date in YYYY-MM-DD (DD set to 01) |
|`division`| String | 2-digit code (match with MSIC Lookup)|
| `index` | Float | Quantity of output |

### Dataset Range