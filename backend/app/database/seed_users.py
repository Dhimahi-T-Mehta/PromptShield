from app.auth.password import hash_password
from app.database.users import (
    create_user,
    get_user_by_username,
)


def seed_user(
    username: str,
    full_name: str,
    email: str,
    password: str,
    role: str,
):
    if get_user_by_username(username):
        print(f"{username} already exists.")
        return

    create_user(
        username=username,
        full_name=full_name,
        email=email,
        password_hash=hash_password(password),
        role=role,
    )

    print(f"{username} created successfully.")


def seed_users():

    seed_user(
        username="admin",
        full_name="System Administrator",
        email="admin@promptshield.local",
        password="admin123",
        role="admin",
    )

    seed_user(
        username="analyst",
        full_name="Security Analyst",
        email="analyst@promptshield.local",
        password="analyst123",
        role="analyst",
    )

    seed_user(
        username="user",
        full_name="End User",
        email="user@promptshield.local",
        password="user123",
        role="user",
    )


if __name__ == "__main__":
    seed_users()