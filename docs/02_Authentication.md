# Authentication Module

## Status

Completed

---

## Features

- User Registration
- Login
- JWT Authentication
- User Profile
- Logout
- Change Password
- Forgot Password
- Reset Password
- Refresh Token
- Token Blacklisting

---

## API Endpoints

POST /api/v1/accounts/register/

POST /api/v1/accounts/login/

POST /api/v1/accounts/logout/

POST /api/v1/accounts/token/refresh/

GET /api/v1/accounts/me/

POST /api/v1/accounts/change-password/

POST /api/v1/accounts/forgot-password/

POST /api/v1/accounts/reset-password/

---

## Business Rules

- Email must be unique.
- Password confirmation is required.
- JWT Access Token lifetime: 30 minutes.
- Refresh Token lifetime: 7 days.
- Refresh token is blacklisted on logout.
- Password reset token expires after 1 hour.

---

## Testing

All APIs tested successfully using Swagger.