import json
import datetime

# Simulated cloud resource telemetry data (e.g., CPU utilization %, active hours, and cost)
CLOUD_RESOURCES = [
    {"resource_id": "vm-ai-inference-01", "cpu_utilization_pct": 8.5, "running_hours": 150, "hourly_cost_usd": 0.05},
    {"resource_id": "vm-data-pipeline-02", "cpu_utilization_pct": 84.2, "running_hours": 45, "hourly_cost_usd": 0.08},
    {"resource_id": "vm-staging-sandbox-03", "cpu_utilization_pct": 2.1, "running_hours": 300, "hourly_cost_usd": 0.03},
    {"resource_id": "vector-db-node-04", "cpu_utilization_pct": 65.0, "running_hours": 120, "hourly_cost_usd": 0.10}
]

IDLE_CPU_THRESHOLD = 10.0  # Percentage below which a resource is considered idle/wasteful

def audit_cloud_resources(resources):
    print("=== STARTING CLOUD FINOPS & TELEMETRY AUDIT ===")
    timestamp = datetime.datetime.utcnow().isoformat()
    
    optimization_actions = []
    total_projected_spend = 0.0
    potential_savings = 0.0

    for res in resources:
        cost = res["running_hours"] * res["hourly_cost_usd"]
        total_projected_spend += cost
        
        status = "OPTIMAL"
        action = "None"

        # Flag underutilized resources
        if res["cpu_utilization_pct"] < IDLE_CPU_THRESHOLD:
            status = "IDLE / WASTEFUL"
            action = "Flagged for auto-shutdown or downscaling"
            potential_savings += cost

        optimization_actions.append({
            "resource_id": res["resource_id"],
            "cpu_pct": res["cpu_utilization_pct"],
            "current_status": status,
            "recommended_action": action,
            "total_cost_usd": round(cost, 2)
        })

    report = {
        "audit_timestamp": timestamp,
        "total_projected_spend_usd": round(total_projected_spend, 2),
        "potential_waste_savings_usd": round(potential_savings, 2),
        "resources_analyzed": optimization_actions
    }

    print(json.dumps(report, indent=4))
    return report

if __name__ == "__main__":
    audit_cloud_resources(CLOUD_RESOURCES)
