# Алгоритмическая задача "ЛИФТ"

## Задание    
Тридцатого декабря все сотрудники известной IT-компании отправляются праздновать Новый год! 
На парковке офиса сотрудников уже ожидают автобусы, чтобы отвезти их в ресторан. 
Известно, что на i-м этаже работает a<sub>i</sub> сотрудников, а парковка расположена на нулевом этаже. 
Изначально лифт расположен на этаже с парковкой. 
Какое минимальное количество времени лифт будет перевозить всех людей на парковку? 
Известно, что лифт движется со скоростью один этаж в секунду, а посадка и высадка происходит мгновенно.


## Формат ввода:
В первой строке дано единственное целое число k(1 ≤ k ≤ 10<sup>9</sup>)  — количество людей, которое вмещает лифт за одну поездку. 
Во второй строке дано единственное целое число n  — количество этажей в здании. 
В следующих n(1 ≤ n ≤ 10<sup>5</sup>) строках дано по одному целому неотрицательному числу a<sub>i</sub>(0≤ a<sub>i</sub> ≤ 10<sup>9</sup>), которое обозначает количество сотрудников на этаже номер i.

## Формат вывода:
Выведите единственное целое число  — минимальное количество секунд, которое необходимо, чтобы все сотрудники оказались на парковке. 