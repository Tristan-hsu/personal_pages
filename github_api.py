import requests
import os
from datetime import datetime

class GitHubAPI:
    def __init__(self):
        self.username = "Tristan-hsu"
        self.base_url = "https://api.github.com"
        self.token = os.environ.get("GITHUB_TOKEN")
        self.headers = {}
        if self.token:
            self.headers["Authorization"] = f"token {self.token}"
    
    def get_user_info(self):
        """Get user profile information"""
        try:
            response = requests.get(f"{self.base_url}/users/{self.username}", headers=self.headers)
            if response.status_code == 200:
                return response.json()
            return None
        except Exception as e:
            print(f"Error fetching user info: {e}")
            return None
    
    def get_repositories(self, sort="updated", per_page=10):
        """Get user repositories"""
        try:
            params = {
                "sort": sort,
                "per_page": per_page,
                "type": "owner"
            }
            response = requests.get(
                f"{self.base_url}/users/{self.username}/repos", 
                headers=self.headers,
                params=params
            )
            if response.status_code == 200:
                repos = response.json()
                # Filter out forks and add additional info
                filtered_repos = []
                for repo in repos:
                    if not repo.get('fork', False):
                        # Get languages for each repo
                        languages = self.get_repo_languages(repo['name'])
                        repo['languages'] = languages
                        filtered_repos.append(repo)
                return filtered_repos
            return []
        except Exception as e:
            print(f"Error fetching repositories: {e}")
            return []
    
    def get_repo_languages(self, repo_name):
        """Get programming languages used in a repository"""
        try:
            response = requests.get(
                f"{self.base_url}/repos/{self.username}/{repo_name}/languages",
                headers=self.headers
            )
            if response.status_code == 200:
                return response.json()
            return {}
        except Exception as e:
            print(f"Error fetching languages for {repo_name}: {e}")
            return {}
    
    def get_commit_activity(self, repo_name):
        """Get commit activity for a repository"""
        try:
            response = requests.get(
                f"{self.base_url}/repos/{self.username}/{repo_name}/commits",
                headers=self.headers,
                params={"per_page": 10}
            )
            if response.status_code == 200:
                commits = response.json()
                return len(commits)
            return 0
        except Exception as e:
            print(f"Error fetching commit activity for {repo_name}: {e}")
            return 0
