from knowledge_base.retriver import (
    retrieve_inventory
)


def get_inventory_context(
    query: str
):

    results = retrieve_inventory(
        query
    )

    return "\n".join(
        results
    )
