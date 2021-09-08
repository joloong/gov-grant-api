# Government Grant Disbursement API

## Development

Setting Up

```
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

Setting Up Database

```
flask db migrate
flask db upgrade
```

Creating .env in root folder

```
echo DATABASE_URI=<your-database-uri> > .env
```

Starting Up Development Server

```
FLASK_APP=app.py FLASK_ENV=development flask run
```

## Endpoints

1. Create Household

   - `POST /household`

2. Add a family member to household

   - `POST /household/<household_id>/member`

3. List households

   - `GET /household`

4. Show household

   - `GET /household/<household_id>`

5. Search for households and recipients of grant disbursement endpoint.

   - `GET /bonus/<bonus_type>`

6. Delete household (TODO)

   - `DELETE /household`

7. Delete family member
   - `DELETE /household/<household_id>/member/<member_id>`
