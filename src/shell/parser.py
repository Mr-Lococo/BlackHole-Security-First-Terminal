def parser_command(command: str):
    try:
        if not command.strip():
            return []
        return command.split().strip()
    except Exception as e:
        print(f"[!] Error parsing command: {e}")
        return []