# Описание проекта

Проект решает задачу **бинарной классификации**: по клиническим показателям пациента
(возраст, пол, давление, холестерин, результаты ЭКГ и нагрузочных проб) определить
значение целевой переменной `target`.

Исходная выборка: [Heart Disease Dataset](https://www.kaggle.com/datasets/krishujeniya/heart-diseae)
(Cleveland Heart Disease, репозиторий UCI) — 303 записи, 13 признаков.

# Запуск

Для запуска проекта под ОС GNU/Linux необходимо выполнить команды:

```shell
git clone <адрес репозитория>
cd heart-disease-classification
python3 -m venv .venv_heart
source .venv_heart/bin/activate
python3 -m pip install -r requirements.txt
```

Активация виртуального окружения:

```shell
source .venv_heart/bin/activate
```

Деактивация:

```shell
deactivate
```

Запуск Jupyter для работы с блокнотом:

```shell
jupyter notebook eda/eda.ipynb
```

### Данные

Файлы с данными в репозиторий не коммитятся. Перед запуском блокнота нужно скачать
датасет и положить его в директорию `./data/` под именем `heart.csv`:

```shell
mkdir -p data
curl -o data/heart.csv https://raw.githubusercontent.com/kb22/Heart-Disease-Prediction/master/dataset.csv
```

> Для пересохранения интерактивного графика в PNG библиотеке `kaleido` нужен браузер
> на движке Chromium. Если он не установлен, выполните `plotly_get_chrome`.
> Сам блокнот при этом читается и без него — графики уже сохранены в `./eda/`.

# Структура проекта

```
.
|__ data/                            исходные и обработанные данные (не коммитятся)
|    |__ heart.csv                   исходный датасет
|    |__ clean_data.pkl              очищенная выборка
|__ eda/
|    |__ eda.ipynb                   блокнот с разведочным анализом
|    |__ numeric_boxplot.html        интерактивный график (plotly)
|    |__ *.png                       сохранённые графики
|__ .gitignore
|__ README.md
|__ requirements.txt
```

# Исследование данных

В работе.
