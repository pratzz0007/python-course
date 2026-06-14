import pandas as pd


def team_leaders_with_at_least_4_direct_reports(employees: pd.DataFrame) -> pd.DataFrame:
    """Return names of team leaders with at least 4 direct reports.

    Expected columns in `employees`:
      - id
      - name
      - department
      - leaderId (nullable)

    Returns a DataFrame with column: name
    """
    # Direct reports count per leaderId (exclude null leaderId)
    counts = (
        employees.dropna(subset=["leaderId"])
        .groupby("leaderId")
        .size()
        .reset_index(name="report_count")
    )

    # Keep leaders with at least 4 reports
    eligible_leader_ids = counts[counts["report_count"] >= 4]["leaderId"]

    # Join to get leader names
    leaders = employees[employees["id"].isin(eligible_leader_ids)][["name"]]

    return leaders.reset_index(drop=True)


# LeetCode-style wrapper (optional)
class Solution:
    def findTeamLeaderNames(self, employees: pd.DataFrame) -> pd.DataFrame:
        return team_leaders_with_at_least_4_direct_reports(employees)

