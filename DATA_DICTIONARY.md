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

### MSIC Lookup

| Division (2 Digit) | Description |
|----------|--------|
| 06 | Extraction of crude petroleum and natural gas |
| 10 | Manufacture of food products |
| 11 | Manufacture of beverages |
| 12 | Manufacture of tobacco products |
| 13 | Manufacture of textiles |
| 14 | Manufacture of wearing apparel |
| 15 | Manufacture of leather and related products |
| 16 | Manufacture of wood and of products of woord and cork, except funiture |
| 17 | Manufacture of paper and paper products |
| 18 | Priniting and reproduction of recorded media |
| 19 | Manufacture of coke and refined petroleum products |
| 20 | Manufacture of chemicals and chemical products |
| 21 | Manufacture of basic pharmaceutical products and pharmaceutical preparations | 
| 22 | Manufacture of rubber and plastics products |
| 23 | Manufacture of other non-metallic mineral products |
| 24 | Manufacture of basic metals |
| 25 | Manufacture of fabricated metal products, except machinery and equipment |
| 26 | Manufacture of computer, electronic and optical products |
| 27 | Manufacture of electrical equipment |
| 28 | Manufacture of machinery and equipment n.e.c. |
| 29 | Manufacture of motor vehicles, trailers and semi-trailers | 
| 30 | Manufacture of other transport equipment |
| 31 | Manufacture of furniture |
| 32 | Other manufacturing |
| 33 | Repair and installation of machinery and equipment |
| 35 | 	Electricity, gas, steam and air conditioning supply |