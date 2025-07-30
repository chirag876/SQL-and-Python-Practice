-- Given the CITY and COUNTRY tables, query the names of all the continents (COUNTRY.Continent) and their respective average city populations (CITY.Population) rounded down to the nearest integer.

-- Note: CITY.CountryCode and COUNTRY.Code are matching key columns.

Solution:
SELECT country.Continent, FLOOR(AVG(city.Population)) AS AvgPopulation
FROM city
JOIN country ON city.CountryCode = country.Code
GROUP BY country.Continent;
