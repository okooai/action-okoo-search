import agentflow as af

async def handle():
    query = af.param("query")
    type_ = af.param("type")
    return await af.asearch(query=query, types=type_)