def logout_from_imap(client):
    try:
        client.logout()
        print("Logout successful!")
    except Exception as e:
        print(f"An error occurred during logout: {e}")
