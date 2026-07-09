Read the Apache-style access log located at /app/access.log and produce a JSON summary report.

Write the report to:

/app/report.json

The JSON object must satisfy all of the following:

1. Include a field named "total_requests" whose value is the total number of log entries in the access log.
2. Include a field named "unique_ips" whose value is the number of distinct client IP addresses appearing in the log.
3. Include a field named "top_path" whose value is the request path that appears most frequently in the access log.
4. The output must be valid JSON and contain exactly the three fields listed above.

You have 120 seconds to complete this task. Do not cheat by using online solutions or hints specific to this task.