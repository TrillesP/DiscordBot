def handle_response(message) -> str:
    u_message = message.lower()

    if u_message.startswith('oi'):
        return 'Olá!'