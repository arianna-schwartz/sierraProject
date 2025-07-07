#!/usr/bin/env python
from random import randint

from pydantic import BaseModel

from crewai.flow import Flow, listen, start

from sierraproject.crews.sierra_crew.sierraCrew import SierraCrew


def kickoff():
    print("Starting Sierra Crew login flow...")
    result = SierraCrew().crew().kickoff()
    print("Result:")
    print(result.raw)

if __name__ == "__main__":
    kickoff()
