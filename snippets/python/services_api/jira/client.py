from jira import JIRA

jira = JIRA('https://jira.atlassian.com', token_auth='')

issue = jira.issue('TSK-1')
print(issue.fields.project.key)
print(issue.fields.issuetype.name)
