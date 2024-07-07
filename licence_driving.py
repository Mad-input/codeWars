"""
Task:
The UK driving number is made up from the personal details of the driver. The individual letters and digits can be code using the below information
Rules

1–5: los primeros cinco caracteres del apellido (rellenados con 9 si tiene menos de 5 caracteres) x

6: El dígito de la década del año de nacimiento (por ejemplo, para 1987 sería 8) x

7–8: el mes de nacimiento (séptimo carácter incrementado en 5 si el conductor es mujer, es decir, 51–62 en lugar de 01–12) x

9–10: la fecha dentro del mes de nacimiento x

11: El dígito del año de nacimiento (por ejemplo, para 1987 sería 7) x

12-13: las dos primeras iniciales del nombre y segundo nombre, completadas con un 9 si no hay segundo nombre x

14: Dígito arbitrario; normalmente 9, pero disminuido para diferenciar a los conductores que tienen los primeros 13 caracteres en común. Siempre usaremos 9 

15-16: dos dígitos de control de computadora. Siempre usaremos "AA"

data = ["John","James","Smith","01-Jan-2000","M"]
Where the elements are as follows

0 = Forename
1 = Middle Name (if any)
2 = Surname
3 = Date of Birth (In the format Day Month Year, this could include the full Month name or just shorthand ie September or Sep)
4 = M-Male or F-Female
"""

def driver(data):
    months = {
    "Jan": '01',
    "Feb": '02',
    "Mar": '03',
    "Apr": '04',
    "May": '05',
    "Jun": '06',
    "Jul": '07',
    "Aug": '08',
    "Sep": '09',
    "Oct": '10',
    "Nov": '11',
    "Dec": '12'
    }
    firts_name = data[0]
    last_name = data[1]
    surname= data[2]
    birth = data[3]
    month_day = birth[:-5].split('-')
    prefix = month_day[1][:3]
    month = months[prefix]
    day = month_day[0]
    year = birth[-4:]
    genre = data[4]
    
    
    if(genre == 'F'):
        month = int(month) + 50
        month_day[1] = month
    
    if len(last_name)< 1:
        last_name = '9'
        
    return f"{surname[:5].ljust(5,'9')}{int(float(year[-2:]) / 10)}{str(month)}{day}{year[-1]}{firts_name[0]}{last_name[0]}9aa".upper()
    
data = ["Johanna", "", "Gibbs", "13-Dec-1981", "F"]
print(driver(data))  



#GIBBS862131J99AA
#GIBBS812131J99AA

