import os
import time
import requests
from typing import Any, Dict, Optional
from dotenv import load_dotenv


class DataCoreAPI:
    """
    OAuth2-authenticated wrapper for Sportradar DataCore.
    Handles token acquisition, caching, automatic renewal, and rate-limiting.
    """

    _TOKEN_BUFFER = 60  # Buffer time (in seconds) before token expire

    def __init__(
        self,
        base_url: str,
        auth_url: str,
        client_id: str,
        client_secret: str,
        sport: str,
        org_id: Optional[str] = None,
        scopes: Optional[list[str]] = None,
        timeout: int = 5,
        rate_limit_sleep: float = 1.0,
    ) -> None:
        """
        Initialize the DataCoreHandballAPI instance.

        Args:
            auth_url (str): The authentication URL for obtaining tokens.
            client_id (str): The client ID for OAuth2 authentication.
            client_secret (str): The client secret for OAuth2 authentication.
            sport (str): The sport type (default is "handball").
            org_id (Optional[str]): Organization ID.
            scopes (Optional[list[str]]): The list of scopes for API access.
            timeout (int): Timeout for HTTP requests in seconds.
            rate_limit_sleep (float): Sleep time to handle rate-limiting.
        """
        load_dotenv()  # Load environment variables from .env file
        self.base_url = base_url
        self.auth_url = auth_url
        self.client_id = client_id
        self.client_secret = client_secret
        self.sport = sport
        self.org_id = org_id
        self.scopes = scopes or ["read:organization"]
        self.timeout = timeout
        self.rate_limit_sleep = rate_limit_sleep

        # Initialize a session for HTTP requests with default headers
        self.session = requests.Session()
        self.session.headers.update(
            {
                "Accept": "application/json",
                "Content-Type": "application/json",
            }
        )

        self._token: Optional[str] = None  # Cached token
        self._expires_at: float = 0.0  # Token expiry timestamp

    def _authenticate(self) -> None:
        """
        Obtain a fresh JWT token using the client-credentials grant.

        This method sends a POST request to the authentication URL with the
        required payload and updates the session with the new token.
        """
        payload: Dict[str, Any] = {
            "credentialId": self.client_id,
            "credentialSecret": self.client_secret,
            "sport": self.sport,
            "organization": {"id": [self.org_id]},
            "scopes": self.scopes,
        }
        # Remove keys with None values from the payload
        payload = {k: v for k, v in payload.items() if v is not None}

        # print(json.dumps(payload, indent=4))
        # Send the authentication request
        resp = self.session.post(self.auth_url, json=payload, timeout=self.timeout)
        resp.raise_for_status()  # Raise an exception for HTTP errors
        data = resp.json().get("data", {})
        self._token = data["token"]  # Extract the token from the response

        # Calculate token expiry time (default to 1 hour if not provided)
        expires_in = data.get("expires_in", 3600)
        self._expires_at = time.time() + expires_in - self._TOKEN_BUFFER

        # Update the session headers with the new token
        self.session.headers.update({"Authorization": f"Bearer {self._token}"})
        print("Authenticated successfully.")

    def _ensure_token(self) -> None:
        """
        Ensure a valid token is available.

        This method checks if the token is missing
        or expired and refreshes it if necessary.
        """
        if not self._token or time.time() >= self._expires_at:
            self._authenticate()

    def _make_request(
        self,
        endpoint: str,
        method: str = "GET",
        params: Optional[Dict[str, Any]] = None,
        json: Optional[Dict[str, Any]] = None,
    ) -> Dict[str, Any]:
        """
        Make a general API request.

        Args:
            endpoint (str): The API endpoint (full URL or relative path).
            method (str): The HTTP method (default is "GET").
            params (Optional[Dict[str, Any]]): Query parameters for request.
            json (Optional[Dict[str, Any]]): JSON payload for the request.

        Returns:
            Dict[str, Any]: The JSON response from the API.
        """
        # Handle rate-limiting by sleeping before making the request
        time.sleep(self.rate_limit_sleep)
        self._ensure_token()  # Ensure a valid token is available

        # Construct the full URL if the endpoint is relative
        url = endpoint if endpoint.startswith("http") else endpoint
        resp = self.session.request(
            method=method.upper(),
            url=url,
            params=params,
            json=json,
            timeout=self.timeout,
        )
        resp.raise_for_status()  # Raise an exception for HTTP errors
        return resp.json()  # Return the JSON response


if __name__ == "__main__":
    # Load environment variables from a specific .env file
    load_dotenv(".env_prd", override=True)

    # Initialize the API client with environment variables
    api = DataCoreAPI(
        base_url=os.getenv("BASE_URL", ""),
        auth_url=os.getenv("AUTH_URL", ""),
        client_id=os.getenv("CLIENT_ID", ""),
        client_secret=os.getenv("CLIENT_SECRET", ""),
        org_id=os.getenv("CLIENT_ORGANIZATION_ID"),
        scopes=["read:organization"],
        sport="handball",
    )

    # Ensure the token is valid and ready for use
    api._ensure_token()
