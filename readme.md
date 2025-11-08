
# 🛒 Backend de Tienda - Django REST Framework

Este proyecto implementa un backend en **Django + Django REST Framework** para la gestión de usuarios, tipos de documentos, productos y compras.  
Incluye autenticación de usuarios, registro de productos y la consulta de compras por documento de identidad.

---

## 🚀 Características principales

- 🔐 Registro y login de usuarios (autenticación por token o JWT)
- 🪪 Gestión de tipos de documento (Cédula, Pasaporte, etc.)
- 🧾 Registro de productos con precio
- 💰 Creación de compras con productos asociados
- 🔍 Consulta de compras por documento de identidad del cliente
- 🧮 Cálculo automático del total de cada compra

---

## 🧩 Estructura del proyecto

```markdown

apps/
├── users/
│    ├── api/
│    ├── models/
│    ├── serializers/
│    ├── admin.py
│    └── apps.py
│
├── document_type/
│    ├── api/
│    ├── models/
│    ├── serializers/
│    ├── admin.py
│    └── apps.py
│
├── product/
│    ├── api/
│    ├── models/
│    ├── serializers/
│    ├── admin.py
│    └── apps.py
│
├── purchase/
│    ├── api/
│    ├── models/
│    ├── serializers/
│    ├── admin.py
│    └── apps.py
│
├── core/
│    ├── models/
│    │     └── base_model.py
│    ├── permissions/
│    │     └── permissions.py
│    ├── utils/
│
├── manage.py

````

---

## ⚙️ Instalación

### 1️⃣ Clonar el repositorio

```bash
git clone git@github.com:fabioCordoba/PruebaTecnicaFalabella-.git
cd backend
````

### 2️⃣ Crear y activar entorno virtual

```bash
python -m venv venv
source venv/bin/activate   # En Windows: venv\Scripts\activate
```

### 3️⃣ Instalar dependencias

```bash
pip install -r requirements.txt
```

### 4️⃣ Configurar variables de entorno

Crea un archivo `.env` en la raíz del proyecto con:

```
SECRET_KEY=tu_clave_secreta
DEBUG=True
ALLOWED_HOSTS=*
DATABASE_URL=sqlite:///db.sqlite3
```

### 5️⃣ Migrar base de datos

```bash
python manage.py makemigrations
python manage.py migrate
```

### 6️⃣ Crear superusuario

```bash
python manage.py createsuperuser
```

### 7️⃣ Iniciar servidor

```bash
python manage.py runserver
```

---

### 8️⃣ Accede a la documentacion

```bash
http://127.0.0.1:8000/docs/
```

### 9️⃣ Accede a produccion

* Api Rest : https://backendfalabella.fabiocordoba.me/
* Docuementacion Swagger: https://backendfalabella.fabiocordoba.me/docs/
* Admin Django: https://backendfalabella.fabiocordoba.me/admin/

###  credenciales para el admin 
```json
{
  "email": "fabiocordoba1@gmail.com",
  "password": "admin"
}
```

---

## 👤 Usuarios (Registro y Login)

### 🔹 Registro de usuario

**POST** `/api/users/register/`

#### Body:

```json
{
  "username": "fabio",
  "email": "fabio@example.com",
  "password": "123456",
  "first_name": "Fabio",
  "last_name": "Cordoba"
}
```

#### Respuesta:

```json
{
  "id": 1,
  "username": "fabio",
  "email": "fabio@example.com"
}
```

---

### 🔹 Login

**POST** `/api/users/login/`

#### Body:

```json
{
  "email": "fabiocordoba1@gmail.com",
  "password": "admin"
}
```

#### Respuesta:

```json
{
    "refresh": "eyJhbGci...",
    "access": "eyJhbGciOi",
    "user": {
        "id": "300133bd-2193-4ebf-9039-05ec355cd823",
        "email": "fabiocordoba1@gmail.com",
        "username": "admin",
        "first_name": "",
        "last_name": "",
        "rol": "administrator",
        "image": null,
        "is_active": true
    }
}
```

---

## 🪪 Tipos de documento

### 🔹 Crear tipo de documento

**POST** `/api/documents/`

#### Body:

```json
{
  "name": "Cédula de Ciudadanía",
  "short_name": "CC"
}
```

#### Respuesta:

```json
{
  "id": 1,
  "name": "Cédula de Ciudadanía",
  "short_name": "CC"
}
```

---

## 🧾 Productos

### 🔹 Registrar producto

**POST** `/api/products/`

#### Body:

```json
{
  "name": "Laptop Dell XPS 13",
  "description": "Ultrabook potente con procesador Intel i7",
  "price": 5200.00
}
```

#### Respuesta:

```json
{
  "id": 1,
  "name": "Laptop Dell XPS 13",
  "price": "5200.00"
}
```

---

## 💰 Compras

### 🔹 Crear compra

**POST** `/api/purchases/`

#### Body:

```json
{
  "user": 1,
  "products": [
    { "product_id": 1, "quantity": 2 },
    { "product_id": 3, "quantity": 1 }
  ]
}
```

#### Respuesta:

```json
{
  "id": 1,
  "code": "FAB-87239",
  "user": "fabio",
  "total": "10400.00",
  "created_at": "2025-10-28T15:00:00Z"
}
```

---

## 🔍 Buscar compras por documento de identidad

### Endpoint

**GET** `/api/purchases/search/?document_number=123456789`

#### Respuesta:

```json
[
  {
    "code": "FAB-87239",
    "user": "fabio",
    "total": "10400.00",
    "products": [
      { "name": "Laptop Dell XPS 13", "quantity": 2, "price": 5200.00 }
    ]
  }
]
```

---

## 🛠 Tecnologías usadas

* [Django 5.x](https://www.djangoproject.com/)
* [Django REST Framework](https://www.django-rest-framework.org/)
* [djangorestframework-simplejwt](https://django-rest-framework-simplejwt.readthedocs.io/en/latest/)
* [SQLite / PostgreSQL](https://www.postgresql.org/)
* Python 3.11+

---

## 🧩 Frontend – Consulta de Compras

Esta aplicación frontend, desarrollada con **Angular 20**, permite consultar las compras registradas de un cliente a través de su documento de identidad.
El sistema consume los endpoints del backend desarrollados en **Django REST Framework**, encargados de gestionar los tipos de documento y las compras asociadas a cada usuario.

### 🚀 Funcionalidades principales

* **Listado de tipos de documento:**
  La aplicación consume el endpoint `/api/document_type/` para mostrar las opciones disponibles (por ejemplo: Cédula de Ciudadanía, Pasaporte, etc.).

* **Búsqueda de compras por documento:**
  Permite al usuario ingresar su tipo y número de documento para consultar las compras asociadas, a través del endpoint `/api/purchases/by_document/`.

### 🧠 Tecnologías utilizadas

* **Angular 20.3.9** con componentes standalone y signals.
* **TypeScript** y **RxJS** para manejo reactivo de datos.
* **HTTPClient** para la comunicación con el backend.
* **Docker + Nginx** para despliegue en producción.

### 🌐 Despliegue

La aplicación se encuentra desplegada y accesible públicamente en:
🔗 [https://frontendfalabella.fabiocordoba.me](https://frontendfalabella.fabiocordoba.me)

### ⚙️ Flujo de uso

1. El usuario accede a la aplicación web.
2. Selecciona su tipo de documento desde el menú desplegable.
3. Ingresa su número de documento.
4. Al presionar **Buscar**, el sistema consulta el backend y muestra las compras registradas.

## 🧑‍💻 Autor

**Fabio Córdoba**
📧 [fabiocordoba1@gmail.com](fabiocordoba1@gmail.com)
💼 [LinkedIn](https://linkedin.com/in/fabiocordoba)
💻 Desarrollador Backend | Django | API REST | Automatización

---


