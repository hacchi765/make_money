# Coding Conventions

- **Python**: Follow PEP 8.
- **Logging**: Use standard `logging` library. All modules should verify execution with INFO logs.
- **Error Handling**: Catch exceptions in main loop to prevent one failure from stopping the entire batch.
- **Markdown Generation**: Ensure robust handling of multiline strings and front matter generation for Hugo.
- **Security**: Never commit `.env` or secrets. Use environment variables for all credentials.
