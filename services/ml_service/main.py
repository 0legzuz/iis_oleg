"""Микросервис предсказаний: классификация по клиническим показателям пациента.

Локальный запуск из каталога ml_service:

    uvicorn main:app --reload

Документация и форма для тестовых запросов: http://localhost:8000/docs
"""
import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel, Field

from api_handler import FastAPIHandler
from monitoring import instrument, observe

app = FastAPI(
    title='Heart Disease Prediction Service',
    description='Сервис предсказаний модели из ЛР2 (RandomForestClassifier)',
    version='2.0',
)
app.handler = FastAPIHandler()
instrument(app)


class PatientFeatures(BaseModel):
    """Обязательные признаки пациента с примерами для Swagger."""

    age: int = Field(..., examples=[63], description='Возраст, лет')
    sex: int = Field(..., examples=[1], description='Пол: 1 — мужской, 0 — женский')
    cp: int = Field(..., examples=[3], description='Тип боли в груди: 0–3')
    trestbps: int = Field(..., examples=[145], description='Давление в покое, мм рт. ст.')
    chol: int = Field(..., examples=[233], description='Холестерин, мг/дл')
    fbs: int = Field(..., examples=[1], description='Сахар натощак > 120 мг/дл: 1 — да')
    restecg: int = Field(..., examples=[0], description='Результат ЭКГ в покое: 0–2')
    thalach: int = Field(..., examples=[150], description='Максимальный пульс, уд/мин')
    exang: int = Field(..., examples=[0], description='Стенокардия при нагрузке: 1 — да')
    oldpeak: float = Field(..., examples=[2.3], description='Депрессия сегмента ST')
    slope: int = Field(..., examples=[0], description='Наклон сегмента ST: 0–2')
    ca: int = Field(..., examples=[0], description='Число крупных сосудов: 0–3')
    thal: int = Field(..., examples=[1], description='Результат теста с таллием: 1–3')


@app.get('/')
def root():
    return {'Hello': 'World'}


@app.post('/api/prediction')
def make_prediction(item_id: int, item_features: PatientFeatures):
    """Предсказание класса для одного пациента."""
    features = item_features.model_dump()
    prediction = app.handler.predict(features)
    probability = round(app.handler.predict_proba(features), 4)
    observe(prediction, features['age'])
    return {
        'item_id': item_id,
        'predict': prediction,
        'probability': probability,
    }


if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8000)
