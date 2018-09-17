# Задача бинарной классификации по записи стихотворения

**Цель**: дан текст и запись его чтения носителем языка. Требуется научиться по записи .wav определяет читают ли данное стихотворение или запись сожержит что-то другое.

## Датасет

Для решения задачи был составлен маленький датасет с метками `Good` и `Bad`. Под первой меткой лежат записи чтения данного стихотворения. Под второй меткой лежат записи других стихотворений. Также есть 5 независимых тестовых записей (`Test`) одна из которых - эталонное чтение носителя языка.

## Обучение модели

Для создания моделей использовалась библиотека `pyAudioAnalysis`. Она создана на основе Scikit Learn. pip3 библиотеку не поставить. Надо напрямую скачать все скрипты с https://github.com/tyiannak/pyAudioAnalysis/.  В дальнейшем все скрипты будут запускаться из папки ./pyAudioAnalysis. Не самый оптимальный метод, но годится.

Модель обучаем с помощью скрипта ***model_builder.py***. Скрипт создает на основе датасета сразу 5 моделей: K Nearest Neighbours, Support Vector Machine, Random Forest, Extratrees, Gradient Boosting. Однако можно ограничиться только KNN. Модели сохраняются в рабочую папку.

### Тестирование модели

Для этой цели написан скрипт PoemClassifier.py. Он принимает имена файлов в качестве аргументов командной строки и классифицирует их по 5 моделям. Потом берется средняя оценка. Было установлено, что 0.5 - пограничное значение, при котором правильно определяется эталонный текст.
