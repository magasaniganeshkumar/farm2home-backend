# Location Module

## Status

Completed

---

## Purpose

Stores customer delivery addresses.

---

## Features

- Create Location
- List Locations
- Retrieve Location
- Update Location
- Soft Delete Location

---

## API Endpoints

GET /api/v1/locations/

POST /api/v1/locations/

GET /api/v1/locations/{id}/

PATCH /api/v1/locations/{id}/

DELETE /api/v1/locations/{id}/

---

## Business Rules

- Users can only access their own locations.
- One default address per user.
- Soft delete is used instead of permanent deletion.

---

## Model Fields

- UUID
- Display Name
- Contact Person
- Contact Number
- House Number
- Street
- Landmark
- Locality
- City
- District
- State
- Country
- Postal Code
- Latitude
- Longitude
- Delivery Instructions
- Default Address
- Active Status

---

## Testing

All CRUD APIs tested successfully using Swagger.