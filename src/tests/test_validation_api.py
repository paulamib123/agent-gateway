def testValidationAPISuccess(mocker, app, client):
        mocker.patch("src.services.validateAgentOutputService.postAgentLog", return_value=None)
        
        # Add the required data in dictionary format 
        data = {}
        response = client.post('/', json=data)

        assert response.status_code == 200

def testValidationAPIFailure(mocker, app, client):
        mocker.patch("src.services.validateAgentOutputService.postAgentLog", return_value=None)

        data = {}
        response = client.post('/', json=data)

        assert response.status_code == 500

