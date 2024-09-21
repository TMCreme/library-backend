# Library Management System

## Description

## Running Locally
* Make sure docker and docker-compose are installed on your system
* Clone the project and switch to preferred branch
* Start the project with `docker compose up --build`
* When the docker container starts running successfully, visit the Swagger API documentation on `http://localhost:8091/api/docs` via the browser
* To run any migrations, run `docker-compose run --rm app app sh -c "python manage.py migrate"`
* To run tests, run `docker compose run --rm app sh -c "python manage.py test"`

## Deploying 

# Project Structure

The project follows a standard dbt project structure:

```
project_name/
|
|--- core
|--- libraryms
|--- scripts
|--- utils
```


## Contributing

To maintain the quality and readability of our project history, we require all contributions to adhere to the **Conventional Commits** standard.

### What are Conventional Commits?

Conventional Commits are a specification for adding human and machine-readable meaning to commit messages. This practice facilitates consistency across commit logs, enables automatic versioning, and aids in the generation of release notes.

### Commit Message Format

Each commit message should be structured as follows:

```
<type>: <description>
```

#### Allowed `<type>` values include:

- `feat` (new features)
- `fix` (bug fixes)
- `doc` (changes to documentation)
- `style` (formatting, missing semi colons, etc; no production code change)
- `refactor` (refactoring production code, e.g., renaming a variable)
- `test` (adding missing tests, refactoring tests; no production code change)
- `chore` (updating grunt tasks etc; no production code change)

### Example Commit Message

```bash
feat: add beta sequence
```
Describes a new feature added to the project.

### Your Contributions

Ensure your commit messages follow this format. This consistency helps us manage the log history and the project development more effectively. For more detailed information, refer to the [Conventional Commits](https://www.conventionalcommits.org/) specification.
