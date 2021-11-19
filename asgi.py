import json
from fastapi import HTTPException
from app import create_app
from weather.adapters.http.worldtime_api import WorldtimeRestApi
from weather.core.domain.use_cases.busca_utctime import BuscaUtcTime
from weather.core.model.request.busca_utctime_input import BuscaUtctimeInputDto
from weather.core.model.serializers.busca_utctime_serializer import (
    BuscaUtctimeJsonEncoder,
)

# Create application
app = create_app()


@app.get("/buscaUtcTime")
async def busca_utc_time(cidade: str) -> str:

    try:

        # Decode the request
        param_cidade = cidade

        ##
        ## Import implementations
        ##

        # Data repository
        repo = WorldtimeRestApi("worldtimeapi.org", endpoint="/api/timezone")
        # Or you can use another implementation
        # repo = FaketimeLib()

        ##
        ## Controller
        ##

        # Create the input use case dto
        area = "America/" + "_".join(
            [each_string.capitalize() for each_string in param_cidade.split("_")]
        )

        input_dto = BuscaUtctimeInputDto.from_dict({"area": area})

        # Use-case
        output_dto = BuscaUtcTime(input_dto, repo).run()

        ##
        ## Presenter
        ##
        # Transform the output use case dto to the expected client data format.

        return json.dumps(output_dto, cls=BuscaUtctimeJsonEncoder)

    except Exception as err:
        raise HTTPException(status_code=500, detail=str(err)) from err
