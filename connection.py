# connection.py
import os
import requests


class Connection:
    def __init__(self):
        self.jira_url = os.getenv("JIRA_URL")
        self.jira_pat = os.getenv("JIRA_PAT")

        if not self.jira_url:
            raise ValueError("JIRA_URL missing")

        if not self.jira_pat:
            raise ValueError("JIRA_PAT missing")

       

    @property
    def headers(self):
        return {
            "Authorization": f"Bearer {self.jira_pat}",
            "Accept": "application/json",
        }

    def test_connection(self):

        url = f"{self.jira_url}/rest/api/2/myself"

        response = requests.get(
        url,
        headers=self.headers,
        timeout=30,
        verify=False
        )

        return {
        "status_code": response.status_code,
        "response_text": response.text[:500]
        }

    def get_issue(self, issue_key):
        """
        Read a Jira issue by key.
        Example: BOM-1773
        """
        url = f"{self.jira_url}/rest/api/2/issue/{issue_key}"

        response = requests.get(
            url,
            headers=self.headers,
            verify=False,
            timeout=30
        )

        response.raise_for_status()
        return response.json()

    def search_issues(self, jql, expand=str):
        """
        Search Jira issues using JQL.
        """
        url = f"{self.jira_url}/rest/api/2/search"

        payload = {
            "jql": jql,
            "expand": expand
        }

        response = requests.get(
            url,
            headers=self.headers,
            params=payload,
            verify=False,
            timeout=30
        )

        response.raise_for_status()
        return response.json()

    def get_pat_length(self):
        """
        Diagnostic helper.
        """
        return len(self.jira_pat)