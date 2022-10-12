drop_demographics = "DROP TABLE IF EXISTS demographics"
drop_immigrations = "DROP TABLE IF EXISTS immigrations;"
drop_airpts = "DROP TABLE IF EXISTS airpts;"
drop_temp = "DROP TABLE IF EXISTS temp;"

# CREATE TABLES

create_airpts = ("""
CREATE TABLE IF NOT EXISTS public.airpts( 
    iata_code    VARCHAR PRIMARY KEY,
    type         VARCHAR,
    name         VARCHAR,
    elevation_ft FLOAT,
    continent    VARCHAR,
    iso_country  VARCHAR,
    iso_region   VARCHAR,
    municipality VARCHAR,
    gps_code     VARCHAR,    
    local_code   VARCHAR,
    coordinates  VARCHAR,
    I94port_city    VARCHAR
    );
""") 

create_immigrations= ("""
CREATE TABLE IF NOT EXISTS public.immigrations( 
  cicid      FLOAT PRIMARY KEY,
    year     FLOAT,
    month    FLOAT,
    cit      FLOAT,
    res      FLOAT,
    iata     VARCHAR(3),
    arrdate  FLOAT,
    mode     FLOAT,
    addr     VARCHAR,
    depdate  FLOAT,
    bir      FLOAT,
    visa     FLOAT,
    count    FLOAT,
    dtadfile VARCHAR,  
    entdepa  VARCHAR(1),
    entdepd  VARCHAR(1),  
    matflag  VARCHAR(1),
    biryear  FLOAT,
    dtaddto  VARCHAR,
    gender   VARCHAR(1), 
    airline  VARCHAR,
    admnum   FLOAT,
    fltno    VARCHAR,
    visatype VARCHAR
    );
""")



create_demographics = """
CREATE TABLE IF NOT EXISTS public.demographics (
    city                   VARCHAR,
    state                  VARCHAR,
    median_age              FLOAT,
    male_population        BIGINT,
    female_population      BIGINT,
    total_population       BIGINT,
    num_of_veterans        BIGINT,
    foreign_born           BIGINT,
    average_household_size FLOAT,
    state_code             VARCHAR(2),
    race                   VARCHAR,
    count                  BIGINT
    );
"""


demographic_ins = ("""
    INSERT INTO demographics(city, state, median_age, male_population,
    female_population, total_population, num_of_veterans, foreign_born,
    average_household_size, state_code, race, count) VALUES (%s, %s, 
    %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
     ON CONFLICT DO NOTHING;
""")

create_temp = """
CREATE TABLE IF NOT EXISTS temp (
    timestamp                      DATE,
    average_temperature            FLOAT,
    average_temperature_uncertainty FLOAT,
    city                           VARCHAR,
    country                        VARCHAR,
    latitude                       VARCHAR,
    longitude                      VARCHAR
);
"""

airpt_ins = ("""
    INSERT INTO airpts (iata_code, type, name, elevation_ft, continent,
    iso_country, iso_region, municipality, gps_code, local_code,
    coordinates, I94port_city) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s,
    %s, %s, %s) 
     ON CONFLICT DO NOTHING;
""")


immigration_ins = (""" 
    INSERT INTO immigrations (cicid, year, month, cit, res, iata,
    arrdate, mode, addr, depdate, bir, visa, count, dtadfile,
    entdepa, entdepd, matflag, biryear, dtaddto, gender, airline, 
    admnum, fltno, visatype) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s) 
    ON CONFLICT DO NOTHING;
""")


temp_ins = ("""
    INSERT INTO temp (timestamp, average_temperature, average_temperature_uncertainty, city, country, 
    latitude, longitude) VALUES (%s, %s, %s, %s, %s, %s, %s) 
    ON CONFLICT DO NOTHING;
""")


drop_table_queries = [drop_airpts, drop_demographics, drop_immigrations, drop_temp]
create_table_queries = [create_airpts, create_demographics, create_immigrations, create_temp]


    
