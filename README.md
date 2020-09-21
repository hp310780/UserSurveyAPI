# User Information API

A simple extendable API for gathering and presenting user information.

## Repository Structure
```
.
├── conftest.py [Pytest setup configuration]
├── .env [Environment Variables for running this API]
├── requirements.txt [Python dependencies]
├── _apis [All internal API endpoint code]
│   └── users.py
│   └── ...
├── _core
│   └── utils.py [Commonly used utilities]
├── _data [.json files representing a datastore]
│   ├── users.json
│   └── ...
├── _tests
│   ├── test_userss.py [Tests for users endpoint]
│   └── ...
└── README.md
```

## Installation

### Requirements
* Python3

Run the following in a shell:

```
> python3 -m venv venv
> source venv/bin/activate
> pip install -r requirements.txt
> flask run
```

Navigate to the following URL in your browser:
```
http://127.0.0.1:5000/
```

You should see the generated API swagger model.

## Design Requirements
* Ability to handle multiple question types.
* Ability to handle different survey flows.

### User Flow
1. User lands on initial web page asking for email.
2. User enters email.
3. User served questions.
4. User responses saved to user entity.

### Data Model
* User
    * Entity containing user information that is gathered through the survey.
* Survey
    * Entity containing a list of questions.
* Question
    * Entity encapsulating what to ask and the expected response type and values if applicable.
* Survey Response
    * Entity for storing the responses to a survey. This will be linked to a user entity.

This API currently uses .json files as a simple representation of a database for mocking purposes.

### To Be Done
* Authentication - Via JWTs.
* Validation 
    * Validation of request data via `flask-restplus`.
    * Validation of request data correctness via third party APIs.
* Page entity for survey allowing multiple questions per page.
* Clean up around development cycle - Perhaps a Makefile with Docker image to make installation and testing easier, more documentation of response and request types.
* Refactor api classes to use BaseDAO from `core/utils.py`.

## Testing

Please follow the [installation steps](##Installation). Then:
```
> py.test
```