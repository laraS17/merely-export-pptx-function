import azure.functions as func

def main(req: func.HttpRequest) -> func.HttpResponse:
    op = req.params.get('operationId')
    if not op:
        try:
            op = (req.get_json() or {}).get('operationId')
        except Exception:
            pass
    if not op:
        return func.HttpResponse("operationId is required", status_code=400)

    return func.HttpResponse(f"Export OK pour operationId={op}")
