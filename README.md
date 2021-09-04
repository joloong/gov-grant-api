# Government Grant Disbursement API

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

6. Delete household

   - `DELETE /household`

7. Delete family member
   - `DELETE /household/<household_id>/member/<member_id>`
