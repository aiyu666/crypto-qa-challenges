# Crypto API challenges
1. Test the public get candlestick API
2. Test the instrument depth websocket

## Setting the global env
1. Update the `.envExample` name to `.env`

## Task 1
```
pytest -m "candlestick"
```

## Task 2
```
pytest -m "book_instrument_depth"
```

# Crypto APP Challenge

## Task 1
1. Open the android device
2. Run the test case
```
pytest -k "test_user_can_go_to_nine_day_forecast"
```

## Task 2

1. Run the script
```
python capture_api/app.py
```



## How to run the test case?
### Run all of tests
```
pytest
```

### Run with tag
```
pytest -m "<tag>"
```

### Run with test case name
```
python -k "<test_case_name>"
```

## Report
The report will generate in the reports folder.
And the log file will also in there.
