def logout_from_imap(client):
    """
    Logs out from the IMAP server and handles any exceptions that may occur.

    :param client: An IMAPClient instance that is currently logged in.
    :raises TypeError: If the provided client is not an instance of IMAPClient.
    """
    try:
        client.logout()
        print("Logout successful!")
    except Exception as e:
        print(f"An error occurred during logout: {e}")
