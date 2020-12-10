* Напишите запрос для отображения department name, name (first_name,
last_name), hire date, salary менеджера для всех менеджеров, чей стаж работы
составляет более 15 лет.
SELECT CONCAT(first_name,' ', last_name) AS Name, hire_date, salary,  (DATEDIFF(now(), hire_date))/365 Experience  FROM departments d JOIN employees e  ON (d.manager_id = e.employee_id)  WHERE (DATEDIFF(now(), hire_date))/365>15;

+-------------------+------------+--------+------------+
| Name              | hire_date  | salary | Experience |
+-------------------+------------+--------+------------+
| Jennifer Whalen   | 1987-09-25 |   4400 |    33.2329 |
| Michael Hartstein | 1987-09-26 |  13000 |    33.2301 |
| Den Raphaely      | 1987-07-01 |  11000 |    33.4685 |
| Susan Mavris      | 1987-09-28 |   6500 |    33.2247 |
| Adam Fripp        | 1987-07-08 |   8200 |    33.4493 |
| Alexander Hunold  | 1987-06-20 |   9000 |    33.4986 |
| Hermann Baer      | 1987-09-29 |  10000 |    33.2219 |
| John Russell      | 1987-08-01 |  14000 |    33.3836 |
| Steven King       | 1987-06-17 |  24000 |    33.5068 |
| Nancy Greenberg   | 1987-06-25 |  12000 |    33.4849 |
| Shelley Higgins   | 1987-09-30 |  12000 |    33.2192 |
+-------------------+------------+--------+------------+



* Напишите запрос для отображения первого дня месяца (в формате datetime) за
три месяца до текущего месяца. Пример:
Текущая дата: 2014-09-03 Ожидаемый результат: 2014-06-01
SELECT date(((PERIOD_ADD (EXTRACT(YEAR_MONTH  FROM CURDATE()),-3)*100)+1)) AS DATE;
+------------+
| DATE       |
+------------+
| 2020-06-01 |
+------------+


* Напишите запрос, чтобы получить первый день текущего года.
SELECT MAKEDATE(EXTRACT(YEAR FROM CURDATE()),1);


+------------------------------------------+
| MAKEDATE(EXTRACT(YEAR FROM CURDATE()),1) |
+------------------------------------------+
| 2020-01-01                               |
+------------------------------------------+

* Напишите запрос, чтобы получить текущую дату в следующем формате:
Выборочные данные : 2014-09-04 Выход: September 4, 2014
SELECT DATE_FORMAT(SYSDATE(), '%M %d, %Y') AS DATE;
SELECT DATE_FORMAT(CURDATE(),'%M %e, %Y') AS 'Current_date';
+-------------------+
| Current_date      |
+-------------------+
| December 10, 2020 |
+-------------------+


* Напишите запрос, чтобы получить имя, фамилию того, кто присоединился в
июне.
SELECT CONCAT(first_name,' ', last_name) AS Name, hire_date FROM employees WHERE MONTH(HIRE_DATE) =  6;

+-------------------+------------+
| Name              | hire_date  |
+-------------------+------------+
| Steven King       | 1987-06-17 |
| Neena Kochhar     | 1987-06-18 |
| Lex De Haan       | 1987-06-19 |
| Alexander Hunold  | 1987-06-20 |
| Bruce Ernst       | 1987-06-21 |
| David Austin      | 1987-06-22 |
| Valli Pataballa   | 1987-06-23 |
| Diana Lorentz     | 1987-06-24 |
| Nancy Greenberg   | 1987-06-25 |
| Daniel Faviet     | 1987-06-26 |
| John Chen         | 1987-06-27 |
| Ismael Sciarra    | 1987-06-28 |
| Jose Manuel Urman | 1987-06-29 |
| Luis Popp         | 1987-06-30 |
+-------------------+------------+

* Напишите запрос, чтобы узнать имя, дату найма и опыт сотрудников.
SELECT FIRST_NAME, HIRE_DATE, DATEDIFF( SYSDATE(), hire_date )/365   FROM employees limit 5;

+------------+------------+--------------------------------------+
| FIRST_NAME | HIRE_DATE  | DATEDIFF( SYSDATE(), hire_date )/365 |
+------------+------------+--------------------------------------+
| Steven     | 1987-06-17 |                              33.5068 |
| Neena      | 1987-06-18 |                              33.5041 |
| Lex        | 1987-06-19 |                              33.5014 |
| Alexander  | 1987-06-20 |                              33.4986 |
| Bruce      | 1987-06-21 |                              33.4959 |
+------------+------------+--------------------------------------+

