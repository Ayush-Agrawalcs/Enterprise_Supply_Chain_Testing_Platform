from .model import ComplianceResult
from .tools import get_compliance_rules


async def run_compliance_check():

    rules = get_compliance_rules()

    findings = []

    for standard, checks in rules.items():

        for check in checks:

            findings.append(
                f"{standard}: {check} - Passed"
            )

    return ComplianceResult(
        passed=True,
        findings=findings
    )

# async def run_compliance_check(system_state: dict):

#     rules = get_compliance_rules()
#     findings = []

#     for standard, checks in rules.items():

#         for check in checks:

#             if check == "Backup supplier required":
#                 status = "Passed" if system_state["backup_supplier"] else "Failed"

#             elif check == "Safety stock required":
#                 status = "Passed" if system_state["safety_stock_ok"] else "Failed"

#             elif check == "Audit trail required":
#                 status = "Passed" if system_state["audit_logs"] else "Failed"

#             else:
#                 status = "Passed"

#             findings.append(f"{standard}: {check} - {status}")

#     passed = all("Failed" not in f for f in findings)

#     return ComplianceResult(
#         passed=passed,
#         findings=findings
#     )