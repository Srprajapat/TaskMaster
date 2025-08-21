#!/usr/bin/env python3
import json
import sys
import urllib.request
import urllib.error

def main():
    url = "http://localhost:3000/"
    
    # Initialize test results
    results = [
        {"testNumber": 1, "status": "failed", "description": "Check if server is running"},
        {"testNumber": 2, "status": "failed", "description": "Check if Django welcome message is displayed"}
    ]
    
    try:
        with urllib.request.urlopen(url, timeout=5) as response:
            status_code = response.getcode()
            response_body = response.read().decode("utf-8")
            
            # Test 1: Check if the server is running (status 200)
            if status_code == 200:
                results[0]["status"] = "passed"
            
            # Test 2: Check if the default Django welcome message is present
            if "The install worked successfully!" in response_body:
                results[1]["status"] = "passed"
    
    except urllib.error.URLError as e:
        results[0]["error"] = str(e)
        results[1]["error"] = str(e)
    except Exception as e:
        results[0]["error"] = str(e)
        results[1]["error"] = str(e)

    # Write test results to JSON file
    with open("test-results.json", "w") as outfile:
        json.dump(results, outfile, indent=2)

    # Exit with non-zero status if any test failed
    if any(test["status"] == "failed" for test in results):
        sys.exit(1)

if __name__ == "__main__":
    main()
