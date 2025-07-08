#!/usr/bin/env python
from random import randint

from crewai.flow import Flow, listen, start
from pydantic import BaseModel

from sierraproject.crews.sierra_crew.sierraCrew import SierraCrew


def kickoff():
    print("Starting Sierra Crew login flow...")
    result = (
        SierraCrew()
        .crew()
        .kickoff(inputs={"email": "arianna.schwartz@madison-reed.com"})
    )
    print("Result:")
    print(result.raw)


if __name__ == "__main__":
    kickoff()
