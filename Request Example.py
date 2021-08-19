import requests
import json

def pivotPoints(symbol, timeframe, barId):

    # Verify argument types
    if type(symbol) != str:
        return {'status':'Invalid', 'error': 'Invalid symbol argument.'}
    if type(timeframe) != str:
        return {'status':'Invalid', 'error': 'Invalid timeframe argument.'}
    if isinstance(barId, (int, str)) == False:
        return {'status':'Invalid', 'error': 'Invalid barId argument.'}
    
    # Make request to api
    token = 'Insert your unique token here...'
    response = requests.get(f'https://www.fasthloc.co.uk/api/getbar.json?symbol={symbol}&timeframe={timeframe}&barid={str(barId)}&token={token}')

    # Verify server response
    if response.status_code != 200:
        # Return error if server response code is not 200
        return {'status':'Invalid', 'error': 'Error in server request.'}
    
    # Pull text string from response
    dataString = response.text

    # Parse text string as python dictionary
    dataDict = json.loads(dataString)

    # Access dictionary to assign high, low, close
    high = dataDict[0]['bar']['high']
    low = dataDict[0]['bar']['low']
    close = dataDict[0]['bar']['close']

    # Calculate Scale to round to the appropriate precision
    scale = len(str(high).split('.')[1])

    # Pivot Points
    pivot = round((high + low + close) / 3, scale)
    r1 = round((pivot * 2) - low, scale)
    s1 = round((pivot * 2) - high, scale)
    r2 = round(pivot + (high - low), scale)
    s2 = round(pivot - (high - low), scale)
    r3 = round(high + (2 * (pivot - low)), scale)
    s3 = round(low - (2 * (high - pivot)), scale)

    # Return Pivots Dictionary
    return {'status':'Valid', 'pivot':pivot, 'r1':r1, 's1':s1, 'r2':r2, 's2':s2, 'r3':r3, 's3':s3}

# Call function to assign Pivot variable
pivotDict = pivotPoints('GBPJPY', 'D1', 0)

# Check for valid return
if pivotDict['status'] == 'Valid':
    # Display Pivot Points
    print('Pivot: ' + str(pivotDict['pivot']))
    print('R1: ' + str(pivotDict['r1']))
    print('S1: ' + str(pivotDict['s1']))
    print('R2: ' + str(pivotDict['r2']))
    print('S2: ' + str(pivotDict['s2']))
    print('R3: ' + str(pivotDict['r3']))
    print('S3: ' + str(pivotDict['s3']))
else:
    # Handle error
    print(pivotDict['error'])


