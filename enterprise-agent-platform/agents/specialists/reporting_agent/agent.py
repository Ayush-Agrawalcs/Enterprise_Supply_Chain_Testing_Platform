# from .templates import EXECUTIVE_TEMPLATE
# class ReportingAgent:

#     async def generate_report(
#         self,
#         plan,
#         scenario,
#         risk,
#         validation,
#         compliance,
#         execution
#     ):

#         # Safe handling if execution is not a dict
#         if not isinstance(execution, dict):
#             execution = {
#                 "result": str(execution)
#             }

#         # ==========================
#         # EXECUTIVE SUMMARY
#         # ==========================

#         summary = f"""
# Objective:
# {plan.objectives}

# Scenario Evaluated:
# {scenario.title}

# Workflow Status:
# Completed Successfully

# The supply chain testing workflow successfully completed:

# ✓ Test Planning
# ✓ Scenario Generation
# ✓ Risk Assessment
# ✓ Data Validation
# ✓ Compliance Verification
# ✓ Execution Simulation
# ✓ Executive Reporting
# """

#         # ==========================
#         # RISK ASSESSMENT
#         # ==========================

#         risk_text = f"""
# Risk Name:
# {risk.risk_name}

# Severity:
# {risk.severity}

# Impact:
# {risk.impact}

# Recommended Mitigation:
# {risk.mitigation}
# """

#         # ==========================
#         # VALIDATION SUMMARY
#         # ==========================

#         validation_text = "\n".join(
#             [
#                 f"✓ {finding}"
#                 for finding in validation.findings
#             ]
#         )

#         # ==========================
#         # COMPLIANCE SUMMARY
#         # ==========================

#         compliance_text = "\n".join(
#             [
#                 f"✓ {finding}"
#                 for finding in compliance.findings
#             ]
#         )

#         # ==========================
#         # EXECUTION RESULT
#         # ==========================

#         if "supplier_name" in execution:

#             execution_text = f"""
# Scenario Event:
# {execution.get("event", "N/A")}

# Supplier Name:
# {execution.get("supplier_name", "N/A")}

# Supplier ID:
# {execution.get("supplier_id", "N/A")}

# Country:
# {execution.get("country", "N/A")}

# Risk Score:
# {execution.get("risk_score", "N/A")}

# Business Impact:
# {execution.get("impact", "N/A")}
# """

#         elif "product" in execution:

#             execution_text = f"""
# Scenario Event:
# {execution.get("event", "N/A")}

# Product:
# {execution.get("product", "N/A")}

# SKU:
# {execution.get("sku", "N/A")}

# Current Stock:
# {execution.get("current_stock", "N/A")}

# Reorder Point:
# {execution.get("reorder_point", "N/A")}

# Business Impact:
# {execution.get("impact", "N/A")}
# """

#         elif "affected_systems" in execution:

#             execution_text = f"""
# Scenario Event:
# {execution.get("event", "N/A")}

# Affected Systems:
# {", ".join(execution.get("affected_systems", []))}

# Business Impact:
# {execution.get("impact", "N/A")}
# """

#         elif "affected_regions" in execution:

#             execution_text = f"""
# Scenario Event:
# {execution.get("event", "N/A")}

# Affected Regions:
# {", ".join(execution.get("affected_regions", []))}

# Business Impact:
# {execution.get("impact", "N/A")}
# """

#         else:

#             execution_text = "\n".join(
#                 [
#                     f"{key}: {value}"
#                     for key, value in execution.items()
#                 ]
#             )

#         # ==========================
#         # REMEDIATION PLAN
#         # ==========================

#         remediation_text = f"""
# Immediate Actions

# 1. Maintain backup suppliers for critical inventory.

# 2. Increase safety stock levels for high-risk products.

# 3. Implement automated inventory monitoring alerts.

# 4. Conduct regular supply chain audits.

# 5. Review supplier performance metrics regularly.

# 6. {risk.mitigation}

# Expected Benefits

# ✓ Reduced operational risk

# ✓ Improved inventory resilience

# ✓ Better supply chain continuity

# ✓ Stronger compliance posture
# """

#         # ==========================
#         # FINAL REPORT
#         # ==========================

#         report = EXECUTIVE_TEMPLATE.format(
#             summary=summary,
#             risk=risk_text,
#             validation=validation_text,
#             compliance=compliance_text,
#             execution=execution_text,
#             remediation=remediation_text
#         )

#         return report


# reporting_agent = ReportingAgent()

from .templates import EXECUTIVE_TEMPLATE


class ReportingAgent:

    async def generate_report(
        self,
        plan,
        scenario,
        risk,
        validation,
        compliance,
        execution
    ):

        # ==========================
        # EXECUTIVE SUMMARY
        # ==========================

        summary = f"""
Objective:
{plan.objectives}

Scenario Evaluated:
{scenario.title}

Workflow Status:
Completed Successfully

The supply chain testing workflow successfully completed:

✓ Test Planning
✓ Scenario Generation
✓ Risk Assessment
✓ Data Validation
✓ Compliance Verification
✓ Execution Simulation
✓ Executive Reporting
"""

        # ==========================
        # RISK ASSESSMENT
        # ==========================

        risk_text = f"""
Risk Name:
{risk.risk_name}

Severity:
{risk.severity}

Impact:
{risk.impact}

Recommended Mitigation:
{risk.mitigation}
"""

        # ==========================
        # VALIDATION SUMMARY
        # ==========================

        validation_text = "\n".join(
            f"✓ {finding}"
            for finding in validation.findings
        )

        # ==========================
        # COMPLIANCE SUMMARY
        # ==========================

        compliance_text = "\n".join(
            f"✓ {finding}"
            for finding in compliance.findings
        )

        # ==========================
        # EXECUTION RESULTS
        # ==========================

        execution_text = ""

        # Safety handling
        if not isinstance(execution, list):
            execution = [execution]

        for idx, item in enumerate(
            execution,
            start=1
        ):

            execution_text += (
                f"\n"
                f"Simulation {idx}\n"
                f"{'-' * 40}\n"
            )

            # Supplier Failure

            if "supplier_name" in item:

                execution_text += f"""
Scenario Event:
{item.get("event", "N/A")}

Supplier Name:
{item.get("supplier_name", "N/A")}

Supplier ID:
{item.get("supplier_id", "N/A")}

Country:
{item.get("country", "N/A")}

Risk Score:
{item.get("risk_score", "N/A")}

Business Impact:
{item.get("impact", "N/A")}

"""

            # Inventory Shortage

            elif "product" in item:

                execution_text += f"""
Scenario Event:
{item.get("event", "N/A")}

Product:
{item.get("product", "N/A")}

SKU:
{item.get("sku", "N/A")}

Current Stock:
{item.get("current_stock", "N/A")}

Reorder Point:
{item.get("reorder_point", "N/A")}

Business Impact:
{item.get("impact", "N/A")}

"""

            # Cyber Attack

            elif "affected_systems" in item:

                execution_text += f"""
Scenario Event:
{item.get("event", "N/A")}

Affected Systems:
{", ".join(item.get("affected_systems", []))}

Business Impact:
{item.get("impact", "N/A")}

"""

            # Natural Disaster

            elif "affected_regions" in item:

                execution_text += f"""
Scenario Event:
{item.get("event", "N/A")}

Affected Regions:
{", ".join(item.get("affected_regions", []))}

Business Impact:
{item.get("impact", "N/A")}

"""

            # Generic

            else:

                execution_text += "\n".join(
                    [
                        f"{k}: {v}"
                        for k, v in item.items()
                    ]
                )

                execution_text += "\n\n"

        # ==========================
        # REMEDIATION PLAN
        # ==========================

        remediation_text = f"""
Immediate Actions

1. Maintain backup suppliers for critical inventory.

2. Increase safety stock levels for high-risk products.

3. Implement automated inventory monitoring alerts.

4. Conduct regular supply chain audits.

5. Review supplier performance metrics regularly.

6. {risk.mitigation}

Expected Benefits

✓ Reduced operational risk

✓ Improved inventory resilience

✓ Better supply chain continuity

✓ Stronger compliance posture
"""

        # ==========================
        # FINAL REPORT
        # ==========================

        report = EXECUTIVE_TEMPLATE.format(
            summary=summary,
            risk=risk_text,
            validation=validation_text,
            compliance=compliance_text,
            execution=execution_text,
            remediation=remediation_text
        )

        return report


reporting_agent = ReportingAgent()