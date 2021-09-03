# Анализ алгоритмов

1. 


АА 7 лаб + домашка

(Перестронин (Justarone))(7 лаб + дз) https://github.com/Justarone/bmstu-aa

(Якуба (TheSawIsTheLaw))(7 лаб + ДЗ) https://github.com/TheSawIsTheLaw/AlgorithmAnalysis

(Кононенко (hackfeed))(7 лаб + дз) https://github.com/hackfeed/aa-5th-sem-labs

(Богаченко (SpectralOne))(7 лаб + дз) https://github.com/SpectralOne/bmstu-aa

(Wilsem)(7 лаб) https://github.com/bmstu-ics7/analysis-of-algorithms/tree/65e04908c9ce1326ffed9d51285f9fa9d664fd9b

(PYTHON Sunshine-ki )(7 лаб+дз+шаблон отчета) https://github.com/Sunshine-ki/BMSTU5_AA

(Winterpuma (оберган))(7 лаб и еще CalcWork) https://github.com/Winterpuma/bmstu_AA/tree/master

(medva1997 (давнииий))(1, 2 лабы) https://github.com/medva1997/bmstu_sem5/tree/master/AA

(TinyMarcus)(7 лаб) https://github.com/TinyMarcus/analysis

(Романов (mRrvz))(7 лаб и ДЗ) https://github.com/mRrvz/bmstu-aa

(NastyRu)(7 лаб) https://github.com/NastyRu/Database

(7 лаб) https://github.com/Gr1dlock/AnalysisOfAlgorithms

(первые 4) https://github.com/Kulikov17/AA_BMSTU

(1, 2, 3) https://github.com/kuso4egdobra/Analyze_Algoritms

(Pandoral (старое))(7 лаб) https://github.com/Panda-Lewandowski/Analysis-of-algorithms

(LubaxaPro) (7 лаб) https://github.com/LyubaxaPro/analysis_of_algorithms

(7 лаб) https://github.com/ZeynalovZ/Analysis-of-algorithms



рк
рк https://github.com/Gr1dlock/AnalysisOfAlgorithms/tree/master/RK

Зачет состоит из двух частей: практическая(лабы) и теоретическая часть.
По теории был прямо зачет: лектор раздавал вопросы, покрывающие кусочки лекций и потом слушал ответы.

Хороший конспект лекций:

1 часть: https://github.com/medva1997/bmstu_sem5/blob/master/AA/AA_part1.PDF

2 часть: https://github.com/medva1997/bmstu_sem5/blob/master/AA/AA_part2.PDF

В нем можно найти ответы на вопросы, которые сложно загуглить :)












*Преподаватель: Лилия Леонидовна Волкова (504 л, liliya@bmstu.ru)*

8 лабораторных работ. 

**Плюшки:** сдай 4 лабы до 8 недели и получи РК1 автоматом, делай все лабы в LaTex и освободись от 8 лабы

## Лабораторная 1: расстояние Левенштейна и Дамерау-Левенштейна

* расстояние Левенштейна - матрично
* расстояние Дамерау-Левенштейна - рекурсивно
* расстояние Левенштейна - рекурсивно без кеша
* расстояние Левенштейна - рекурсивно с кешем


- Сравнивать ПРОЦЕССОРНОЕ время, для строк разной длины: 10 - 50/100 с шагом 10, среднее из нескольких измерений, можно попарно или вместе
- сравнивать, сколько памяти выделилось МАКСИМУМ (а не всего)
- 2 режима: пользовательский (ввод собственных строк) и экспериментальный (для замера времени)

## Требования к отчету:

 * Анонс до рисунка или таблицы. Таблицы - свсерху ссправа, листинг - сверху слева, 
 * На каждый источник должна быть ссыллка `[1]`
 * Если введение начинается с :, то в списке  с маленькой буквы и запятыми
 
 
* cостав: титульник, оглавление (автоматическое), введение (применение динамического программирования на материале расстояния Левенштейна и Дамерау-Левенштейна
), содержание, заключение (ОЧЕНЬ ВАЖНО, связанное с началом - цели и задачи. Кратко: что сделали, цель достигнута, выполнены все задачи: и список задач), список литературы (не википедия и не препод)
* цель: получить навык динамического программирования
* задачи: 
* - изучить расстояние Левенштейна и Дамерау-Левенштейна
* - разработать алгоритмы поиска расстояния Левенштейна и Дамерау-Левенштейна
* - реализовать вышеперечисленные алгоритмы
* - провести сравнительный анализ процессорного времени выполнения реализаций этих алгоритмов
* - провести сравнительный анализ пиковой затраченной реализованными алгоритмами памяти
* - выбрать "любимую" реализацию


* Левенштейна и Дамерау-Левенштейна между собой можно сравнивать только в терминах "затрачено больше времени", а лучше/хуже - нельзя



Всего 4 главы:
1. Аналитическая: 
теория, применение, стандартная математика, обзор, выбор направления

2. Конструкторская 
разработка алгоритмов и структуры программы. 
Перечисленные алгоритмы, схема алгоритмов (для рекурсивного видимо из 2 частей)

3. Технологическая
выбор языка, среды разработки, библиотек. Код, листинги, как будем замерять время и память.

4. Экспериментальная (в дипломе - исследовательская)

