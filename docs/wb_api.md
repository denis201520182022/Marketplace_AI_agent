# Официальная спецификация Wildberries API: Отзывы, Вопросы и Карточки товаров

Данный документ содержит полную техническую информацию, необходимую для разработки интеграционного коннектора Wildberries в проекте AI-агента для селлеров маркетплейсов.

---

## 1. Базовые параметры и авторизация

### 1.1. Базовые URL (Endpoints)
* **Production API (Боевой сервер):**
  * Отзывы и вопросы: `https://feedbacks-api.wildberries.ru`
  * Контент и карточки товаров: `https://content-api.wildberries.ru`
* **Sandbox API (Тестовый контур):**
  * `https://feedbacks-api-sandbox.wildberries.ru`

### 1.2. Получение токена селлера
1. Селлер авторизуется в личном кабинете Wildberries: [seller.wildberries.ru](https://seller.wildberries.ru/).
2. Переходит: *«Профиль» ➔ «Настройки» ➔ «Доступ к API»*.
3. Создаёт новый токен со следующими обязательными областями доступа (категориями):
   * **«Отзывы и вопросы»** (Customer communication) — права на чтение и запись.
   * **«Контент»** (Content) — права на чтение карточек товаров.
4. Срок действия токена задаётся селлером (рекомендуется бессрочный или на 1 год).

### 1.3. Передача токена в запросах
Токен передаётся в заголовке каждого HTTP-запроса:
```http
Authorization: <ТОКЕН_СЕЛЛЕРА>
Content-Type: application/json
```
*(Также поддерживается заголовок `HeaderApiKey: <ТОКЕН_СЕЛЛЕРА>`, но стандартным является `Authorization`).*

### 1.4. Ограничения частоты запросов (Rate Limiting)
* Для категории «Вопросы и отзывы»: стандартно **до 3 запросов в секунду** на один токен, с допустимым кратковременным всплеском до 6 rps.
* При превышении лимита API возвращает HTTP-статус **`429 Too Many Requests`**.
* Коннектор обязан реализовывать паттерн **Token Bucket / Leaky Bucket** в Redis с экспоненциальной задержкой (Exponential Backoff).

---

## 2. API Отзывов (Feedbacks API)

Базовый хост: `https://feedbacks-api.wildberries.ru`

### 2.1. Получение списка отзывов
**Метод:** `GET /api/v1/feedbacks`

#### Параметры запроса (Query Parameters):
| Параметр | Тип | Обязательный | Описание |
| :--- | :--- | :--- | :--- |
| `isAnswered` | `boolean` | **Да** | `false` — получить новые неотвеченные отзывы, `true` — уже обработанные |
| `take` | `integer` | **Да** | Количество запрашиваемых отзывов (от 1 до 5000) |
| `skip` | `integer` | **Да** | Смещение пагинации (для первой страницы `0`) |
| `order` | `string` | Нет | Сортировка по дате: `dateAsc` (сначала старые) или `dateDesc` (сначала новые) |
| `nmId` | `integer` | Нет | Артикул WB конкретного товара для фильтрации |
| `dateFrom` | `integer` | Нет | Unix timestamp начала периода |
| `dateTo` | `integer` | Нет | Unix timestamp конца периода |

#### Пример запроса:
```http
GET /api/v1/feedbacks?isAnswered=false&take=100&skip=0&order=dateDesc HTTP/1.1
Host: feedbacks-api.wildberries.ru
Authorization: eyJhbGciOi...
```

#### Пример успешного ответа (`200 OK`):
```json
{
  "data": {
    "countUnanswered": 14,
    "countArchive": 150,
    "feedbacks": [
      {
        "id": "YX52RZEBhH9mrcYdEJuD",
        "text": "Наушники отличные, играют чисто, басы на высоте!",
        "pros": "Качественный звук, приятный пластик",
        "cons": "Коробка была немного помята при доставке",
        "productValuation": 5,
        "createdDate": "2026-10-17T14:32:01Z",
        "answer": null,
        "state": "none",
        "productDetails": {
          "nmId": 18274619,
          "imtId": 12893847,
          "productName": "Беспроводные наушники Pro",
          "supplierArticle": "HEADPHONE-PRO-BLACK",
          "brandName": "SoundMaster"
        },
        "video": null,
        "photo": [
          {
            "fullSize": "https://feedbackphotos.wb.ru/...",
            "minSize": "https://feedbackphotos.wb.ru/..."
          }
        ],
        "userName": "Александр",
        "matchingSize": "ok",
        "isWasViewed": false
      }
    ]
  },
  "error": false,
  "errorText": ""
}
```

---

### 2.2. Отправка ответа на отзыв
**Метод:** `POST /api/v1/feedbacks/answer`

#### Заголовки:
```http
Authorization: <ТОКЕН>
Content-Type: application/json
```

#### Тело запроса (JSON Body):
```json
{
  "id": "YX52RZEBhH9mrcYdEJuD",
  "text": "Здравствуйте, Александр! Благодарим за высокую оценку нашего товара. Рады, что вы оценили качество звучания. Приятного использования!"
}
```

#### Поля запроса:
* `id` (`string`, обязательное) — уникальный идентификатор отзыва из `GET /api/v1/feedbacks`.
* `text` (`string`, обязательное) — текст ответа селлера (от 2 до 1000 символов).

#### Ответ сервера:
* При успехе: `200 OK`
```json
{
  "data": null,
  "error": false,
  "errorText": ""
}
```
* При ошибке (например, отзыв уже отвечен или не существует): `400 Bad Request` или `404 Not Found`.

---

### 2.3. Редактирование ранее отправленного ответа
**Метод:** `PATCH /api/v1/feedbacks/answer`

#### Тело запроса (JSON Body):
```json
{
  "id": "YX52RZEBhH9mrcYdEJuD",
  "text": "Здравствуйте, Александр! Исправленный вариант ответа..."
}
```
*(Селлер может отредактировать опубликованный ответ в течение ограниченного времени).*

---

### 2.4. Получение количества неотвеченных отзывов
**Метод:** `GET /api/v1/feedbacks/count-unanswered`
Используется воркером для быстрой проверки наличия новых событий без выгрузки всего списка.

---

## 3. API Вопросов (Questions API)

Базовый хост: `https://feedbacks-api.wildberries.ru`

### 3.1. Получение списка вопросов
**Метод:** `GET /api/v1/questions`

#### Параметры запроса (Query Parameters):
| Параметр | Тип | Обязательный | Описание |
| :--- | :--- | :--- | :--- |
| `isAnswered` | `boolean` | **Да** | `false` — неотвеченные вопросы, `true` — отвеченные |
| `take` | `integer` | **Да** | Количество (1–5000) |
| `skip` | `integer` | **Да** | Пагинация (0, 100, ...) |
| `order` | `string` | Нет | `dateAsc` или `dateDesc` |
| `nmId` | `integer` | Нет | Артикул товара WB |

#### Пример успешного ответа (`200 OK`):
```json
{
  "data": {
    "countUnanswered": 5,
    "countArchive": 42,
    "questions": [
      {
        "id": "J2FMRjUj6hwvwCElqssz",
        "text": "Подскажите, пожалуйста, какой разъём для зарядки: Type-C или Micro-USB?",
        "createdDate": "2026-10-17T15:10:00Z",
        "state": "none",
        "answer": null,
        "productDetails": {
          "nmId": 18274619,
          "productName": "Беспроводные наушники Pro",
          "supplierArticle": "HEADPHONE-PRO-BLACK",
          "brandName": "SoundMaster"
        },
        "wasViewed": false
      }
    ]
  },
  "error": false,
  "errorText": ""
}
```

---

### 3.2. Ответ на вопрос покупателя или отклонение
**Метод:** `PATCH /api/v1/questions`

#### Заголовки:
```http
Authorization: <ТОКЕН>
Content-Type: application/json
```

#### Вариант А: Публичный ответ на сайте (`state: "wbRu"`)
```json
{
  "id": "J2FMRjUj6hwvwCElqssz",
  "answer": {
    "text": "Здравствуйте! В данной модели используется современный разъём Type-C. Кабель для зарядки идёт в комплекте."
  },
  "state": "wbRu"
}
```

#### Вариант Б: Отклонение вопроса без публикации на сайте (`state: "none"`)
```json
{
  "id": "J2FMRjUj6hwvwCElqssz",
  "answer": {
    "text": "К сожалению, мы не можем ответить на данный вопрос."
  },
  "state": "none"
}
```

#### Поля запроса:
* `id` (`string`, обязательное) — идентификатор вопроса.
* `answer.text` (`string`, обязательное) — текст ответа селлера.
* `state` (`string`, обязательное) — `"wbRu"` (опубликовать на WB) или `"none"` (скрыть).

---

## 4. Content API: Получение актуальной карточки товара (No-cache)

Базовый хост: `https://content-api.wildberries.ru`

Чтобы ИИ-агент всегда имел актуальную информацию о характеристиках, описании и составе товара (без кэширования), используется Content API.

### 4.1. Получение карточки товара по артикулу (nmId)
**Метод:** `POST /content/v2/get/cards/list`

#### Заголовки:
```http
Authorization: <ТОКЕН>
Content-Type: application/json
```

#### Тело запроса (JSON Body):
```json
{
  "settings": {
    "sort": {
      "ascending": true
    },
    "cursor": {
      "limit": 10
    },
    "filter": {
      "withPhoto": -1,
      "textSearch": "18274619"
    }
  }
}
```
*Примечание: Поле `textSearch` принимает артикул WB (`nmId`) в виде строки, что позволяет точечно извлечь карточку.*

#### Пример ответа (`200 OK`):
```json
{
  "cards": [
    {
      "nmID": 18274619,
      "imtID": 12893847,
      "vendorCode": "HEADPHONE-PRO-BLACK",
      "title": "Беспроводные наушники SoundMaster Pro с шумоподавлением",
      "description": "Полноразмерные беспроводные наушники с активным шумоподавлением ANC. Время работы до 40 часов. Зарядка Type-C...",
      "brand": "SoundMaster",
      "characteristics": [
        {
          "id": 14177451,
          "name": "Тип разъема",
          "value": ["Type-C"]
        },
        {
          "id": 14177452,
          "name": "Время работы от аккумулятора",
          "value": ["40 ч"]
        },
        {
          "id": 14177453,
          "name": "Система активного шумоподавления (ANC)",
          "value": ["Да"]
        },
        {
          "id": 14177454,
          "name": "Гарантийный срок",
          "value": ["1 год"]
        }
      ],
      "dimensions": {
        "length": 20,
        "width": 15,
        "height": 8
      }
    }
  ],
  "cursor": {
    "updatedAt": "2026-10-10T12:00:00Z",
    "nmID": 18274619,
    "total": 1
  }
}
```

---

## 5. Типовые ошибки и обработка сбоев

| HTTP-код | Причина | Действие коннектора |
| :--- | :--- | :--- |
| `400 Bad Request` | Неверные параметры запроса или некорректный ID | Логирование ошибки, переход события в статус `ERROR` |
| `401 Unauthorized` | Токен не указан или истёк | Оповещение селлера в бот о необходимости обновить токен WB |
| `403 Forbidden` | У токена нет прав на категорию «Отзывы и вопросы» или «Контент» | Оповещение селлера о нехватке прав доступа токена |
| `429 Too Many Requests` | Превышен лимит запросов в секунду | Воркер делает паузу (Sleep backoff 2-5 сек) и повторяет запрос через очередь DLX |
| `500, 502, 503, 504` | Временный сбой на серверах Wildberries | Повтор запроса через RabbitMQ retry с экспоненциальной задержкой |
