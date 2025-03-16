# Data Fusion Contest 2025 - Label Craft (Baseline_v0)

![image](https://github.com/user-attachments/assets/b48cc238-a2c7-4dce-9fa9-2abac4e151d5)

### Описание
Этот репозиторий содержит базовое решение (Baseline_v0) для задачи 1 "Label Craft" соревнования [Data Fusion Contest 2025](https://ods.ai/competitions/data-fusion2025-labelcraft).

### Структура проекта

- **baseline_publick_v0.ipynb** - ноутбук с бейзлайном для классификации, использующий TF-IDF и SGDClassifier.
- **sample_submit/** - папка с примером сабмита для baseline_publick_v0.ipynb.
- **Labeled_Qwen2.5-7B-Lite-Beta.ipynb** - ноутбук с примером доразметки данных из `unlabeled_train` при помощи модели Qwen2.5-7B-Instruct.

### Разметка с помощью Qwen2.5-7B-Instruct
Для доразметки данных используется большая языковая модель **Qwen2.5-7B-Instruct**, которая поднимается локально как сервер с помощью библиотеки **vLLM** и взаимодействует через API **openai**.

Основная идея: LLM размечает датасет по дереву категорий, дополняя исходные данные для улучшения качества классификации.

### Ссылки
- **Соревнование**: [Data Fusion Contest 2025 - Label Craft](https://ods.ai/competitions/data-fusion2025-labelcraft)

