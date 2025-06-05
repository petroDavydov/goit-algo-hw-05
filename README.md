###### goit-algo-hw-05
 * Search algorithms/Алгоритми пошуку


# ВИСНОВКИ ЩО ДО НАДАНИХ РЕЗУЛЬТАТІВ ПО РОБОТІ АЛГОРИТМІВ


#### В даних обчисленнях використовувалися патерни слів 'qwerty' та 'дослідження'. Подивимось на результати роботи алгоритмів, наведених нижче.

* РЕЗУЛЬТАТИ РОБОТИ АЛГОРИТМІВ

  - article1.txt

##### Pattern: 'qwerty'

 - KMP did not find the pattern in 0.00201250 seconds
 - Boyer-Moore did not find the pattern in 0.00146460 seconds
 - Rabin-Karp did not find the pattern in 0.00460880 seconds


##### Pattern: 'дослідження'

 - KMP did not find the pattern in 0.00202940 seconds
 - Boyer-Moore did not find the pattern in 0.00064460 seconds
 - Rabin-Karp did not find the pattern in 0.00577700 seconds

--- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- 

  - article2.txt 

##### Pattern: 'qwerty'

 - KMP did not find the pattern in 0.00237550 seconds        
 - Boyer-Moore did not find the pattern in 0.00193410 seconds
 - Rabin-Karp did not find the pattern in 0.00786010 seconds


##### Pattern: 'дослідження'

 - KMP found at index 238 in 0.00006870 seconds
 - Boyer-Moore found at index 238 in 0.00003850 seconds
 - Rabin-Karp found at index 238 in 0.00017570 seconds


## Висновки


#### Боер-Мур - найшвидший --> добре працює на довгих текстах.

#### КМП - середній по швидкості --> ефективний при великому патерні.

#### Рабін-Карп - залежність від хешування та додатково якщо відсутній патерн, робить його в нашому дослідженні найповільнішим.


###### П.С. також проводились дослідження з довгими рядками, які допомогли упевнитись у деяких моментах роботи алгоритмів. Данні по додатковим дослідженням сюди не вносились.